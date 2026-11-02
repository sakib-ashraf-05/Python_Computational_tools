import numpy as np
import matplotlib.pyplot as plt

# ---- Data ----
students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
hours = np.array([8, 10, 12, 15, 18, 20, 7, 14, 16, 22])
scores = np.array([65, 72, 75, 82, 88, 90, 60, 80, 85, 95])

# ---- Statistics ----
corr = np.corrcoef(hours, scores)[0, 1]
slope, intercept = np.polyfit(hours, scores, 1)

print(f"Study hours - mean: {hours.mean():.1f}, min: {hours.min()}, max: {hours.max()}")
print(f"Exam scores - mean: {scores.mean():.1f}, min: {scores.min()}, max: {scores.max()}")
print(f"Correlation coefficient (r): {corr:.3f}")
print(f"Trend line: score = {slope:.2f} * hours + {intercept:.2f}")

fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))
fig.suptitle("Study Hours vs Exam Scores", fontsize=16, fontweight="bold")

# ---- Histogram: study hours ----
axes[0].hist(hours, bins=5, color="#4c9be8", edgecolor="black")
axes[0].axvline(hours.mean(), color="red", linestyle="--", label=f"Mean = {hours.mean():.1f}")
axes[0].set_title("Distribution of Study Hours")
axes[0].set_xlabel("Study Hours / Week")
axes[0].set_ylabel("Number of Students")
axes[0].legend()

# ---- Histogram: exam scores ----
axes[1].hist(scores, bins=5, color="#6cc070", edgecolor="black")
axes[1].axvline(scores.mean(), color="red", linestyle="--", label=f"Mean = {scores.mean():.1f}")
axes[1].set_title("Distribution of Exam Scores")
axes[1].set_xlabel("Exam Score")
axes[1].set_ylabel("Number of Students")
axes[1].legend()

# ---- Scatter plot with trend line ----
axes[2].scatter(hours, scores, s=90, color="#d9534f", edgecolor="black", zorder=3)
for name, x, y in zip(students, hours, scores):
    axes[2].annotate(name, (x, y), textcoords="offset points", xytext=(6, -12), fontsize=9)
x_line = np.linspace(hours.min(), hours.max(), 100)
axes[2].plot(x_line, slope * x_line + intercept, color="black", linestyle="--",
             label=f"Trend line (r = {corr:.3f})")
axes[2].set_title("Study Hours vs Exam Score")
axes[2].set_xlabel("Study Hours / Week")
axes[2].set_ylabel("Exam Score")
axes[2].grid(True, linestyle="--", alpha=0.5)
axes[2].legend()

plt.tight_layout()
plt.savefig("Python/Q26/study_vs_score.png", dpi=150)
plt.show()