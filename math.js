/* Numerical operators on smooth Cartesian fields. No dependencies. */
(function(root){
  'use strict';
  const h=0.0002;
  const add=(a,b)=>a.map((v,i)=>v+b[i]);
  const sub=(a,b)=>a.map((v,i)=>v-b[i]);
  const scale=(a,s)=>a.map(v=>s*v);
  const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
  const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
  const shift=(p,i,d)=>p.map((v,j)=>v+(j===i?d:0));
  const d=(f,p,i)=> (f(shift(p,i,h))-f(shift(p,i,-h)))/(2*h);
  const grad=(f,p)=>[0,1,2].map(i=>d(f,p,i));
  const div=(F,p)=>[0,1,2].reduce((s,i)=>s+d(q=>F(q)[i],p,i),0);
  const curl=(F,p)=>[d(q=>F(q)[2],p,1)-d(q=>F(q)[1],p,2),d(q=>F(q)[0],p,2)-d(q=>F(q)[2],p,0),d(q=>F(q)[1],p,0)-d(q=>F(q)[0],p,1)];
  const lap=(f,p)=>[0,1,2].reduce((s,i)=>s+(f(shift(p,i,h))-2*f(p)+f(shift(p,i,-h)))/(h*h),0);
  const vlap=(F,p)=>[0,1,2].map(i=>lap(q=>F(q)[i],p));
  const directional=(A,F,p)=>[0,1,2].map(i=>dot(A(p),grad(q=>F(q)[i],p)));
  // Counterclockwise square: outward normals and tangent directions.
  function boundary(F,p,r,kind,n=240){
    let total=0;
    for(let j=0;j<n;j++){
      const t=-r+(j+0.5)*2*r/n;
      const sides=[[[p[0]+t,p[1]-r,p[2]],[0,-1,0],[1,0,0]],[[p[0]+r,p[1]+t,p[2]],[1,0,0],[0,1,0]],[[p[0]-t,p[1]+r,p[2]],[0,1,0],[-1,0,0]],[[p[0]-r,p[1]-t,p[2]],[-1,0,0],[0,-1,0]]];
      for(const [q,normal,tangent] of sides) total+=dot(F(q),kind==='flux'?normal:tangent)*2*r/n;
    }
    return total;
  }
  function area(f,p,r,n=32){
    let total=0;
    for(let i=0;i<n;i++)for(let j=0;j<n;j++)total+=f([p[0]-r+(i+0.5)*2*r/n,p[1]-r+(j+0.5)*2*r/n,p[2]])*(2*r/n)**2;
    return total;
  }
  const api={add,sub,scale,dot,cross,d,grad,div,curl,lap,vlap,directional,boundary,area};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;
  else root.VC=api;
})(typeof window==='undefined'?globalThis:window);
