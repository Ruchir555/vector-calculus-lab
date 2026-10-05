const {test}=require('node:test');
const assert=require('node:assert/strict');
const M=require('./math.js');
const {lessons,sum}=require('./lessons.js');
function close(actual,expected,tol=2e-6){
  const error=typeof actual==='number'?Math.abs(actual-expected):Math.hypot(...M.sub(actual,expected));
  assert.ok(error<tol,'error '+error+' exceeds '+tol+'; actual '+actual+', expected '+expected);
}
test('operators agree with independently differentiated polynomials',()=>{
  const f=([x,y,z])=>x*x*y+3*y*y*z+z*z;
  const F=([x,y,z])=>[x*y,y*z,z*x];
  for(const p of [[.4,-.3,.7],[-.8,1.2,-.6],[0,0,0]]){
    const [x,y,z]=p;
    close(M.grad(f,p),[2*x*y,x*x+6*y*z,3*y*y+2*z]);
    close(M.lap(f,p),2*y+6*z+2);
    close(M.div(F,p),x+y+z);
    close(M.curl(F,p),[-y,-z,-x]);
  }
});
test('curl-curl is not generally zero',()=>{
  const a=1.3,b=-.8,F=([x,y])=>[a*x*y,b*x*x,0];
  close(M.curl(q=>M.curl(F,q),[.3,-.2,.9]),[0,a-2*b,0]);
});
test('3D divergence cancellation includes the z derivative',()=>{
  const a=1.4,b=.3,A=([x,y,z])=>[a*y*z,b*x*z,x*y];
  const C=p=>M.curl(A,p),p=[.3,.7,.9];
  close(C(p),[(1-b)*p[0],(a-1)*p[1],(b-a)*p[2]]);
  close(M.div(C,p),0);
  close(M.d(q=>C(q)[0],p,0)+M.d(q=>C(q)[1],p,1),a-b);
});
for(const lesson of lessons){
  test('full identity: '+lesson.id,()=>{
    for(const [a,b] of [[1,.7],[0,0],[-2,2],[2,-2],[.35,-.65]]){
      const model=lesson.build(a,b);
      for(const p of [[.45,.35,.6],[-.8,.7,-.9],[1.2,-1,.2],[0,.9,0]]){
        close(model.lhs(p),sum(model.rhs.map(t=>t.fn(p))),lesson.id==='vortex'?2e-6:4e-6);
      }
    }
  });
}
test('boundary flux and circulation match analytic area integrals',()=>{
  for(const a of [-2,0,1.4])for(const b of [-1.2,0,2]){
    const F=([x,y])=>[a*x-b*y,b*x+a*y,0];
    for(const r of [.15,.5,1]){
      const p=[.45,-.35,.7];
      close(M.boundary(F,p,r,'flux'),8*a*r*r,1e-10);
      close(M.boundary(F,p,r,'circulation'),8*b*r*r,1e-10);
      close(M.area(q=>M.div(F,q),p,r),8*a*r*r,1e-8);
      close(M.area(q=>M.curl(F,q)[2],p,r),8*b*r*r,1e-8);
    }
  }
});
test('vortex has nonzero circulation independently of radius',()=>{
  for(const radius of [.3,.7,1.5]){
    let integral=0;const b=.7,n=2000;
    for(let i=0;i<n;i++){
      const t=(i+.5)*2*Math.PI/n,p=[radius*Math.cos(t),radius*Math.sin(t),0];
      const F=lessons.find(l=>l.id==='vortex').build(1,b).source(p);
      integral+=M.dot(F,[-radius*Math.sin(t),radius*Math.cos(t),0])*2*Math.PI/n;
    }
    close(integral,2*Math.PI*b,1e-10);
  }
});
test('potential construction matches both mixed partials and path integrals',()=>{
  const model=lessons.find(l=>l.id==='conservative').build(1,1);
  const p=[.6,-.4,.8];close(M.grad(model.background,p),model.source(p));
  close(M.d(q=>model.source(q)[0],p,1),2*p[0]+2*p[1]);
  close(M.d(q=>model.source(q)[1],p,0),2*p[0]+2*p[1]);
  let diagonal=0,edge=0;const n=2000;
  for(let i=0;i<n;i++){const t=(i+.5)/n;diagonal+=M.dot(model.source([t,t,0]),[1,1,0])/n;edge+=model.source([t,0,0])[0]/n+model.source([1,t,0])[1]/n;}
  close(diagonal,3,1e-6);close(edge,3,1e-6);
});
test('failed condition gives independently computed unequal path work',()=>{
  const a=.6,b=-.7,F=lessons.find(l=>l.id==='failed-condition').build(a,b).source;
  let first=0,second=0;const n=100;
  for(let i=0;i<n;i++){const t=(i+.5)/n;first+=(F([t,0,0])[0]+F([1,t,0])[1])/n;second+=(F([0,t,0])[1]+F([t,1,0])[0])/n;}
  close(first,a+b,1e-12);close(second,a-b,1e-12);
});
test('uniform sphere matches potential, interior density, continuity and exterior flux',()=>{
  const model=lessons.find(l=>l.id==='gravity-sphere').build(1,0),mass=1.1,R=1.4;
  for(const p of [[.2,.3,.4],[2,0,.3]])close(model.source(p),M.scale(M.grad(model.background,p),-1),1e-7);
  close(M.div(model.source,[0,0,0]),-3*mass/R**3,1e-10);
  close(M.div(model.source,[2,1,.5]),0,1e-7);
  close(model.source([R-1e-9,0,0]),model.source([R+1e-9,0,0]),1e-8);
  close(model.background([R-1e-9,0,0]),model.background([R+1e-9,0,0]),1e-8);
  const radial=model.source([2,0,0])[0];close(4*Math.PI*4*radial,-4*Math.PI*mass,1e-10);
});
test('point gravity requires full 3D divergence and inward source sign',()=>{
  const model=lessons.find(l=>l.id==='gravity-point').build(1,0),p=[1,0,0];
  close(model.source(p),[-1.1,0,0]);close(M.div(model.source,p),0,5e-7);
  const planar=M.d(q=>model.source(q)[0],p,0)+M.d(q=>model.source(q)[1],p,1);
  close(planar,1.1,5e-7);close(M.d(q=>model.source(q)[2],p,2),-1.1,3e-7);
});
test('smooth electric cloud gives correct field, total-charge limit and curl',()=>{
  const model=lessons.find(l=>l.id==='electrostatics').build(-1.3,0),s=.7,p=[.5,.3,-.2];
  close(model.source(p),M.scale(M.grad(model.background,p),-1),1e-7);close(M.curl(model.source,p),[0,0,0],1e-7);
  const radius=100;const flux=4*Math.PI*radius**2*model.source([radius,0,0])[0];
  close(flux,-1.3*radius**3/(radius**2+s*s)**1.5,1e-12);close(flux,-1.3,1e-4);
});
