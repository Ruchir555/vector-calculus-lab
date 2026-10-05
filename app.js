/* Canvas rendering and lesson controls. The mathematics lives in math.js. */
'use strict';
const $=id=>document.getElementById(id);
const {lessons,sum}=Lab;
let index=0, model, probe=[0.45,0.35,0], enabled=[];
const a=$('a'),b=$('b'),z=$('z'),r=$('r');
const W=600,H=440,pad=35,extent=2;
const sx=x=>pad+(x+extent)/(2*extent)*(W-2*pad);
const sy=y=>H-pad-(y+extent)/(2*extent)*(H-2*pad);
const fmt=x=>{if(Array.isArray(x))return '('+x.map(fmt).join(', ')+')';return Math.abs(x)<1e-7?'0':Math.abs(x)<0.001?x.toExponential(2):x.toFixed(3);};
const norm=x=>typeof x==='number'?Math.abs(x):Math.hypot(...x);
const minus=(x,y)=>typeof x==='number'?x-y:VC.sub(x,y);
function safe(fn,p){if(model.singular&&Math.hypot(p[0],p[1])<0.22)return null;try{const v=fn(p);return (typeof v==='number'?Number.isFinite(v):v.every(Number.isFinite))?v:null;}catch{return null;}}
function reset(){a.value=1;b.value=0.7;z.value=0;r.value=0.5;probe=[0.45,0.35,0];$('view').value='source';$('arrows').checked=true;$('contours').checked=true;enabled=model.rhs.map(()=>true);buildTerms();draw();}
let group='';
lessons.forEach((lesson,i)=>{
  if(lesson.group!==group){group=lesson.group;const label=document.createElement('div');label.className='group';label.textContent=group;$('chapters').append(label);}
  const btn=document.createElement('button');btn.type='button';btn.innerHTML='<span class="num">'+String(i+1).padStart(2,'0')+'</span><span>'+lesson.title+'</span>';btn.addEventListener('click',()=>select(i));$('chapters').append(btn);
});
function select(i,hash=true){
  index=i;const l=lessons[i];
  for(const key of ['title','tag','formula','types','intuition','observe','trap','question','answer'])$(key).textContent=l[key];
  $('section').textContent=l.group;$('step').textContent=String(i+1).padStart(2,'0')+' / '+lessons.length;
  $('position').textContent='Lesson '+(i+1)+' of '+lessons.length;
  $('proof').replaceChildren(...l.proof.map(text=>{const li=document.createElement('li');li.textContent=text;return li;}));
  document.querySelectorAll('nav button').forEach((btn,j)=>{btn.classList.toggle('active',j===i);btn.setAttribute('aria-current',j===i?'page':'false');});
  document.querySelectorAll('main details').forEach(d=>d.open=false);
  $('previous').disabled=i===0;$('next').disabled=i===lessons.length-1;
  model=l.build(1,0.7);reset();
  if(hash)history.replaceState(null,'','#'+l.id);
}
function buildTerms(){
  $('terms').hidden=model.rhs.length===1;
  $('term-options').replaceChildren(...model.rhs.map((term,i)=>{
    const label=document.createElement('label'),input=document.createElement('input');
    input.type='checkbox';input.checked=enabled[i];input.addEventListener('change',()=>{enabled[i]=input.checked;draw();});
    label.append(input,document.createTextNode(' '+term.label));return label;
  }));
}
function colour(v,max){
  const t=Math.min(1,Math.abs(v)/(max||1)),base=v>=0?[205,119,46]:[44,119,159];
  return 'rgb('+base.map(c=>Math.round(248+(c-248)*t)).join(',')+')';
}
function arrow(ctx,x,y,u,v){
  const length=Math.hypot(u,v);if(length<1e-7)return;
  const desired=.18*length,capped=desired>.28,scale=Math.min(desired,.28)/length;
  const x1=sx(x),y1=sy(y),x2=sx(x+u*scale),y2=sy(y+v*scale),angle=Math.atan2(y2-y1,x2-x1);
  ctx.strokeStyle='#256d58';ctx.fillStyle='#256d58';ctx.lineWidth=1.65;
  ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();
  ctx.beginPath();ctx.moveTo(x2,y2);ctx.lineTo(x2-5*Math.cos(angle-.5),y2-5*Math.sin(angle-.5));ctx.lineTo(x2-5*Math.cos(angle+.5),y2-5*Math.sin(angle+.5));ctx.closePath();ctx.fill();
  if(capped){ctx.strokeStyle='#a7b6ae';ctx.lineWidth=1;ctx.beginPath();ctx.arc(x1,y1,3,0,2*Math.PI);ctx.stroke();}
}
function symbol(ctx,x,y,value){
  if(Math.abs(value)<1e-7)return;
  const size=3+Math.min(7,Math.sqrt(Math.abs(value))*3),X=sx(x),Y=sy(y);
  ctx.strokeStyle=value>0?'#2973a4':'#be7734';ctx.fillStyle=ctx.strokeStyle;ctx.lineWidth=1.4;ctx.beginPath();ctx.arc(X,Y,size,0,2*Math.PI);ctx.stroke();
  if(value>0){ctx.beginPath();ctx.arc(X,Y,1.6,0,2*Math.PI);ctx.fill();}
  else{ctx.beginPath();ctx.moveTo(X-size*.5,Y-size*.5);ctx.lineTo(X+size*.5,Y+size*.5);ctx.moveTo(X-size*.5,Y+size*.5);ctx.lineTo(X+size*.5,Y-size*.5);ctx.stroke();}
}
function contours(ctx,f){
  const n=36,grid=[];let lo=Infinity,hi=-Infinity;
  for(let i=0;i<=n;i++){grid[i]=[];for(let j=0;j<=n;j++){const v=safe(f,[-extent+i*4/n,-extent+j*4/n,probe[2]]);grid[i][j]=v;if(v!==null){lo=Math.min(lo,v);hi=Math.max(hi,v);}}}
  if(hi-lo<1e-7)return;
  ctx.strokeStyle='#7f96814d';ctx.lineWidth=1;
  for(let level=1;level<10;level++){
    const c=lo+(hi-lo)*level/10;ctx.beginPath();
    for(let i=0;i<n;i++)for(let j=0;j<n;j++){
      const corners=[[i,j],[i+1,j],[i+1,j+1],[i,j+1]],hits=[];
      for(let e=0;e<4;e++){const A=corners[e],B=corners[(e+1)%4],va=grid[A[0]][A[1]],vb=grid[B[0]][B[1]];
        if(va===null||vb===null||va===vb||!((va<=c&&vb>c)||(vb<=c&&va>c)))continue;
        const t=(c-va)/(vb-va);hits.push([sx(-2+(A[0]+t*(B[0]-A[0]))*4/n),sy(-2+(A[1]+t*(B[1]-A[1]))*4/n)]);
      }
      for(let k=0;k+1<hits.length;k+=2){ctx.moveTo(...hits[k]);ctx.lineTo(...hits[k+1]);}
    }ctx.stroke();
  }
}
function panel(canvas,fn,type,background,key,overlayGradient=false){
  const ctx=canvas.getContext('2d');ctx.clearRect(0,0,W,H);ctx.fillStyle='#f9faf6';ctx.fillRect(0,0,W,H);
  const scalarFn=type==='scalar'?fn:background;let maximum=0;
  if(scalarFn){
    const n=36,cells=[];
    for(let i=0;i<n;i++)for(let j=0;j<n;j++){const x=-2+(i+.5)*4/n,y=-2+(j+.5)*4/n,v=safe(scalarFn,[x,y,probe[2]]);cells.push([i,j,v]);if(v!==null)maximum=Math.max(maximum,Math.abs(v));}
    if(maximum<1e-7)maximum=0;
    for(const [i,j,v] of cells){ctx.fillStyle=v===null?'#dce0d8':colour(v,maximum);ctx.fillRect(sx(-2+i*4/n),sy(-2+(j+1)*4/n),(W-2*pad)/n+.5,(H-2*pad)/n+.5);}
    if($('contours').checked&&background)contours(ctx,background);
  }
  ctx.strokeStyle='#b5c3b544';ctx.lineWidth=1;ctx.beginPath();
  for(let t=-2;t<=2;t+=.5){ctx.moveTo(sx(t),sy(-2));ctx.lineTo(sx(t),sy(2));ctx.moveTo(sx(-2),sy(t));ctx.lineTo(sx(2),sy(t));}ctx.stroke();
  ctx.strokeStyle='#79918b66';ctx.beginPath();ctx.moveTo(sx(0),sy(-2));ctx.lineTo(sx(0),sy(2));ctx.moveTo(sx(-2),sy(0));ctx.lineTo(sx(2),sy(0));ctx.stroke();
  ctx.font='11px Segoe UI';ctx.fillStyle='#658076';ctx.fillText('x',W-22,sy(0)-5);ctx.fillText('y',sx(0)+8,20);
  for(let t=-2;t<=2;t++){ctx.fillText(String(t),sx(t)-4,H-14);ctx.fillText(String(t),10,sy(t)+4);}
  if($('arrows').checked&&(type==='vector'||overlayGradient)){
    for(let x=-1.8;x<=1.81;x+=.3)for(let y=-1.8;y<=1.81;y+=.3){const p=[x,y,probe[2]],v=safe(type==='vector'?fn:q=>VC.grad(fn,q),p);if(v===null)continue;arrow(ctx,x,y,v[0],v[1]);symbol(ctx,x,y,v[2]);}
  }
  if(model.singular){ctx.fillStyle='#e3e4dd';ctx.strokeStyle='#a0a59a';ctx.beginPath();ctx.ellipse(sx(0),sy(0),.22*(W-2*pad)/4,.22*(H-2*pad)/4,0,0,2*Math.PI);ctx.fill();ctx.stroke();ctx.fillStyle='#7e877c';ctx.fillText('hole',sx(0)-11,sy(0)+4);}
  if(model.probe){
    ctx.strokeStyle='#c48b34';ctx.lineWidth=2;ctx.setLineDash([]);
    const R=Number(r.value);
    if(model.probe==='vortex'){ctx.beginPath();ctx.ellipse(sx(0),sy(0),R*(W-2*pad)/4,R*(H-2*pad)/4,0,0,2*Math.PI);ctx.stroke();}
    else{
      ctx.strokeRect(sx(probe[0]-R),sy(probe[1]+R),2*R*(W-2*pad)/4,2*R*(H-2*pad)/4);
      // Show outward normals for flux, CCW tangents for circulation.
      const outward=model.probe==='flux';
      const sides=[[probe[0],probe[1]-R,outward?0:1,outward?-1:0],[probe[0]+R,probe[1],outward?1:0,outward?0:1],[probe[0],probe[1]+R,outward?0:-1,outward?1:0],[probe[0]-R,probe[1],outward?-1:0,outward?0:-1]];
      for(const [x,y,u,v] of sides){ctx.strokeStyle='#c48b34';const X=sx(x),Y=sy(y),dx=u*12,dy=-v*12;ctx.beginPath();ctx.moveTo(X,Y);ctx.lineTo(X+dx,Y+dy);ctx.stroke();const angle=Math.atan2(dy,dx);ctx.beginPath();ctx.moveTo(X+dx,Y+dy);ctx.lineTo(X+dx-5*Math.cos(angle-.5),Y+dy-5*Math.sin(angle-.5));ctx.moveTo(X+dx,Y+dy);ctx.lineTo(X+dx-5*Math.cos(angle+.5),Y+dy-5*Math.sin(angle+.5));ctx.stroke();}
    }
  }
  ctx.strokeStyle='#19332e';ctx.fillStyle='white';ctx.lineWidth=2;ctx.beginPath();ctx.arc(sx(probe[0]),sy(probe[1]),5,0,2*Math.PI);ctx.fill();ctx.stroke();
  $(key).textContent=scalarFn?(maximum===0?'Colour: zero everywhere in this slice':'Colour: −'+fmt(maximum)+' (blue) → 0 (ivory) → +'+fmt(maximum)+' (orange)')+' · '+(type==='vector'?'green arrows: x–y; ⊙/⊗: z':'scalar value'):'Green arrows: x–y · Blue ⊙: +z · Orange ⊗: −z';
}
function draw(){
  const A=Number(a.value),B=Number(b.value);probe[2]=Number(z.value);model=lessons[index].build(A,B);
  for(const el of [a,b,z,r])$(el.id+'-value').textContent=Number(el.value).toFixed(2);
  a.disabled=model.singular;
  $('example').textContent=model.example;$('r-control').hidden=!model.probe;
  const lhs=safe(model.lhs,probe),all=model.rhs.map(t=>safe(t.fn,probe));
  const invalid=lhs===null||all.some(v=>v===null),full=invalid?null:sum(all);
  const outputType=invalid?'vector':typeof lhs==='number'?'scalar':'vector';
  const selected=p=>{
    const values=model.rhs.filter((_,i)=>enabled[i]).map(t=>t.fn(p));
    return values.length?sum(values):(outputType==='scalar'?0:[0,0,0]);
  };
  const displayed=safe(selected,probe);
  const source=$('view').value==='source',leftFn=source?model.source:model.lhs,leftType=source?model.sourceType:outputType;
  $('left-title').textContent=source?'Field being differentiated':'Left-hand side result';$('left-type').textContent=leftType;
  $('right-type').textContent=outputType;$('right-title').textContent=enabled.every(Boolean)?'Right-hand side sum':'Selected contributions (partial sum)';
  panel($('left'),leftFn,leftType,model.background,'left-key',source&&leftType==='scalar');
  panel($('right'),selected,outputType,outputType==='vector'?model.background:null,'right-key');
  $('point').textContent=fmt(probe);$('lhs').textContent=lhs===null?'Excluded / undefined':fmt(lhs);
  $('rhs').textContent=displayed===null?'Excluded / undefined':fmt(displayed);
  const error=invalid?null:norm(minus(lhs,full));
  $('residual').textContent=invalid?'Excluded / undefined':error<1e-8?'≈ 0':error.toExponential(2);
  if(model.probe==='vortex'){
    $('integrals').innerHTML='<strong>Circle around the origin:</strong> radius '+fmt(Number(r.value))+' · circulation = 2πb = '+fmt(2*Math.PI*B)+'. The curl integral over a disk is not permitted: the field is undefined at its centre.';
  }else if(model.probe){
    const R=Number(r.value),kind=model.probe,boundary=VC.boundary(model.F,probe,R,kind),density=kind==='flux'?p=>VC.div(model.F,p):p=>VC.curl(model.F,p)[2],interior=VC.area(density,probe,R);
    $('integrals').innerHTML='<strong>'+ (kind==='flux'?'Outward boundary flux':'Counterclockwise boundary circulation')+':</strong> '+fmt(boundary)+' &nbsp; = &nbsp; <strong>Area integral of '+(kind==='flux'?'div F':'(curl F)z')+':</strong> '+fmt(interior)+'<br>Area = '+fmt(4*R*R)+' · boundary integral / area = '+fmt(boundary/(4*R*R))+'. Integrals use midpoint quadrature; this linear example is exact up to roundoff.';
  }else $('integrals').replaceChildren();
}
for(const input of [a,b,z,r])input.addEventListener('input',draw);
for(const id of ['arrows','contours','view'])$(id).addEventListener('change',draw);
$('reset').addEventListener('click',reset);
$('previous').addEventListener('click',()=>select(Math.max(0,index-1)));
$('next').addEventListener('click',()=>select(Math.min(lessons.length-1,index+1)));
for(const id of ['left','right']){
  const canvas=$(id);
  canvas.addEventListener('click',event=>{
    const rect=canvas.getBoundingClientRect(),X=(event.clientX-rect.left)*W/rect.width,Y=(event.clientY-rect.top)*H/rect.height;
    probe[0]=Math.max(-1.8,Math.min(1.8,(X-pad)/(W-2*pad)*4-2));probe[1]=Math.max(-1.8,Math.min(1.8,(H-pad-Y)/(H-2*pad)*4-2));draw();
  });
  canvas.addEventListener('keydown',event=>{
    const directions={ArrowLeft:[-.1,0],ArrowRight:[.1,0],ArrowUp:[0,.1],ArrowDown:[0,-.1]},delta=directions[event.key];
    if(delta){event.preventDefault();probe[0]=Math.max(-1.8,Math.min(1.8,probe[0]+delta[0]));probe[1]=Math.max(-1.8,Math.min(1.8,probe[1]+delta[1]));draw();}
  });
}
window.addEventListener('hashchange',()=>{const i=lessons.findIndex(l=>l.id===location.hash.slice(1));if(i>=0)select(i,false);});
const initial=lessons.findIndex(l=>l.id===location.hash.slice(1));select(initial<0?0:initial,false);
