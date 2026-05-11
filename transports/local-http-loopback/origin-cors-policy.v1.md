# Local HTTP Loopback Origin and CORS Policy v1

## Purpose

Define browser-safe access posture for `local_http_loopback`.

## Required Policy

- no wildcard CORS
- no broad origin reflection
- allowlist local origins only
- browser access requires strict origin policy
- non-browser clients may use token or config posture instead of CORS

## Boundary

- CORS or origin failure is a transport or security failure, not an operation
  failure.
- This document does not implement middleware or origin evaluation behavior.
