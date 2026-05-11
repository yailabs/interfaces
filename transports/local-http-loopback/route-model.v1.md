# Local HTTP Loopback Route Model v1

## Purpose

Define the route posture for `local_http_loopback` without expanding or
implementing routes in this wave.

## Required Route Posture

- operation invocation route
- operation metadata or readiness route
- local health or readiness route
- discovery route
- optional stream discovery route as a pointer to `local_event_stream`

## Rules

- The contract may define route shapes, but it does not implement routing.
- OpenAPI expansion is deferred in API.05.
- Stream transport remains separate; loopback request-response routes do not
  become stream-frame carriers.
