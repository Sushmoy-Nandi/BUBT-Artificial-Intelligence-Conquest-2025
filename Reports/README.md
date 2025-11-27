# Reports: Figure Explanations

_Generated on 2025-11-27 21:18:59_

## 01. Distribution Of Bilirubin Levels

![Distribution Of Bilirubin Levels](./01_distribution_of_bilirubin_levels_20251127-205612.png)

Univariate distribution of Bilirubin. Right-skew expected; motivates log1p transform.

## 02. Distribution Of Albumin Levels

![Distribution Of Albumin Levels](./02_distribution_of_albumin_levels_20251127-205615.png)

Univariate distribution of Albumin. Lower values reflect poorer synthetic function.

## 03. Target Class Distribution (train)

![Target Class Distribution (train)](./03_target_class_distribution_(train)_20251127-205616.png)

Class counts for the target (C, CL, D). Inspect imbalance to guide CV and metrics.

## 04. Age

![Age](./04_age_20251127-205617.png)

Figure generated during EDA/modeling. Inspect title and axes to interpret trends, distributions, or performance.

## 05. Correlation Heatmap (train Numeric Features)

![Correlation Heatmap (train Numeric Features)](./05_correlation_heatmap_(train_numeric_features)_20251127-205618.png)

Correlation matrix among numeric labs. Blocks indicate multicollinearity; informs ratio features and pruning.

## 06. Missing Values (top 20) - Train

![Missing Values (top 20) - Train](./06_missing_values_(top_20)_-_train_20251127-205618.png)

Top columns by percent missing. Guides imputation strategy and potential missingness indicators.

## 07. Categorical Distribution Drug

![Categorical Distribution Drug](./07_categorical_distribution_drug_20251127-205619.png)

Category frequency for DRUG. Highlights dominant/rare categories and potential imbalance.

## 08. Categorical Distribution Ascites

![Categorical Distribution Ascites](./08_categorical_distribution_ascites_20251127-205619.png)

Category frequency for Ascites. Highlights dominant/rare categories and potential imbalance.

## 09. Categorical Distribution Hepatomegaly

![Categorical Distribution Hepatomegaly](./09_categorical_distribution_hepatomegaly_20251127-205619.png)

Category frequency for Hepatomegaly. Highlights dominant/rare categories and potential imbalance.

## 10. Categorical Distribution Spiders

![Categorical Distribution Spiders](./10_categorical_distribution_spiders_20251127-205620.png)

Category frequency for Spiders. Highlights dominant/rare categories and potential imbalance.

## 11. Categorical Distribution Edema

![Categorical Distribution Edema](./11_categorical_distribution_edema_20251127-205620.png)

Category frequency for Edema. Highlights dominant/rare categories and potential imbalance.

## 12. Figure

![Figure](./12_figure_20251127-205627.png)

Figure generated during EDA/modeling. Inspect title and axes to interpret trends, distributions, or performance.

## 13. Pca 2d Scatter (train Numeric)

![Pca 2d Scatter (train Numeric)](./13_pca_2d_scatter_(train_numeric)_20251127-205633.png)

2D PCA projection of numeric features colored by class to visualize global structure and overlap.

## 14. Confusion Matrix (oof)

![Confusion Matrix (oof)](./14_confusion_matrix_(oof)_20251127-211146.png)

OOF confusion matrix. Off-diagonals reveal systematic misclassifications between classes.

## 15. Reliability Diagram (oof)

![Reliability Diagram (oof)](./15_reliability_diagram_(oof)_20251127-211147.png)

Calibration curve comparing predicted confidence to empirical accuracy; assesses probability calibration.
