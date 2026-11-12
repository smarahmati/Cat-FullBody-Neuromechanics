/* Display complete saved signals in a movable window. No simulation is run here.
   Axes use absolute simulation time; reference and prediction share one clock. */
'use strict';
const data = JSON.parse(document.getElementById('comparison-data').textContent);
const el = id => document.getElementById(id);
const endTime = data.time[data.time.length - 1];
let start = 0, windowSize = Math.min(4, endTime), charts = [], hoverTime = null;
let playing = false, previousFrame = null, pendingFrame = null;
function nearest(time) {
  let low = 0, high = data.time.length - 1;
  while (low < high) { const mid = Math.floor((low + high) / 2); if (data.time[mid] < time) low = mid + 1; else high = mid; }
  return low;
}
function setStart(value) {
  start = Math.max(0, Math.min(Number(value) || 0, Math.max(0, endTime - windowSize)));
  el('start').value = start.toFixed(2); el('timeline').value = start;
  el('interval').textContent = `Showing ${start.toFixed(2)}–${Math.min(endTime,start+windowSize).toFixed(2)} s of 0–${endTime.toFixed(2)} s`;
  requestDraw();
}
function requestDraw() {
  if (pendingFrame !== null) return;
  pendingFrame = requestAnimationFrame(() => { pendingFrame = null; charts.forEach(draw); });
}
function buildCharts() {
  el('plots').replaceChildren(); el('plots').className = el('mode').value;
  charts = [];
  for (const trace of data[el('mode').value]) {
    if (el('limb').value !== 'all' && trace.limb !== Number(el('limb').value)) continue;
    const card = document.createElement('section'); card.className = 'chart';
    const title = document.createElement('h3'); title.textContent = trace.title;
    const canvas = document.createElement('canvas'); canvas.setAttribute('aria-label',trace.title); canvas.setAttribute('role','img');
    const text = document.createElement('p'); card.append(title,canvas,text); el('plots').append(card);
    const chart = {trace,canvas,text}; charts.push(chart);
    canvas.addEventListener('pointermove',event => { const rect = canvas.getBoundingClientRect(); const fraction = Math.max(0,Math.min(1,(event.clientX-rect.left-46)/(rect.width-60))); hoverTime = start+fraction*windowSize; requestDraw(); });
    canvas.addEventListener('pointerleave',() => { hoverTime = null; requestDraw(); });
  }
  requestDraw();
}
function draw(chart) {
  const {canvas,trace,text} = chart, rect = canvas.getBoundingClientRect();
  const width = rect.width, height = 245, ratio = Math.min(2,window.devicePixelRatio||1);
  canvas.width = Math.round(width*ratio); canvas.height = Math.round(height*ratio);
  const c = canvas.getContext('2d'); c.scale(ratio,ratio);
  const left=46,right=width-14,top=15,bottom=height-38, finish=Math.min(endTime,start+windowSize);
  const first=nearest(start), last=nearest(finish);
  let min=Infinity,max=-Infinity,sum=0,count=0;
  for(let i=first;i<=last;i++){min=Math.min(min,trace.prediction[i],trace.reference[i]);max=Math.max(max,trace.prediction[i],trace.reference[i]);sum+=(trace.prediction[i]-trace.reference[i])**2;count++;}
  const margin=Math.max((max-min)*.10,trace.unit==='N'?.25:1); min-=margin;max+=margin;
  const x=t=>left+(t-start)/Math.max(1e-9,finish-start)*(right-left), y=v=>bottom-(v-min)/(max-min)*(bottom-top);
  c.font='11px Arial';c.lineWidth=1;c.fillStyle='#345';c.strokeStyle='#e0e8ec';
  for(let i=0;i<=4;i++){let tx=start+(finish-start)*i/4,ty=min+(max-min)*i/4;c.beginPath();c.moveTo(x(tx),top);c.lineTo(x(tx),bottom);c.moveTo(left,y(ty));c.lineTo(right,y(ty));c.stroke();c.textAlign='center';c.fillText(tx.toFixed(1),x(tx),bottom+17);c.textAlign='right';c.fillText(ty.toFixed(1),left-5,y(ty)+4);}
  c.save();c.beginPath();c.rect(left,top,right-left,bottom-top);c.clip();
  for(const [values,color,dash] of [[trace.reference,'#222',[5,4]],[trace.prediction,'#087f9c',[]]]){c.strokeStyle=color;c.lineWidth=1.5;c.setLineDash(dash);c.beginPath();for(let i=Math.max(0,first-1);i<=last;i++){if(i===Math.max(0,first-1))c.moveTo(x(data.time[i]),y(values[i]));else c.lineTo(x(data.time[i]),y(values[i]));}c.stroke();}
  c.setLineDash([]);
  if(hoverTime!==null&&hoverTime>=start&&hoverTime<=finish){const i=nearest(hoverTime);c.strokeStyle='#bd801e';c.beginPath();c.moveTo(x(data.time[i]),top);c.lineTo(x(data.time[i]),bottom);c.stroke();for(const [value,color] of [[trace.prediction[i],'#087f9c'],[trace.reference[i],'#222']]){c.fillStyle=color;c.beginPath();c.arc(x(data.time[i]),y(value),3,0,2*Math.PI);c.fill();}text.textContent=`t ${data.time[i].toFixed(3)} s · predicted ${trace.prediction[i].toFixed(2)} · reference ${trace.reference[i].toFixed(2)} ${trace.unit}`;}
  else{text.textContent=`Window RMSE: ${Math.sqrt(sum/Math.max(1,count)).toFixed(2)} ${trace.unit}`;}
  c.restore();c.fillStyle='#345';c.textAlign='center';c.fillText('Simulation time (s)',(left+right)/2,height-6);c.textAlign='left';c.fillText(trace.unit,4,11);
}
function pause(){playing=false;previousFrame=null;el('play').textContent='Play window';}
function animate(timestamp){if(!playing)return;if(previousFrame!==null)setStart(start+(timestamp-previousFrame)/1000*.5);previousFrame=timestamp;if(start>=endTime-windowSize){pause();return;}requestAnimationFrame(animate);}
el('play').onclick=()=>{if(playing){pause();return;}if(start>=endTime-windowSize)setStart(0);playing=true;el('play').textContent='Pause';requestAnimationFrame(animate);};
for(const id of ['timeline','start'])el(id).addEventListener('input',()=>{pause();setStart(el(id).value);});
el('width').onchange=()=>{pause();windowSize=el('width').value==='all'?endTime:Math.min(Number(el('width').value),endTime);el('timeline').max=Math.max(0,endTime-windowSize);el('start').max=el('timeline').max;setStart(start);};
el('first').onclick=()=>{pause();setStart(0);};el('middle').onclick=()=>{pause();setStart((endTime-windowSize)/2);};el('last').onclick=()=>{pause();setStart(endTime-windowSize);};
el('back').onclick=()=>{pause();setStart(start-4);};el('next').onclick=()=>{pause();setStart(start+4);};
el('mode').onchange=buildCharts;el('limb').onchange=buildCharts;
window.addEventListener('resize',requestDraw);
el('timeline').max=Math.max(0,endTime-windowSize);el('start').max=el('timeline').max;buildCharts();setStart(0);
