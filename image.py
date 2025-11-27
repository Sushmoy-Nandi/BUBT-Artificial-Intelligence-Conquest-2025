# Reports Catalog — Auto-generate explanations for all saved images
from pathlib import Path
import re
from datetime import datetime

reports_dir = Path("Reports")
assert reports_dir.exists(), "Reports/ folder not found. Run the notebook cells that create figures first."

def parse_file(f: Path):
    # Expected pattern: "{seq}_{title_slug}_{timestamp}.png"
    stem = f.stem
    parts = stem.split("_")
    if len(parts) < 3:
        return {"seq": 9999, "title_slug": stem, "title_key": stem.lower(), "file": f.name}
    seq = parts[0]
    title_slug = "_".join(parts[1:-1]) if len(parts) > 2 else "_".join(parts[1:])
    # Normalize for matching keys
    title_key = re.sub(r"[^a-z0-9]+", "_", title_slug.lower()).strip("_")
    try:
        seq_i = int(seq)
    except:
        seq_i = 9999
    return {"seq": seq_i, "title_slug": title_slug, "title_key": title_key, "file": f.name}

def pretty_title(slug: str) -> str:
    t = slug.replace("_", " ").strip()
    # Keep common acronyms as-is
    t = t.replace("Oof", "OOF").replace("Roc", "ROC").replace("Pca", "PCA")
    # Minimal title-casing while preserving all-caps tokens
    return " ".join([w if w.isupper() else w.capitalize() for w in t.split()])

def explain_for_key(key: str, slug: str) -> str:
    # Specific mappings
    mapping = {
        "target_class_distribution_train": "Class counts for the target (C, CL, D). Inspect imbalance to guide CV and metrics.",
        "numeric_feature_histograms_subset": "Univariate histograms for selected numeric features to spot skew, outliers, and ranges.",
        "correlation_heatmap_train_numeric_features": "Correlation matrix among numeric labs. Blocks indicate multicollinearity; informs ratio features and pruning.",
        "missing_values_top_20_train": "Top columns by percent missing. Guides imputation strategy and potential missingness indicators.",
        "distribution_of_bilirubin_levels": "Univariate distribution of Bilirubin. Right-skew expected; motivates log1p transform.",
        "bilirubin_distribution_by_patient_status": "Bilirubin distribution split by Status (C, CL, D). Higher levels typically align with worse outcomes.",
        "distribution_of_albumin_levels": "Univariate distribution of Albumin. Lower values reflect poorer synthetic function.",
        "albumin_distribution_by_sex": "Albumin distribution by Sex. Checks for sex-related shifts or bias.",
        "pairplot_subset": "Pairwise relationships for a subset of features colored by class; quick visual separability check.",
        "pca_2d_scatter_train_numeric": "2D PCA projection of numeric features colored by class to visualize global structure and overlap.",
        "confusion_matrix_oof": "OOF confusion matrix. Off-diagonals reveal systematic misclassifications between classes.",
        "reliability_diagram_oof": "Calibration curve comparing predicted confidence to empirical accuracy; assesses probability calibration.",
    }
    # Patterned mappings
    if key.startswith("categorical_distribution_"):
        col = key.replace("categorical_distribution_", "")
        col = col.upper() if len(col) <= 4 else col.capitalize()
        return f"Category frequency for {col}. Highlights dominant/rare categories and potential imbalance."
    if key.startswith("categorical_distribution"):
        return "Category frequency plot for a clinical categorical feature; check dominant classes and rare levels."
    if "heatmap" in key and "correlation" in key:
        return mapping["correlation_heatmap_train_numeric_features"]
    if "reliability" in key and "diagram" in key:
        return mapping["reliability_diagram_oof"]
    if "confusion_matrix" in key:
        return mapping["confusion_matrix_oof"]
    if "histograms" in key:
        return mapping["numeric_feature_histograms_subset"]
    if "pca" in key and "2d" in key:
        return mapping["pca_2d_scatter_train_numeric"]
    if "bilirubin" in key and "distribution" in key:
        if "by" in key:
            return mapping["bilirubin_distribution_by_patient_status"]
        return mapping["distribution_of_bilirubin_levels"]
    if "albumin" in key and "distribution" in key:
        if "sex" in key:
            return mapping["albumin_distribution_by_sex"]
        return mapping["distribution_of_albumin_levels"]
    if "missing_values" in key or "missing" in key:
        return mapping["missing_values_top_20_train"]
    if "target_class_distribution" in key or ("target" in key and "distribution" in key):
        return mapping["target_class_distribution_train"]
    # Fallback
    return "Figure generated during EDA/modeling. Inspect title and axes to interpret trends, distributions, or performance."

images = [p for p in reports_dir.glob("*.png")]
items = [parse_file(p) for p in images]
items.sort(key=lambda x: (x["seq"], x["file"]))

lines = []
lines.append("# Reports: Figure Explanations")
lines.append("")
lines.append(f"_Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")
lines.append("")
for it in items:
    title = pretty_title(it["title_slug"])
    expl = explain_for_key(it["title_key"], it["title_slug"])
    lines.append(f"## {it['seq']:02d}. {title}")
    lines.append("")
    lines.append(f"![{title}](./{it['file']})")
    lines.append("")
    lines.append(f"{expl}")
    lines.append("")

readme_path = reports_dir / "README.md"
readme_path.write_text("\n".join(lines), encoding="utf-8")
print(f"[Reports] Wrote explanations for {len(items)} image(s) to: {readme_path}")
# Preview first few lines
print("\\n".join(lines[:12]))