# Local HTTP Loopback Platform Bindings v1

## Purpose

Freeze the allowed physical binding posture for `local_http_loopback` without
implementing a server.

## Allowed Bind Addresses

- `127.0.0.1`
- `::1`
- `localhost`

## Forbidden Default Binding

- `0.0.0.0`
- LAN interface
- public interface
- wildcard host exposure

## Notes

- `local_http_loopback` is not LAN exposure.
- Runtime will implement loopback listener and port lifecycle later.
