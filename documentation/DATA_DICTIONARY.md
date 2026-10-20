# Data Dictionary

| Field | Meaning |
|---|---|
| `record_id` | Unique identifier for an  record |
| `data_status` | Provenance flag; all included records are generated  records |
| `scenario_type` | `adversarial` or `benign` |
| `threat_vector` | A1–A5 for  adversarial categories; BENIGN otherwise |
| `system_variant` | One of six  policy/control variants |
| `agent_id` | Identifier among 150 agent labels |
| `tool_endpoint_id` | Identifier among 45 endpoint labels |
| `risk_score` |  risk score in [0,1] |
| `gate_path` |  gate label derived from the risk score |
| `decision` |  allow/block outcome |
| `detected_or_blocked` | 1 if the  decision is block, otherwise 0 |
| `latency_ms` |  per-record latency in milliseconds |
| `cpu_overhead_pct` |  CPU overhead percentage |
| `experiment_seed` | Seed used for reproducible record generation |
