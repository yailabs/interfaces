use std::fmt;
use std::io::{self, BufRead, Write};
use std::str::FromStr;

use serde::de::DeserializeOwned;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum LocalIpcRpcFrameType {
    #[serde(rename = "handshake.request")]
    HandshakeRequest,
    #[serde(rename = "handshake.response")]
    HandshakeResponse,
    #[serde(rename = "operation.request")]
    OperationRequest,
    #[serde(rename = "operation.response")]
    OperationResponse,
    #[serde(rename = "stream.open")]
    StreamOpen,
    #[serde(rename = "stream.frame")]
    StreamFrame,
    #[serde(rename = "stream.close")]
    StreamClose,
    #[serde(rename = "cancel.request")]
    CancelRequest,
    #[serde(rename = "heartbeat")]
    Heartbeat,
    #[serde(rename = "error")]
    Error,
}

impl LocalIpcRpcFrameType {
    pub fn as_str(self) -> &'static str {
        match self {
            Self::HandshakeRequest => "handshake.request",
            Self::HandshakeResponse => "handshake.response",
            Self::OperationRequest => "operation.request",
            Self::OperationResponse => "operation.response",
            Self::StreamOpen => "stream.open",
            Self::StreamFrame => "stream.frame",
            Self::StreamClose => "stream.close",
            Self::CancelRequest => "cancel.request",
            Self::Heartbeat => "heartbeat",
            Self::Error => "error",
        }
    }
}

impl fmt::Display for LocalIpcRpcFrameType {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(self.as_str())
    }
}

impl FromStr for LocalIpcRpcFrameType {
    type Err = &'static str;

    fn from_str(value: &str) -> Result<Self, Self::Err> {
        match value {
            "handshake.request" => Ok(Self::HandshakeRequest),
            "handshake.response" => Ok(Self::HandshakeResponse),
            "operation.request" => Ok(Self::OperationRequest),
            "operation.response" => Ok(Self::OperationResponse),
            "stream.open" => Ok(Self::StreamOpen),
            "stream.frame" => Ok(Self::StreamFrame),
            "stream.close" => Ok(Self::StreamClose),
            "cancel.request" => Ok(Self::CancelRequest),
            "heartbeat" => Ok(Self::Heartbeat),
            "error" => Ok(Self::Error),
            _ => Err("unsupported local_ipc_rpc frame type"),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LocalIpcRpcFrame<TPayload> {
    pub frame_schema: String,
    pub frame_id: String,
    pub frame_type: LocalIpcRpcFrameType,
    pub frame_version: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub request_id: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub correlation_id: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub stream_id: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub sequence: Option<u64>,
    pub payload_encoding: String,
    pub payload: TPayload,
    pub payload_size: usize,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub flags: Option<Vec<String>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub created_at: Option<String>,
}

impl<TPayload> LocalIpcRpcFrame<TPayload>
where
    TPayload: Serialize,
{
    pub fn new(
        frame_id: impl Into<String>,
        frame_type: LocalIpcRpcFrameType,
        frame_version: impl Into<String>,
        request_id: Option<String>,
        correlation_id: Option<String>,
        stream_id: Option<String>,
        payload: TPayload,
    ) -> serde_json::Result<Self> {
        let payload_size = serde_json::to_vec(&payload)?.len();
        Ok(Self {
            frame_schema: "api/transports/local-ipc-rpc/frame.v1".to_string(),
            frame_id: frame_id.into(),
            frame_type,
            frame_version: frame_version.into(),
            request_id,
            correlation_id,
            stream_id,
            sequence: None,
            payload_encoding: "json".to_string(),
            payload,
            payload_size,
            flags: None,
            created_at: None,
        })
    }
}

pub fn write_frame_json<TPayload, TWriter>(
    writer: &mut TWriter,
    frame: &LocalIpcRpcFrame<TPayload>,
) -> io::Result<()>
where
    TPayload: Serialize,
    TWriter: Write,
{
    let mut bytes =
        serde_json::to_vec(frame).map_err(|err| io::Error::new(io::ErrorKind::InvalidData, err))?;
    bytes.push(b'\n');
    writer.write_all(&bytes)
}

pub fn read_frame_json<TPayload, TReader>(
    reader: &mut TReader,
) -> io::Result<Option<LocalIpcRpcFrame<TPayload>>>
where
    TPayload: DeserializeOwned,
    TReader: BufRead,
{
    let mut line = String::new();
    let bytes = reader.read_line(&mut line)?;
    if bytes == 0 {
        return Ok(None);
    }
    let frame = serde_json::from_str(line.trim_end())
        .map_err(|err| io::Error::new(io::ErrorKind::InvalidData, err))?;
    Ok(Some(frame))
}
