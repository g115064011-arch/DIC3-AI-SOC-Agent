"""Profile a GUIDE CSV: row/incident counts, label balance, and per-column null ratio / cardinality / samples.

Usage: python experiments/e0_profile_guide.py data/archive/GUIDE_Train.csv > experiments/results/guide_train_profile.json
"""
import sys, json
from collections import Counter, defaultdict
import pandas as pd

path = sys.argv[1]
SKIP_UNIQUE = {"Id", "AlertId"}
rows = 0
nulls = Counter()
uniq = defaultdict(set)
samples = {}
grade_rows = Counter()
incident_grade = {}
category = Counter()
mitre_present = 0
techniques = Counter()
orgs = set()
ts_min, ts_max = None, None
action_grouped = Counter()

for chunk in pd.read_csv(path, chunksize=1_000_000, dtype=str, keep_default_na=True):
    rows += len(chunk)
    for c in chunk.columns:
        col = chunk[c]
        nulls[c] += int(col.isna().sum())
        if c not in SKIP_UNIQUE and len(uniq[c]) < 2_000_000:
            uniq[c].update(col.dropna().unique())
        if c not in samples:
            samples[c] = col.dropna().head(5).tolist()
    grade_rows.update(chunk["IncidentGrade"].fillna("<NA>"))
    key = chunk["OrgId"] + "-" + chunk["IncidentId"]
    for k, g in zip(key, chunk["IncidentGrade"]):
        if isinstance(g, str):
            incident_grade[k] = g
    category.update(chunk["Category"].fillna("<NA>"))
    action_grouped.update(chunk["ActionGrouped"].fillna("<NA>"))
    m = chunk["MitreTechniques"].dropna()
    mitre_present += len(m)
    for v in m:
        techniques.update(v.split(";"))
    ts = chunk["Timestamp"].dropna()
    lo, hi = ts.min(), ts.max()
    ts_min = lo if ts_min is None or lo < ts_min else ts_min
    ts_max = hi if ts_max is None or hi > ts_max else ts_max
    print(f"... {rows:,} rows", file=sys.stderr)

out = {
    "rows": rows,
    "incidents": len(incident_grade),
    "orgs": len(uniq["OrgId"]),
    "timestamp_range": [ts_min, ts_max],
    "grade_by_row": dict(grade_rows),
    "grade_by_incident": dict(Counter(incident_grade.values())),
    "category": dict(category.most_common()),
    "action_grouped": dict(action_grouped),
    "mitre_row_ratio": round(mitre_present / rows, 4),
    "distinct_techniques": len(techniques),
    "top_techniques": techniques.most_common(15),
    "columns": {
        c: {
            "null_ratio": round(nulls[c] / rows, 4),
            "nunique": (len(uniq[c]) if c not in SKIP_UNIQUE else None),
            "samples": samples[c],
        }
        for c in samples
    },
}
print(json.dumps(out, ensure_ascii=False, indent=1))
