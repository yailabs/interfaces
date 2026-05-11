use thiserror::Error;

pub type YaiResult<T> = Result<T, YaiError>;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum YaiStatus {
    Ok,
    Partial,
    Pending,
    Ready,
    Unavailable,
    Blocked,
    Denied,
    Error,
}

impl YaiStatus {
    pub fn as_str(self) -> &'static str {
        match self {
            Self::Ok => "ok",
            Self::Partial => "partial",
            Self::Pending => "pending",
            Self::Ready => "ready",
            Self::Unavailable => "unavailable",
            Self::Blocked => "blocked",
            Self::Denied => "denied",
            Self::Error => "error",
        }
    }
}

#[derive(Debug, Error)]
pub enum YaiError {
    #[error("YAI transport is not configured for operation {operation_id}")]
    TransportNotConfigured { operation_id: &'static str },

    #[error("YAI transport {transport} contract status for operation {operation_id}: {status}: {message}")]
    TransportContract {
        operation_id: &'static str,
        transport: &'static str,
        status: &'static str,
        message: String,
    },

    #[error("YAI transport unavailable for operation {operation_id}: {message}")]
    TransportUnavailable {
        operation_id: &'static str,
        message: String,
    },

    #[error("YAI operation unavailable for operation {operation_id}: {message}")]
    OperationUnavailable {
        operation_id: &'static str,
        message: String,
    },

    #[error("YAI decode error for operation {operation_id}: {message}")]
    DecodeError {
        operation_id: &'static str,
        message: String,
    },

    #[error("YAI API error for operation {operation_id}: {message}")]
    ApiError {
        operation_id: &'static str,
        message: String,
    },

    #[error("YAI unsupported transport behavior for operation {operation_id}: {message}")]
    Unsupported {
        operation_id: &'static str,
        message: String,
    },
}
