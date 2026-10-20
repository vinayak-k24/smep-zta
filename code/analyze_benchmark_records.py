#!/usr/bin/env python3
"""Analyze generated illustrative benchmark records; not a reanalysis of observed experiments."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "dataset" / "benchmark_evaluation_records.csv"
OUT = ROOT / "results" / "recomputed"
OUT.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(INPUT)
expected = "generated_illustrative_not_observed"
if not df["data_status"].eq(expected).all():
    raise SystemExit("Provenance check failed: expected generated illustrative records.")

rows = []
for variant, sub in df.groupby("system_variant"):
    adv = sub[sub["scenario_type"] == "adversarial"]
    ben = sub[sub["scenario_type"] == "benign"]
    rows.append({
        "system_variant": variant,
        "data_status": expected,
        "n_records": len(sub),
        "n_adversarial": len(adv),
        "n_benign": len(ben),
        "adversarial_block_rate": (adv["decision"] == "block").mean() if len(adv) else float("nan"),
        "benign_false_positive_rate": (ben["decision"] == "block").mean() if len(ben) else float("nan"),
        "median_latency_ms": sub["latency_ms"].median(),
        "mean_cpu_overhead_pct": sub["cpu_overhead_pct"].mean()
    })
pd.DataFrame(rows).to_csv(OUT / "metric_summary_by_variant.csv", index=False)
print(f"Analyzed {len(df):,} generated illustrative records. Outputs: {OUT}")
print("These results demonstrate the analysis workflow and are not measurements from the manuscript experiment.")
