/** Render a JSON batch on stdin into standalone SVGs in the supplied directory.
 * This tool changes documentation figures only. It never runs the model.
 * CAT_MATHJAX_PATH optionally locates a separately installed documentation toolset.
 */
const fs = require('fs');
const path = require('path');
const load = name => require(require.resolve('mathjax-full/js/' + name, {
  paths: [process.env.CAT_MATHJAX_PATH || __dirname]
}));
const {mathjax} = load('mathjax.js');
const {TeX} = load('input/tex.js');
const {SVG} = load('output/svg.js');
const {liteAdaptor} = load('adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = load('handlers/html.js');
const {AllPackages} = load('input/tex/AllPackages.js');
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const document = mathjax.document('', {
  InputJax: new TeX({packages: AllPackages}),
  OutputJax: new SVG({fontCache: 'none'})
});
const escape = text => String(text).replace(/&/g,'&amp;').replace(/</g,'&lt;')
  .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const destination = process.argv[2];
const equations = JSON.parse(fs.readFileSync(0, 'utf8'));
for (const equation of equations) {
  const container = document.convert(equation.rendered_latex, {display: true});
  const markup = adaptor.outerHTML(container);
  if (/data-mjx-error|data-mml-node="merror"/.test(markup)) {
    throw new Error('Invalid equation: ' + equation.label + '\n' + markup);
  }
  const inner = adaptor.firstChild(container);
  const [x,y,w,h] = adaptor.getAttribute(inner,'viewBox').split(/[ ,]+/).map(Number);
  if (![x,y,w,h].every(Number.isFinite) || w <= 0 || h <= 0) {
    throw new Error('Invalid equation bounds: ' + equation.label);
  }
  // MathJax's viewBox uses 1000 units per em. Use an ordinary readable font size.
  const fontSize = equation.inline ? 16 : 20;
  const scale = fontSize / 1000;
  const width = equation.inline ? Math.ceil(w*scale+4) : Math.max(960,Math.ceil(w*scale+100));
  const height = Math.ceil(h*scale+(equation.inline ? 6 : 32));
  const left = equation.inline ? 2 : (width-w*scale)/2;
  const top = equation.inline ? 3 : 16;
  const glyphs = adaptor.innerHTML(inner);
  const title = (equation.number ? `Equation ${equation.number}: ` : '') + equation.label;
  const number = equation.number ? `<text x="${width-14}" y="${height/2}" text-anchor="end" dominant-baseline="middle" font-family="Georgia, serif" font-size="16">(${equation.number})</text>` : '';
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title description"><title id="title">${escape(title)}</title><desc id="description">${escape(equation.latex)}</desc><rect width="100%" height="100%" rx="4" fill="#fff"/><g fill="#162c3a" stroke="#162c3a" color="#162c3a"><g transform="translate(${left-x*scale} ${top-y*scale}) scale(${scale})">${glyphs}</g>${number}</g></svg>\n`;
  fs.writeFileSync(path.join(destination,equation.file),svg,'utf8');
}
console.log('Rendered ' + equations.length + ' equation figures.');
