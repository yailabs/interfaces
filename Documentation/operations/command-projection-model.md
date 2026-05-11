# Command Projection Model

Command projection is a client-facing view over API operations. API owns the projection contract, not the client UX that renders it.

## Projection Sources

- Operation registry records.
- Operation projection records.
- Action descriptor records.
- Request/response schemas and conformance checks.

## Projection Rules

- A command projection must map back to a registered API operation or action descriptor.
- Client labels and grouping are presentation choices outside API ownership.
- Projection metadata may include family, capability, safety posture, required context, and transport eligibility.
- Runtime handler names are not command projection authority.

## Delegation

SDK documentation owns typed package interfaces. Console documentation owns terminal client interaction design. API documentation owns only the protocol projection they consume.
