import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# ---- Data ----
df = pd.DataFrame({
    "Student": [f"S{i}" for i in range(1, 11)],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics":     [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry":   [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English":     [80, 84, 72, 91, 76, 80, 70, 95, 77, 89],
})
subjects = ["Mathematics", "Physics", "Chemistry", "English"]

# ---- Summary statistics ----
print("Summary statistics:\n")
print(df[subjects].describe().round(2))

corr = df[subjects].corr()
print("\nCorrelation matrix:\n")
print(corr.round(3))

df["Average"] = df[subjects].mean(axis=1)
top = df.loc[df["Average"].idxmax()]
low = df.loc[df["Average"].idxmin()]
print(f"\nTop performer   : {top['Student']} (avg {top['Average']:.1f})")
print(f"Lowest performer: {low['Student']} (avg {low['Average']:.1f})")

# ---- 1. Subject-wise score distributions ----
fig, axes = plt.subplots(1, 2, figsize=(18, 5.5))
fig.suptitle("Subject-wise Score Distributions", fontsize=16, fontweight="bold")

for subject in subjects:
    sns.histplot(df[subject], kde=True, bins=5, alpha=0.3, label=subject, ax=axes[0])
axes[0].set_title("Histograms with KDE")
axes[0].set_xlabel("Score")
axes[0].legend()

long_df = df.melt(id_vars="Student", value_vars=subjects,
                  var_name="Subject", value_name="Score")
sns.boxplot(data=long_df, x="Subject", y="Score", hue="Subject",
            palette="Set2", legend=False, ax=axes[1])
axes[1].set_title("Box Plot")

plt.tight_layout()
plt.savefig("Python/Q27/distributions.png", dpi=150)

# ---- 2. Pairwise relationships ----
pair = sns.pairplot(df[subjects], kind="reg", diag_kind="kde",
                    plot_kws={"line_kws": {"color": "red"}})
pair.figure.suptitle("Pairwise Relationships Between Subjects", y=1.02,
                     fontsize=16, fontweight="bold")
pair.savefig("Python/Q27/pairplot.png", dpi=150)

# ---- 3. Correlation heatmap ----
plt.figure(figsize=(7, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            vmin=0.8, vmax=1, square=True, linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("Python/Q27/heatmap.png", dpi=150)

plt.show()