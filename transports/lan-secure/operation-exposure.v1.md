# LAN Secure Operation Exposure v1

## Purpose

Define when a runtime operation may be exposed over `lan_secure`.

## Rules

- LAN exposure is `blocked_by_default`
- an operation may use `lan_secure` only when the runtime enables LAN, the
  client is paired, the device is allowed, runtime policy allows the operation
  family, the API operation map allows `lan_secure`, and runtime guards allow
  the operation
- Local HTTP Loopback availability does not imply LAN exposure
- sensitive write, stream, platform-remote, and compatibility surfaces remain
  blocked unless explicitly allowed later

## Boundary

- API.07 defines exposure policy only
- no runtime exposure behavior is implemented here
