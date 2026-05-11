# LAN Secure Discovery v1

## Purpose

Define LAN endpoint discovery posture without implementing discovery.

## Rules

- explicit client or SDK configuration is the preferred LAN discovery path
- runtime-advertised discovery, if added later, must remain explicit opt-in
- discovery must never silently widen Local HTTP Loopback into LAN exposure
- discovery failures must distinguish `lan_disabled`, `runtime_unavailable`,
  and bind or trust posture failures

## Boundary

- API.07 does not implement LAN discovery or advertisement
