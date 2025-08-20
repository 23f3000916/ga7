# Interactive Relationship Explorer — Marimo notebook
# Author contact: 24ds1000034@ds.study.iitm.ac.in
# This notebook demonstrates reactive analysis of a bivariate relationship.
# Open in edit mode: `uvx marimo edit interactive_analysis_marimo.py`
# Run as an app:     `uvx marimo run interactive_analysis_marimo.py`
# Export to HTML:    `uvx marimo export interactive_analysis_marimo.py -o analysis.html`

import marimo as mo

app = mo.App()

@app.cell
def __(mo):
    # Cell 1 — Intro & purpose (no dependencies)
    # Documentation: This cell explains the notebook's goal.
    mo.md(
        """
        # Interactive Relationship Explorer
        This Marimo notebook is **reactive**: when you change a control,
        all dependent cells update automatically. Use the sliders below to
        generate data and observe how noise and sample size affect the
        relationship between variables.
        """
    )
    return ()

@app.cell
def __():
    # Cell 2 — Core imports (provides shared libraries to downstream cells)
    # Data flow: (none) -> (np, pd, plt)
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return np, pd, plt

@app.cell
def __(mo):
    # Cell 3 — UI controls (source of interactivity)
    # Data flow: user -> (n, noise)
    n = mo.ui.slider(start=100, stop=5000, step=100, value=1000, label="Sample size n")
    noise = mo.ui.slider(start=0.0, stop=2.0, step=0.1, value=0.5, label="Noise σ")
    mo.md(
        """
        ### Controls
        - {n}
        - {noise}
        """
    )
    # Return the widgets so their .value can be used by dependent cells
    return n, noise

@app.cell
def __(np, pd, n, noise):
    # Cell 4 — Data generation (depends on UI)
    # Data flow: (n.value, noise.value) -> (df)
    rng = np.random.default_rng(123)
    x = rng.normal(0, 1, size=n.value)
    y = 2.5 * x + rng.normal(0, noise.value, size=n.value)
    df = pd.DataFrame({"x": x, "y": y})
    # Lightweight preview for transparency (head only)
    df.head(10)
    return (df,)

@app.cell
def __(np, df):
    # Cell 5 — Summary statistics & simple linear fit (depends on df)
    # Data flow: (df) -> (corr, m, b)
    corr = df["x"].corr(df["y"])
    # Least-squares slope and intercept
    m, b = np.polyfit(df["x"], df["y"], 1)
    return corr, m, b

@app.cell
def __(np, plt, df, m, b):
    # Cell 6 — Visualization (depends on df and fit)
    # Data flow: (df, m, b) -> figure
    fig, ax = plt.subplots()
    ax.scatter(df["x"], df["y"], alpha=0.3, s=18)
    xs = np.linspace(df["x"].min(), df["x"].max(), 200)
    ax.plot(xs, m * xs + b, linewidth=2)
    ax.set_title("Scatter of y vs. x with fitted line")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fig
    return (fig,)

@app.cell
def __(mo, n, noise, corr, m, b):
    # Cell 7 — Dynamic markdown summary (reacts to widget state & stats)
    # Data flow: (n.value, noise.value, corr, m, b) -> live report
    mo.md(
        f"""
        ### Live summary
        - **n** = {n.value}
        - **σ** = {noise.value}
        - **Correlation** `corr(x, y)` ≈ **{corr:.3f}**
        - **Fitted model**: \(\hat{{y}} = {m:.2f}\,x + {b:.2f}\)
        
        **Interpretation.**
        Increasing noise (σ) weakens the linear relationship (reduces |corr|) and
        makes the fitted line less predictive; increasing n stabilizes estimates.
        """
    )
    return ()

if __name__ == "__main__":
    app.run()
