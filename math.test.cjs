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
