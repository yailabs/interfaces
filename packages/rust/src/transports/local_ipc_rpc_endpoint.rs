use std::env;
use std::fs;
use std::path::{Path, PathBuf};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum LocalIpcRpcEndpointSource {
    Explicit,
    Environment,
    DiscoveryFile,
    PlatformDefault,
}

impl LocalIpcRpcEndpointSource {
    pub fn as_str(self) -> &'static str {
        match self {
            Self::Explicit => "explicit",
            Self::Environment => "environment",
            Self::DiscoveryFile => "discovery_file",
            Self::PlatformDefault => "platform_default",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum LocalIpcRpcDiscoveryStatus {
    Configured,
    NotConfigured,
    EndpointMissing,
    PermissionDenied,
    VersionMismatch,
    RuntimeUnavailable,
}

impl LocalIpcRpcDiscoveryStatus {
    pub fn as_str(self) -> &'static str {
        match self {
            Self::Configured => "configured",
            Self::NotConfigured => "not_configured",
            Self::EndpointMissing => "endpoint_missing",
            Self::PermissionDenied => "permission_denied",
            Self::VersionMismatch => "version_mismatch",
            Self::RuntimeUnavailable => "runtime_unavailable",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct LocalIpcRpcEndpoint {
    pub path: PathBuf,
    pub source: LocalIpcRpcEndpointSource,
    pub status: LocalIpcRpcDiscoveryStatus,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct LocalIpcRpcDiscoveryFailure {
    pub status: LocalIpcRpcDiscoveryStatus,
    pub message: String,
}

impl LocalIpcRpcDiscoveryFailure {
    pub fn new(status: LocalIpcRpcDiscoveryStatus, message: impl Into<String>) -> Self {
        Self {
            status,
            message: message.into(),
        }
    }
}

fn runtime_root_from_env() -> Option<PathBuf> {
    if let Ok(value) = env::var("YAI_RUNTIME_ROOT") {
        let value = value.trim();
        if !value.is_empty() {
            return Some(PathBuf::from(value));
        }
    }

    if let Ok(value) = env::var("YAI_RUN_ROOT") {
        let value = value.trim();
        if !value.is_empty() {
            return Some(PathBuf::from(value).join("runtime"));
        }
    }

    for key in ["YAI_CANONICAL_ROOTFS", "YAI_ROOTFS"] {
        if let Ok(value) = env::var(key) {
            let value = value.trim();
            if !value.is_empty() {
                return Some(PathBuf::from(value).join("run/yai/runtime"));
            }
        }
    }

    None
}

pub fn runtime_discovery_file_path() -> PathBuf {
    let runtime_root = runtime_root_from_env().unwrap_or_else(|| {
        if cfg!(target_os = "macos") {
            env::var("HOME")
                .map(|home| PathBuf::from(home).join("Library/Application Support/yai/runtime"))
                .unwrap_or_else(|_| PathBuf::from("/run/yai/runtime"))
        } else {
            PathBuf::from("/run/yai/runtime")
        }
    });
    runtime_root.join("transport/local-ipc-rpc.endpoint")
}

pub fn platform_default_endpoint_path() -> PathBuf {
    if let Some(runtime_root) = runtime_root_from_env() {
        return runtime_root.join(platform_default_relative_name());
    }

    #[cfg(unix)]
    {
        if let Ok(xdg_runtime_dir) = env::var("XDG_RUNTIME_DIR") {
            let xdg_runtime_dir = xdg_runtime_dir.trim();
            if !xdg_runtime_dir.is_empty() {
                return PathBuf::from(xdg_runtime_dir).join("yai-local-ipc-rpc.sock");
            }
        }

        if cfg!(target_os = "macos") {
            if let Ok(home) = env::var("HOME") {
                let home = home.trim();
                if !home.is_empty() {
                    return PathBuf::from(home).join(
                        "Library/Application Support/yai/runtime/transport/local-ipc-rpc.sock",
                    );
                }
            }
        }

        PathBuf::from("/tmp/yai-local-ipc-rpc.sock")
    }

    #[cfg(not(unix))]
    {
        PathBuf::from(r"\\.\pipe\yai-local-ipc-rpc")
    }
}

fn platform_default_relative_name() -> &'static str {
    if cfg!(unix) {
        "transport/local-ipc-rpc.sock"
    } else {
        "transport/local-ipc-rpc.pipe"
    }
}

fn endpoint_exists(path: &Path) -> Result<(), LocalIpcRpcDiscoveryFailure> {
    match fs::metadata(path) {
        Ok(_) => Ok(()),
        Err(err) if err.kind() == std::io::ErrorKind::NotFound => {
            Err(LocalIpcRpcDiscoveryFailure::new(
                LocalIpcRpcDiscoveryStatus::EndpointMissing,
                format!("endpoint path missing: {}", path.display()),
            ))
        }
        Err(err) if err.kind() == std::io::ErrorKind::PermissionDenied => {
            Err(LocalIpcRpcDiscoveryFailure::new(
                LocalIpcRpcDiscoveryStatus::PermissionDenied,
                format!("endpoint path not accessible: {}", path.display()),
            ))
        }
        Err(err) => Err(LocalIpcRpcDiscoveryFailure::new(
            LocalIpcRpcDiscoveryStatus::RuntimeUnavailable,
            format!(
                "endpoint metadata unavailable for {}: {err}",
                path.display()
            ),
        )),
    }
}

fn finalize_candidate(
    path: PathBuf,
    source: LocalIpcRpcEndpointSource,
) -> Result<LocalIpcRpcEndpoint, LocalIpcRpcDiscoveryFailure> {
    if path.as_os_str().is_empty() {
        return Err(LocalIpcRpcDiscoveryFailure::new(
            LocalIpcRpcDiscoveryStatus::NotConfigured,
            "local_ipc_rpc endpoint path is empty",
        ));
    }

    endpoint_exists(&path)?;

    Ok(LocalIpcRpcEndpoint {
        path,
        source,
        status: LocalIpcRpcDiscoveryStatus::Configured,
    })
}

pub fn resolve_endpoint(
    explicit_endpoint: Option<&Path>,
    use_runtime_discovery_file: bool,
    use_platform_default: bool,
) -> Result<LocalIpcRpcEndpoint, LocalIpcRpcDiscoveryFailure> {
    if let Some(path) = explicit_endpoint.filter(|path| !path.as_os_str().is_empty()) {
        return finalize_candidate(path.to_path_buf(), LocalIpcRpcEndpointSource::Explicit);
    }

    if let Ok(value) = env::var("YAI_LOCAL_IPC_ENDPOINT") {
        let value = value.trim();
        if !value.is_empty() {
            return finalize_candidate(
                PathBuf::from(value),
                LocalIpcRpcEndpointSource::Environment,
            );
        }
    }

    if use_runtime_discovery_file {
        let discovery_file = runtime_discovery_file_path();
        match fs::read_to_string(&discovery_file) {
            Ok(contents) => {
                let candidate = contents
                    .lines()
                    .find(|line| !line.trim().is_empty())
                    .map(str::trim)
                    .unwrap_or("");
                if !candidate.is_empty() {
                    return finalize_candidate(
                        PathBuf::from(candidate),
                        LocalIpcRpcEndpointSource::DiscoveryFile,
                    );
                }
                if !use_platform_default {
                    return Err(LocalIpcRpcDiscoveryFailure::new(
                        LocalIpcRpcDiscoveryStatus::EndpointMissing,
                        format!(
                            "runtime discovery file did not contain an endpoint: {}",
                            discovery_file.display()
                        ),
                    ));
                }
            }
            Err(err) if err.kind() == std::io::ErrorKind::NotFound => {
                if !use_platform_default {
                    return Err(LocalIpcRpcDiscoveryFailure::new(
                        LocalIpcRpcDiscoveryStatus::EndpointMissing,
                        format!(
                            "runtime discovery file missing: {}",
                            discovery_file.display()
                        ),
                    ));
                }
            }
            Err(err) if err.kind() == std::io::ErrorKind::PermissionDenied => {
                return Err(LocalIpcRpcDiscoveryFailure::new(
                    LocalIpcRpcDiscoveryStatus::PermissionDenied,
                    format!(
                        "runtime discovery file not accessible: {} ({err})",
                        discovery_file.display()
                    ),
                ));
            }
            Err(err) => {
                return Err(LocalIpcRpcDiscoveryFailure::new(
                    LocalIpcRpcDiscoveryStatus::RuntimeUnavailable,
                    format!(
                        "runtime discovery file unavailable: {} ({err})",
                        discovery_file.display()
                    ),
                ));
            }
        }
    }

    if use_platform_default {
        return finalize_candidate(
            platform_default_endpoint_path(),
            LocalIpcRpcEndpointSource::PlatformDefault,
        );
    }

    Err(LocalIpcRpcDiscoveryFailure::new(
        LocalIpcRpcDiscoveryStatus::NotConfigured,
        "no explicit, environment, discovery-file, or platform-default local_ipc_rpc endpoint is configured",
    ))
}
