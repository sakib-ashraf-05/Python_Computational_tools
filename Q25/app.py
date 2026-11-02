import matplotlib
import matplotlib.pyplot as plt

# ---- Data ----
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

# ---- Highest / lowest ----
max_sales, min_sales = max(sales), min(sales)
max_month = months[sales.index(max_sales)]
min_month = months[sales.index(min_sales)]

print(f"Highest sales: {max_month} - ₹{max_sales:,}")
print(f"Lowest sales : {min_month} - ₹{min_sales:,}")
print(f"Total revenue: ₹{sum(sales):,}")
print(f"Average/month: ₹{sum(sales)/len(sales):,.0f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle("Monthly Sales Revenue - Retail Store", fontsize=16, fontweight="bold")

# ---- Line chart ----
ax1.plot(months, sales, marker="o", color="#1f77b4", linewidth=2, label="Sales")
ax1.scatter(max_month, max_sales, color="green", s=150, zorder=5,
            label=f"Highest ({max_month})")
ax1.scatter(min_month, min_sales, color="red", s=150, zorder=5,
            label=f"Lowest ({min_month})")
ax1.annotate(f"₹{max_sales:,}", (max_month, max_sales),
             textcoords="offset points", xytext=(-35, 10), color="green", fontweight="bold")
ax1.annotate(f"₹{min_sales:,}", (min_month, min_sales),
             textcoords="offset points", xytext=(5, -18), color="red", fontweight="bold")
ax1.set_title("Line Chart")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales (₹)")
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend()

# ---- Bar chart ----
colors = ["green" if s == max_sales else "red" if s == min_sales else "#4c9be8"
          for s in sales]
bars = ax2.bar(months, sales, color=colors)
for bar, s in zip(bars, sales):
    ax2.text(bar.get_x() + bar.get_width() / 2, s + 800, f"{s/1000:.0f}k",
             ha="center", fontsize=9)
ax2.set_title("Bar Chart (green = highest, red = lowest)")
ax2.set_xlabel("Month")
ax2.set_ylabel("Sales (₹)")
ax2.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("Python/Q25/sales_charts.png", dpi=150)
plt.show()