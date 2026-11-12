# Equation figure renderer

This optional documentation tool renders LaTeX into self-contained SVG figures. It does not run or change the neuromechanical model.

The repository includes the finished figures, so viewing the documentation and running the simulation do not require Node.js or MathJax.

To rebuild changed equations, run these commands from the project root:

```sh
npm install --prefix Code/simulation_tools/equation_renderer
python Code/simulation_tools/generate_github_guides.py
```

- [Scientific equation sources](../../../Documentation/equations.json) define the numbered model equations.
- [Figure source index](../../../Documentation/Figures_and_Videos/Equations/equation_sources.json) preserves the LaTeX for every figure.
- [render_equations.cjs](render_equations.cjs) draws the mathematical symbols and equation numbers.
- [package.json](package.json) specifies the MathJax dependency version.
- [Documentation build guide](../../../Documentation/publishing.md) explains the HTML and GitHub documentation.
