# Transport Model

The SDK does not assume local or remote runtime by default.

Current status:
- transport is abstract
- no HTTP gateway is assumed
- no IPC/socket transport is claimed

Future transports may include HTTP, IPC, local socket, or embedded adapters when canonical runtime/API transport surfaces are available.

Wave 22D3 note:
- runtime lifecycle/status payloads may include sealed posture fields;
- SDK forwards sealed status as typed data;
- transport abstraction remains unchanged.

Wave 22D4 visibility note:
- SDK may expose client-connection/operator-context posture fields coming from
  runtime status projection;
- this remains read-model visibility only, without transport-side connect/disconnect behavior.

Wave 22D5 visibility note:
- SDK may expose active-case readiness fields (`activeCasePosture`,
  `activeCaseReason`, `activeCaseRef`) as operator-context projection;
- this remains status visibility only and does not imply case selection behavior.

Wave 22D7 note:
- runtime status may include service-boundary fields for lifecycle/manager/install posture and operational readiness;
- transport abstraction is unchanged and does not imply system service control.
