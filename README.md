# SMEP-ZTA Benchmark Evaluation Package

## Data provenance
They are provided for testing the analysis workflow, checking output tables, and demonstrating the data schema. 

## Contents
- `dataset/benchmark_evaluation_records.csv`: 15,450 generated  action records (12,400 adversarial and 3,050 benign), with 150 agent identifiers and 45 tool endpoint identifiers.
- `results/_metric_summary_by_variant.csv`: metric summaries by six system variants, calculated from the included records.
- `results/_threat_breakdown.csv`:  breakdown by A1–A5 and benign category.
- `results/_confusion_counts.csv`:  TP/FN/FP/TN counts by variant.
- `configuration/benchmark_config.json`: generation seed, scenario design, and manuscript-reported reference values.
- `code/analyze_benchmark_records.py`: reproducible analysis script.
- `documentation/REVIEWER_DATA_PROVENANCE.md`: provenance wording and checklist.
- `documentation/DATA_DICTIONARY.md`: field definitions.

## Run the analysis
```bash
python code/analyze_benchmark_records.py
```
The script writes derived summaries to `results/recomputed/`.
