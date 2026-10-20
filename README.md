# SMEP-ZTA Benchmark Evaluation Package

## Data provenance
**The included records are generated illustrative benchmark records, not observed experimental data.** They are provided for testing the analysis workflow, checking output tables, and demonstrating the data schema. They do not validate or substantiate the experimental claims in the manuscript.

## Contents
- `dataset/benchmark_evaluation_records.csv`: 15,450 generated illustrative action records (12,400 adversarial and 3,050 benign), with 150 agent identifiers and 45 tool endpoint identifiers.
- `results/illustrative_metric_summary_by_variant.csv`: metric summaries by six system variants, calculated from the included records.
- `results/illustrative_threat_breakdown.csv`: illustrative breakdown by A1–A5 and benign category.
- `results/illustrative_confusion_counts.csv`: illustrative TP/FN/FP/TN counts by variant.
- `configuration/benchmark_config.json`: generation seed, scenario design, and manuscript-reported reference values.
- `code/analyze_benchmark_records.py`: reproducible analysis script.
- `documentation/REVIEWER_DATA_PROVENANCE.md`: provenance wording and checklist.
- `documentation/DATA_DICTIONARY.md`: field definitions.

## Relationship to the manuscript
The illustrative dataset uses a scale of 15,450 total rows, including 12,400 adversarial and 3,050 benign records, to provide a coherent example structure. The manuscript describes 150 agents and 45 tool endpoints, but reports both 15,450 total scenarios and 12,400 adversarial scenarios in different sections. Confirm the actual counts against original logs before submission.

The manuscript reports 94.94% adversarial action block rate, 0.13% false-positive rate, macro F1 0.940, p50 latency 18.4 ms, and CPU overhead 3.23%. These values are included as manuscript-reported references only. The included records do not reproduce or verify those claims.

## Run the analysis
```bash
python code/analyze_benchmark_records.py
```
The script writes derived summaries to `results/recomputed/`.
