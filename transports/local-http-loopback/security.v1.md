# Local HTTP Loopback Security v1

## Purpose

Freeze the minimum security posture for the loopback HTTP transport.

## Security Baseline

- loopback-only default
- same-machine by default
- no LAN exposure by default
- no default wildcard CORS
- local client token or equivalent required before sensitive operations
- explicit dev-mode posture if unauthenticated local read surfaces are allowed
- no raw provider credential exposure
- no provider or model direct transport through browser

## Bind Posture

- allowed bind addresses: `127.0.0.1`, `::1`, `localhost`
- forbidden default binding: `0.0.0.0`, LAN interface, public interface,
  wildcard host exposure
