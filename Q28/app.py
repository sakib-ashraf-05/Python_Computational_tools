import pandas as pd
import plotly.express as px

# ---- Data ----
df = pd.DataFrame({
    "Student": [f"S{i}" for i in range(1, 11)],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
})

avg = df["Mathematics"].mean()
top = df.loc[df["Mathematics"].idxmax()]
low = df.loc[df["Mathematics"].idxmin()]

print(f"Average marks: {avg:.1f}")
print(f"Highest: {top['Student']} ({top['Mathematics']})")
print(f"Lowest : {low['Student']} ({low['Mathematics']})")

# ---- Interactive bar chart ----
fig = px.bar(
    df,
    x="Student",
    y="Mathematics",
    text="Mathematics",
    color="Mathematics",
    color_continuous_scale="Blues",
    title="Mathematics Marks of Students",
    labels={"Mathematics": "Marks"},
)

fig.update_traces(textposition="outside")
fig.add_hline(y=avg, line_dash="dash", line_color="red",
              annotation_text=f"Average = {avg:.1f}",
              annotation_position="top left")
fig.update_layout(
    yaxis_range=[0, 105],
    template="plotly_white",
    title_x=0.5,
    coloraxis_showscale=False,
    hovermode="x",
)

fig.write_html("Python/Q28/maths_bar_chart.html")     # shareable interactive file
fig.show()                                            # opens in your browser