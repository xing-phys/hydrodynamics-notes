(() => {
  'use strict';
  const NS = 'http://www.w3.org/2000/svg';
  const colors = {primary:'#16776f', secondary:'#c38149', muted:'#96aaa4'};
  const node = (name, attrs={}, text) => {
    const e=document.createElementNS(NS,name);
    for(const [k,v] of Object.entries(attrs)) e.setAttribute(k,String(v));
    if(text!==undefined) e.textContent=text;
    return e;
  };
  function chart(id, xDomain, yDomain, xLabel, yLabel) {
    const svg=document.getElementById(id);
    if(!svg) return null;
    svg.querySelectorAll(':scope > g').forEach(e=>e.remove());
    const g=node('g'); svg.append(g);
    const h=Number(svg.viewBox.baseVal.height), w=720;
    const pad={l:65,r:24,t:25,b:55};
    const x=v=>pad.l+(v-xDomain[0])/(xDomain[1]-xDomain[0])*(w-pad.l-pad.r);
    const y=v=>h-pad.b-(v-yDomain[0])/(yDomain[1]-yDomain[0])*(h-pad.t-pad.b);
    for(let i=0;i<=4;i++) {
      const xv=xDomain[0]+(xDomain[1]-xDomain[0])*i/4;
      const yv=yDomain[0]+(yDomain[1]-yDomain[0])*i/4;
      g.append(node('line',{x1:x(xv),x2:x(xv),y1:pad.t,y2:h-pad.b,stroke:'currentColor',opacity:'.09'}));
      g.append(node('line',{x1:pad.l,x2:w-pad.r,y1:y(yv),y2:y(yv),stroke:'currentColor',opacity:'.09'}));
      g.append(node('text',{x:x(xv),y:h-pad.b+23,'text-anchor':'middle',fill:'currentColor','font-size':12},Number(xv.toFixed(2))));
      g.append(node('text',{x:pad.l-10,y:y(yv)+4,'text-anchor':'end',fill:'currentColor','font-size':12},Number(yv.toFixed(2))));
    }
    g.append(node('line',{x1:pad.l,x2:w-pad.r,y1:h-pad.b,y2:h-pad.b,stroke:'currentColor',opacity:'.5'}));
    g.append(node('text',{x:(w+pad.l-pad.r)/2,y:h-8,'text-anchor':'middle',fill:'currentColor','font-size':13},xLabel));
    g.append(node('text',{x:pad.l,y:15,fill:'currentColor','font-size':13},yLabel));
    const curve=(points,color=colors.primary,extra={})=>g.append(node('path',{d:points.map(([a,b],i)=>`${i?'L':'M'}${x(a).toFixed(2)},${y(b).toFixed(2)}`).join(' '),fill:'none',stroke:color,'stroke-width':2.5,...extra}));
    return {svg,g,x,y,curve};
  }
  function bind(id, fn) { const e=document.getElementById(id); if(e) e.addEventListener('input',fn); }
  function diffusion() {
    if(!document.getElementById('diffusion-lab'))return;
    const D=Number(document.getElementById('diffusion-D').value),t=Number(document.getElementById('diffusion-t').value);
    document.getElementById('diffusion-D-value').textContent=D.toFixed(1);
    document.getElementById('diffusion-t-value').textContent=t.toFixed(1);
    const c=chart('diffusion-plot',[-8,8],[0,.45],'Position x','Probability density P');
    const points=s=>Array.from({length:401},(_,i)=>{const x=-8+16*i/400;return [x,Math.exp(-x*x/(2*s))/Math.sqrt(2*Math.PI*s)];});
    c.curve(points(1),colors.muted,{'stroke-dasharray':'5 4'});
    c.curve(points(1+2*D*t));
    document.getElementById('diffusion-status').textContent=`Variance = ${(1+2*D*t).toFixed(2)} · Standard deviation = ${Math.sqrt(1+2*D*t).toFixed(2)} · Dashed: initial packet; solid: current packet.`;
  }
  function modePoles(k) { const v=k*k-.25; return v>=0?[[Math.sqrt(v),-.5],[-Math.sqrt(v),-.5]]:[[0,-.5+Math.sqrt(-v)],[0,-.5-Math.sqrt(-v)]]; }
  function modes() {
    if(!document.getElementById('modes-lab'))return;
    const k=Number(document.getElementById('modes-k').value);
    document.getElementById('modes-k-value').textContent=k.toFixed(2);
    const c=chart('modes-plot',[-2.1,2.1],[-1.15,.1],'Real frequency Re ω','Imaginary frequency Im ω');
    for(let b=0;b<2;b++)c.curve(Array.from({length:401},(_,i)=>modePoles(2*i/400)[b]),colors.muted,{'stroke-width':2,'stroke-dasharray':'4 3'});
    const poles=modePoles(k);
    poles.forEach(([a,b],i)=>c.g.append(node('circle',{cx:c.x(a),cy:c.y(b),r:7,fill:i?colors.secondary:colors.primary,stroke:'var(--bs-body-bg)'})));
    document.getElementById('modes-status').textContent=`ω₊ = ${poles[0][0].toFixed(3)} ${poles[0][1]<0?'−':'+'} ${Math.abs(poles[0][1]).toFixed(3)}i; ω₋ = ${poles[1][0].toFixed(3)} − ${Math.abs(poles[1][1]).toFixed(3)}i. ${k<.5?'Two purely decaying modes.':k>.5?'Two damped propagating modes.':'The poles coincide.'}`;
  }
  function waves() {
    if(!document.getElementById('waves-lab'))return;
    const loga=Number(document.getElementById('waves-alpha').value),a=10**loga;
    document.getElementById('waves-alpha-value').textContent=loga.toFixed(1);
    const maxSpeed=Math.max(1.1,Math.sqrt((.05+20*a)*Math.tanh(20))*1.08);
    const c=chart('waves-plot',[0,20],[0,maxSpeed],'Dimensionless wave number q = kH','Phase speed / √(gH)');
    const points=alpha=>Array.from({length:401},(_,i)=>{const q=20*i/400;return[q,q===0?1:Math.sqrt((1/q+alpha*q)*Math.tanh(q))];});
    c.curve(points(0),colors.muted,{'stroke-dasharray':'5 4'});
    c.curve(points(a));
    document.getElementById('waves-status').textContent=`α = ${a.toPrecision(3)} · Gravity and capillarity are equal at q = 1/√α = ${(1/Math.sqrt(a)).toFixed(2)}. Dashed: zero surface tension; solid: selected α. The vertical scale adjusts to keep the curve visible.`;
  }
  document.addEventListener('DOMContentLoaded',()=>{
    bind('diffusion-D',diffusion);bind('diffusion-t',diffusion);bind('modes-k',modes);bind('waves-alpha',waves);
    diffusion();modes();waves();
  });
})();
