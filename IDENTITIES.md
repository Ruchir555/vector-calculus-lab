# Vector calculus identity and proof catalogue

[Download the typeset PDF](docs/vector-calculus-atlas.pdf). These 57 standard statements use oriented Cartesian coordinates in Euclidean 3D. Repeated indices are summed. First-order rules require C¹, second-order rules C², and third-order commutations C³. Integral and domain assumptions appear in the proofs. This is a comprehensive standard repertoire, not every possible derived identity.

## 1. Delta as the identity tensor

$$
\delta_{ij}a_j=a_i,\qquad\delta_{ij}\delta_{jk}=\delta_{ik},\qquad\delta_{ii}=3.
$$

**Index proof.** By definition $\delta_{ij}=1$ when $i=j$, otherwise zero. The sum selects the matching component. The matrix product selects $j=i=k$. The trace counts the three coordinates.

## 2. Epsilon contraction

$$
\varepsilon_{ijk}\varepsilon_{i\ell m}=\delta_{j\ell}\delta_{km}-\delta_{jm}\delta_{k\ell}.
$$

**Index proof.** If $j=k$ or $\ell=m$, both sides vanish. Otherwise the left side can be nonzero only when the ordered pairs $(j,k)$ and $(\ell,m)$ contain the same two distinct indices. Its value is $+1$ for the same order and $-1$ for the reversed order, exactly the right side. In particular $\varepsilon_{ijk}\varepsilon_{ij\ell}=2\delta_{k\ell}$ and $\varepsilon_{ijk}\varepsilon_{ijk}=6$.
**Picture / use.** This is the reusable engine for double curls and cross-product identities.

## 3. Cross-product antisymmetry and orthogonality

$$
\mathbf{A}\times\mathbf{B}=-\mathbf{B}\times\mathbf{A},\quad \mathbf{A}\cdot(\mathbf{A}\times\mathbf{B})=0,\quad\mathbf{A}\times\mathbf{A}=0.
$$

**Index proof.** $\varepsilon_{ijk}A_jB_k=-\varepsilon_{ikj}A_jB_k=-\varepsilon_{ijk}B_jA_k$. Also $\varepsilon_{ijk}A_iA_jB_k=0$ because $A_iA_j$ is symmetric in $i,j$ while $\varepsilon$ is antisymmetric. The same argument sets $\varepsilon_{ijk}A_jA_k=0$.

## 4. Scalar triple product

$$
\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=\mathbf{B}\cdot(\mathbf{C}\times\mathbf{A})=\mathbf{C}\cdot(\mathbf{A}\times\mathbf{B}).
$$

**Index proof.** The first expression is $\varepsilon_{ijk}A_iB_jC_k$. Cyclic relabelling $(i,j,k)\mapsto(j,k,i)$ preserves $\varepsilon$, giving the other expressions. Interchanging any two vectors changes the sign.
**Picture / use.** The signed volume of a parallelepiped is unchanged by cyclic relabelling.

## 5. Vector triple product (BAC-CAB)

$$
\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=\mathbf{B}(\mathbf{A}\cdot\mathbf{C})-\mathbf{C}(\mathbf{A}\cdot\mathbf{B}).
$$

**Index proof.** $[\mathbf{A}\times(\mathbf{B}\times\mathbf{C})]_i=\varepsilon_{ijk}\varepsilon_{k\ell m}A_jB_\ell C_m=(\delta_{i\ell}\delta_{jm}-\delta_{im}\delta_{j\ell})A_jB_\ell C_m$. Contract to get $B_iA_jC_j-C_iA_jB_j$. Antisymmetry also gives $(\mathbf{A}\times\mathbf{B})\times\mathbf{C}=\mathbf{B}(\mathbf{A}\cdot\mathbf{C})-\mathbf{A}(\mathbf{B}\cdot\mathbf{C})$.
**Picture / use.** Cross products are not associative. Parentheses matter.

## 6. Lagrange identity and cross-product magnitude

$$
(\mathbf{A}\times\mathbf{B})\cdot(\mathbf{C}\times\mathbf D)=(\mathbf{A}\cdot\mathbf{C})(\mathbf{B}\cdot\mathbf D)-(\mathbf{A}\cdot\mathbf D)(\mathbf{B}\cdot\mathbf{C}).
$$

**Index proof.** Contract $\varepsilon_{ijk}\varepsilon_{i\ell m}A_jB_kC_\ell D_m$ using identity 2. Setting $\mathbf{C}=\mathbf{A}$, $\mathbf D=\mathbf{B}$ yields $|\mathbf{A}\times\mathbf{B}|^2=|\mathbf{A}|^2|\mathbf{B}|^2-(\mathbf{A}\cdot\mathbf{B})^2$.

## 7. Dyad action and transpose

$$
(\mathbf{A}\otimes\mathbf{B})\mathbf{C}=\mathbf{A}(\mathbf{B}\cdot\mathbf{C}),\quad (\mathbf{A}\otimes\mathbf{B})^T=\mathbf{B}\otimes\mathbf{A}.
$$

**Index proof.** $A_iB_jC_j$ is $A_i$ times the scalar $B_jC_j$. Transposition exchanges $i,j$, producing $B_iA_j$. The trace is $A_iB_i=\mathbf{A}\cdot\mathbf{B}$.

## 8. Linearity

$$
D(af+bg)=aDf+bDg,\qquad D(a\mathbf{A}+b\mathbf{B})=aD\mathbf{A}+bD\mathbf{B}.
$$

**Index proof.** Here $D$ is any type-compatible operator among gradient, divergence, curl and Laplacian, and $a,b$ are constants. Each component is a linear combination of partial derivatives. For example $\varepsilon_{ijk}\partial_j(aA_k+bB_k)=a\varepsilon_{ijk}\partial_jA_k+b\varepsilon_{ijk}\partial_jB_k$.

## 9. Gradient of a scalar product

$$
\nabla(fg)=f\nabla g+g\nabla f.
$$

**Index proof.** $\partial_i(fg)=f\partial_i g+g\partial_i f$ for each free index $i$.
**Picture / use.** Both factors can change as you move.

## 10. Divergence of a scaled vector

$$
\nabla\cdot(f\mathbf{A})=f\nabla\cdot\mathbf{A}+\nabla f\cdot\mathbf{A}.
$$

**Index proof.** $\partial_i(fA_i)=f\partial_iA_i+(\partial_i f)A_i$.
**Picture / use.** A changing weight can create sources even when $\nabla\cdot\mathbf{A}=0$.

## 11. Curl of a scaled vector

$$
\nabla\times(f\mathbf{A})=f\nabla\times\mathbf{A}+\nabla f\times\mathbf{A}.
$$

**Index proof.** $\varepsilon_{ijk}\partial_j(fA_k)=f\varepsilon_{ijk}\partial_jA_k+\varepsilon_{ijk}(\partial_jf)A_k$.
**Picture / use.** Keep the order $\nabla f\times\mathbf{A}$.

## 12. Scalar quotient gradient

$$
\nabla(f/g)=\frac{g\nabla f-f\nabla g}{g^2}.
$$

**Index proof.** $\partial_i(fg^{-1})=g^{-1}\partial_i f-fg^{-2}\partial_i g$, on a region where $g\ne0$.

## 13. Vector quotient divergence and curl

$$
\begin{aligned}\nabla\cdot(\mathbf{A}/f)&=\frac{\nabla\cdot\mathbf{A}}{f}-\frac{\nabla f\cdot\mathbf{A}}{f^2},\\ \nabla\times(\mathbf{A}/f)&=\frac{\nabla\times\mathbf{A}}{f}-\frac{\nabla f\times\mathbf{A}}{f^2}.\end{aligned}
$$

**Index proof.** For $f\ne0$, expand $\partial_i(f^{-1}A_i)$ and $\varepsilon_{ijk}\partial_j(f^{-1}A_k)$ respectively. Use $\partial_j f^{-1}=-f^{-2}\partial_jf$.

## 14. Scalar chain rule

$$
\nabla h(f)=h^{\prime}(f)\nabla f.
$$

**Index proof.** $\partial_i h(f)=h^{\prime}(f)\partial_i f$. More generally $\partial_i h(f,g)=h_f\partial_i f+h_g\partial_i g$.

## 15. Directional product rules

$$
\begin{aligned}(\mathbf{A}\cdot\nabla)(fg)&=f(\mathbf{A}\cdot\nabla)g+g(\mathbf{A}\cdot\nabla)f,\\ (\mathbf{A}\cdot\nabla)(f\mathbf{B})&=f(\mathbf{A}\cdot\nabla)\mathbf{B}+[(\mathbf{A}\cdot\nabla)f]\mathbf{B}.\end{aligned}
$$

**Index proof.** Multiply $\partial_j(fg)$ or $\partial_j(fB_i)$ by $A_j$, then apply the ordinary product rule. The operator acts on what follows its parentheses.

## 16. Divergence of a cross product

$$
\nabla\cdot(\mathbf{A}\times\mathbf{B})=\mathbf{B}\cdot\nabla\times\mathbf{A}-\mathbf{A}\cdot\nabla\times\mathbf{B}.
$$

**Index proof.** $\partial_i(\varepsilon_{ijk}A_jB_k)=\varepsilon_{ijk}(\partial_iA_j)B_k+\varepsilon_{ijk}A_j\partial_iB_k$. In the first term $\varepsilon_{ijk}=\varepsilon_{kij}$; in the second $\varepsilon_{ijk}=-\varepsilon_{jik}$. Thus the terms are $B_k(\nabla\times\mathbf{A})_k-A_j(\nabla\times\mathbf{B})_j$.

## 17. Curl of a cross product

$$
\begin{aligned}\nabla\times(\mathbf{A}\times\mathbf{B})={}&\mathbf{A}\,\nabla\cdot\mathbf{B}-\mathbf{B}\,\nabla\cdot\mathbf{A}\\ &+(\mathbf{B}\cdot\nabla)\mathbf{A}-(\mathbf{A}\cdot\nabla)\mathbf{B}.\end{aligned}
$$

**Index proof.** $\varepsilon_{ijk}\partial_j(\varepsilon_{k\ell m}A_\ell B_m)=\partial_j(A_iB_j-A_jB_i)$. Expand the two products: $A_i\partial_jB_j-B_i\partial_jA_j+B_j\partial_jA_i-A_j\partial_jB_i$.

## 18. Gradient of a dot product

$$
\begin{aligned}\nabla(\mathbf{A}\cdot\mathbf{B})={}&(\mathbf{A}\cdot\nabla)\mathbf{B}+(\mathbf{B}\cdot\nabla)\mathbf{A}\\ &+\mathbf{A}\times\nabla\times\mathbf{B}+\mathbf{B}\times\nabla\times\mathbf{A}.\end{aligned}
$$

**Index proof.** $[\mathbf{A}\times\nabla\times\mathbf{B}]_i=A_j\partial_iB_j-A_j\partial_jB_i$ by contracting two epsilons. Similarly $[\mathbf{B}\times\nabla\times\mathbf{A}]_i=B_j\partial_iA_j-B_j\partial_jA_i$. Adding the two directional derivatives cancels the negative terms, leaving $\partial_i(A_jB_j)$.

## 19. Convective acceleration identity

$$
(\mathbf{A}\cdot\nabla)\mathbf{A}=\nabla\!\left(\frac{|\mathbf{A}|^2}{2}\right)-\mathbf{A}\times\nabla\times\mathbf{A}.
$$

**Index proof.** Set $\mathbf{B}=\mathbf{A}$ in the previous identity and divide by two. Directly, $\partial_i(A_jA_j/2)=A_j\partial_iA_j$, while $[\mathbf{A}\times\nabla\times\mathbf{A}]_i=A_j\partial_iA_j-A_j\partial_jA_i$.
**Picture / use.** A steady curved flow can accelerate even if its speed is constant.

## 20. Divergence of a dyadic field

$$
\nabla\cdot(\mathbf{A}\otimes\mathbf{B})=(\mathbf{B}\cdot\nabla)\mathbf{A}+\mathbf{A}\,\nabla\cdot\mathbf{B}.
$$

**Index proof.** With our stated convention, $\partial_j(A_iB_j)=B_j\partial_jA_i+A_i\partial_jB_j$. Consequently $\nabla\cdot(\mathbf v\otimes\mathbf v)=(\mathbf v\cdot\nabla)\mathbf v+\mathbf v\,\nabla\cdot\mathbf v$.
**Picture / use.** This connects momentum flux to advective acceleration. Tensor-divergence conventions must be stated.

## 21. Curl of a gradient cross gradient

$$
\begin{aligned}\nabla\times(\nabla f\times\nabla g)={}&\nabla f\,\nabla^2 g-\nabla g\,\nabla^2 f\\ &+(\nabla g\cdot\nabla)\nabla f-(\nabla f\cdot\nabla)\nabla g.\end{aligned}
$$

**Index proof.** Apply identity 17 to $A_i=\partial_i f$, $B_i=\partial_i g$; alternatively expand $\partial_j((\partial_i f)(\partial_j g)-(\partial_j f)(\partial_i g))$.

## 22. Divergence of a gradient

$$
\nabla\cdot\nabla f=\nabla^2 f.
$$

**Index proof.** $\partial_i(\partial_i f)=\partial_1^2 f+\partial_2^2 f+\partial_3^2 f$. This is the definition of the Cartesian scalar Laplacian.
**Picture / use.** Sum the curvatures; a saddle can have zero sum without being flat.

## 23. Curl of a gradient

$$
\nabla\times\nabla f=\mathbf0.
$$

**Index proof.** $\varepsilon_{ijk}\partial_j\partial_k f=0$: the $C^2$ Hessian is symmetric in $j,k$, while $\varepsilon$ is antisymmetric. Pair each term with the same term after swapping $j,k$.
**Picture / use.** A globally defined smooth height function gives zero circulation around every closed path.

## 24. Divergence of a curl

$$
\nabla\cdot\nabla\times\mathbf{A}=0.
$$

**Index proof.** $\partial_i\varepsilon_{ijk}\partial_jA_k=\varepsilon_{ijk}\partial_i\partial_jA_k=0$ by symmetry of the $i,j$ derivatives and antisymmetry of $\varepsilon$. The Cartesian epsilon is constant.

## 25. Double curl

$$
\nabla\times\nabla\times\mathbf{A}=\nabla(\nabla\cdot\mathbf{A})-\nabla^2\mathbf{A}.
$$

**Index proof.** $\varepsilon_{ijk}\varepsilon_{k\ell m}\partial_j\partial_\ell A_m=(\delta_{i\ell}\delta_{jm}-\delta_{im}\delta_{j\ell})\partial_j\partial_\ell A_m=\partial_i\partial_j A_j-\partial_j\partial_j A_i$.
**Picture / use.** Divergence-free does not mean double curl is zero; it means double curl equals $-\nabla^2\mathbf{A}$.

## 26. Laplacian of a scalar product

$$
\nabla^2(fg)=f\nabla^2 g+g\nabla^2 f+2\nabla f\cdot\nabla g.
$$

**Index proof.** $\partial_i\partial_i(fg)=\partial_i[f\partial_i g+g\partial_i f]$. Expanding gives $f\partial_i^2g+g\partial_i^2f+2(\partial_i f)(\partial_i g)$.

## 27. Laplacian of a scaled vector

$$
\nabla^2(f\mathbf{A})=f\nabla^2\mathbf{A}+\mathbf{A}\nabla^2 f+2(\nabla f\cdot\nabla)\mathbf{A}.
$$

**Index proof.** For each free index $i$, apply the previous scalar product rule to $fA_i$: $\partial_j\partial_j(fA_i)=f\partial_j\partial_jA_i+A_i\partial_j\partial_jf+2(\partial_j f)(\partial_j A_i)$.

## 28. Laplacian chain rule

$$
\nabla^2 h(f)=h^{\prime}(f)\nabla^2 f+h^{\prime\prime}(f)|\nabla f|^2.
$$

**Index proof.** $\partial_i\partial_i h(f)=\partial_i[h^{\prime}(f)\partial_i f]=h^{\prime}(f)\partial_i^2 f+h^{\prime\prime}(f)(\partial_i f)^2$. Sum over $i$.

## 29. Laplacian of a dot product

$$
\nabla^2(\mathbf{A}\cdot\mathbf{B})=(\nabla^2\mathbf{A})\cdot\mathbf{B}+\mathbf{A}\cdot\nabla^2\mathbf{B}+2(\partial_j A_i)(\partial_j B_i).
$$

**Index proof.** Expand $\partial_j\partial_j(A_iB_i)$ twice with the product rule. The last term sums both $i,j$; it is twice the Frobenius inner product of the two Jacobians, not generally $2(\nabla\cdot\mathbf{A})(\nabla\cdot\mathbf{B})$.

## 30. Laplacian of a cross product

$$
\nabla^2(\mathbf{A}\times\mathbf{B})=(\nabla^2\mathbf{A})\times\mathbf{B}+\mathbf{A}\times\nabla^2\mathbf{B}+2\sum_j(\partial_j\mathbf{A})\times(\partial_j\mathbf{B}).
$$

**Index proof.** Apply $\partial_\ell\partial_\ell$ to $\varepsilon_{ijk}A_jB_k$. Since epsilon is constant, the three component terms are $\varepsilon_{ijk}[(\nabla^2 A_j)B_k+A_j\nabla^2 B_k+2(\partial_\ell A_j)(\partial_\ell B_k)]$.

## 31. Laplacian commutes with gradient

$$
\nabla^2\nabla f=\nabla\nabla^2 f.
$$

**Index proof.** For $C^3$ $f$, $\partial_j\partial_j\partial_i f=\partial_i\partial_j\partial_j f$ by commuting partial derivatives. This is a Cartesian statement with constant coefficients.

## 32. Laplacian commutes with divergence and curl

$$
\nabla^2(\nabla\cdot\mathbf{A})=\nabla\cdot(\nabla^2\mathbf{A}),\qquad \nabla^2(\nabla\times\mathbf{A})=\nabla\times(\nabla^2\mathbf{A}).
$$

**Index proof.** For $C^3$ $\mathbf{A}$, move $\partial_\ell\partial_\ell$ through $\partial_i$ in $\partial_\ell\partial_\ell\partial_iA_i$, or through $\varepsilon_{ijk}\partial_j$ in $\partial_\ell\partial_\ell\varepsilon_{ijk}\partial_jA_k$.

## 33. Triple curl

$$
\nabla\times\nabla\times\nabla\times\mathbf{A}=-\nabla^2(\nabla\times\mathbf{A}).
$$

**Index proof.** Apply double curl to $\nabla\times\mathbf{A}$. Its divergence is zero, so the gradient-of-divergence term vanishes. The result follows for $C^3$ fields.

## 34. Curl of a scalar times a gradient

$$
\nabla\times(f\nabla g)=\nabla f\times\nabla g.
$$

**Index proof.** $\varepsilon_{ijk}\partial_j(f\partial_k g)=\varepsilon_{ijk}(\partial_j f)(\partial_k g)+f\varepsilon_{ijk}\partial_j\partial_k g$. The second term vanishes by Hessian symmetry.

## 35. Divergence of two crossed gradients

$$
\nabla\cdot(\nabla f\times\nabla g)=0.
$$

**Index proof.** Expand $\varepsilon_{ijk}\partial_i[(\partial_j f)(\partial_k g)]$. The term with $\partial_i\partial_j f$ vanishes by symmetry in $i,j$, and the term with $\partial_i\partial_k g$ vanishes by symmetry in $i,k$.

## 36. Curl energy and the antisymmetric Jacobian

$$
|\nabla\times\mathbf{A}|^2=(\partial_iA_j)(\partial_iA_j)-(\partial_iA_j)(\partial_jA_i).
$$

**Index proof.** Contract $\varepsilon_{kij}\varepsilon_{k\ell m}(\partial_iA_j)(\partial_\ell A_m)$ to obtain the right side. If $W=(J-J^T)/2$ then $|\nabla\times\mathbf{A}|^2=2W_{ij}W_{ij}$.
**Picture / use.** Curl records the antisymmetric part of local velocity variation; symmetric strain is different.

## 37. Position and radius derivatives

$$
\partial_i x_j=\delta_{ij},\quad \partial_i r=\frac{x_i}{r},\quad\partial_i\widehat r_j=\frac{\delta_{ij}-\widehat r_i\widehat r_j}{r}.
$$

**Index proof.** Differentiate $r^2=x_jx_j$: $2r\partial_i r=2x_i$. Apply the quotient rule to $x_j/r$ to get $\delta_{ij}/r-x_ix_j/r^3$.

## 38. Radial scalar gradient and Hessian

$$
\begin{aligned}\nabla u(r)&=u^{\prime}(r)\widehat{\mathbf r},\\ \partial_i\partial_j u(r)&=u^{\prime\prime}\widehat r_i\widehat r_j+\frac{u^{\prime}}r(\delta_{ij}-\widehat r_i\widehat r_j).\end{aligned}
$$

**Index proof.** First use $\partial_i u=u^{\prime}x_i/r$. Differentiate again and insert the unit-radius derivative from the preceding identity. The Hessian has a radial eigenvalue $u^{\prime\prime}$ and two tangential eigenvalues $u^{\prime}/r$.

## 39. Radial scalar Laplacian

$$
\nabla^2 u(r)=u^{\prime\prime}(r)+\frac{2}{r}u^{\prime}(r)=\frac1{r^2}\frac{d}{dr}\big(r^2u^{\prime}(r)\big).
$$

**Index proof.** Trace the radial Hessian: $\widehat r_i\widehat r_i=1$ and $\delta_{ii}=3$. Thus the trace is $u^{\prime\prime}+(3-1)u^{\prime}/r$. Expand the ordinary derivative to obtain the final form.

## 40. Radial divergence and curl

$$
\nabla\cdot[a(r)\widehat{\mathbf r}]=a^{\prime}+\frac{2a}{r},\quad\nabla\times[a(r)\widehat{\mathbf r}]=\mathbf0.
$$

**Index proof.** Write $F_i=a(r)x_i/r$. Then $\partial_i F_i=a^{\prime}x_ix_i/r^2+a(3/r-r^2/r^3)$. For curl, $\partial_jF_k$ is a linear combination of $\delta_{jk}$ and $x_jx_k$, both symmetric; contraction with $\varepsilon_{ijk}$ vanishes.

## 41. Power-law Laplacian and inverse-square flux

$$
\nabla^2 r^n=n(n+1)r^{n-2},\quad\nabla^2\frac1r=0\ (r>0),\quad\int_{S_R}\frac{\mathbf{x}}{r^3}\cdot\mathbf{n}\,dS=4\pi.
$$

**Index proof.** Insert $u^{\prime}=nr^{n-1}$ and $u^{\prime\prime}=n(n-1)r^{n-2}$ into the radial Laplacian. On the sphere $r=R$, $\mathbf{n}=\mathbf{x}/R$, so $x_in_i/r^3=1/R^2$. Multiply by surface area $4\pi R^2$.
**Picture / use.** Zero ordinary divergence away from a source does not mean zero flux around it.

## 42. Point-source distribution

$$
\nabla\cdot\frac{\mathbf{x}}{r^3}=4\pi\delta^{(3)}(\mathbf{x}),\qquad \nabla^2\frac1r=-4\pi\delta^{(3)}(\mathbf{x}).
$$

**Index proof.** For a compactly supported smooth test function $\psi$, distributional divergence gives $-\int (x_i/r^3)\partial_i\psi\,d^3x$. Excise a ball of radius $\eta$. Ordinary divergence is zero outside it, and the outward normal of the excised domain is $-\widehat{\mathbf r}$. Integration by parts gives $\int_{S_\eta}\psi/\eta^2\,dS\to4\pi\psi(0)$. The omitted ball contribution tends to zero because $r^{-2}$ is locally integrable in three dimensions. Since $\nabla(1/r)=-\mathbf{x}/r^3$, the Laplacian identity follows. No extra point term appears in this first derivative because the corresponding boundary term scales as $\eta$.
**Picture / use.** The delta is a source concentrated at a point, not an ordinary finite value assigned at the origin.

## 43. Gradient theorem

$$
\int_C\nabla f\cdot d\mathbf{x}=f(\mathbf{x}(b))-f(\mathbf{x}(a)).
$$

**Index proof.** For a piecewise $C^1$ parameterisation $x_i(t)$ and $C^1$ $f$, $\partial_i f(x(t))\dot x_i(t)=d f(x(t))/dt$. Integrate and apply the one-dimensional fundamental theorem on each segment; endpoint terms telescope.
**Picture / use.** For a mechanical force $\mathbf{F}=-\nabla U$, work is $U(a)-U(b)$.

## 44. Divergence theorem

$$
\int_{\partial V}F_i n_i\,dS=\int_V\partial_iF_i\,dV.
$$

**Index proof.** For a rectangular box, integrate $\partial_iF_i$ first in $x_i$. The fundamental theorem gives the value of $F_i$ on its two opposite faces with normals $+e_i,-e_i$. Sum $i$. Subdividing a general bounded region with piecewise smooth (or Lipschitz) boundary cancels all internal face fluxes. The boundary and volume Riemann sums converge to the displayed integrals for $C^1$ $\mathbf{F}$.
**Picture / use.** Only outer faces survive when neighbouring boxes are combined.

## 45. Stokes theorem

$$
\int_{\partial S}F_i\,dx_i=\int_S\varepsilon_{ijk}\partial_jF_k\,n_i\,dS.
$$

**Index proof.** On a smooth parameterised patch $x_i(u,v)$, set $a=F_ix_{i,u}$ and $b=F_ix_{i,v}$. Green's rectangle argument gives $\oint(a\,du+b\,dv)=\iint(\partial_u b-\partial_v a)\,du\,dv$. The mixed derivatives of $x_i$ cancel, leaving $(\partial_jF_i)(x_{j,u}x_{i,v}-x_{j,v}x_{i,u})$. Epsilon contraction identifies this with $(\nabla\times\mathbf{F})_k\varepsilon_{k\ell m}x_{\ell,u}x_{m,v}$. Patch boundaries cancel on an oriented piecewise smooth surface. Use $C^1$ $\mathbf{F}$ and $C^2$ patches.
**Picture / use.** The induced boundary direction follows the right-hand rule. A singular point on the surface invalidates the ordinary theorem.

## 46. Green circulation theorem

$$
\oint_{\partial D}(P\,dx+Q\,dy)=\iint_D(\partial_x Q-\partial_y P)\,dx\,dy.
$$

**Index proof.** On $[a,b]\times[c,d]$, integrate $\partial_xQ$ in $x$ and $-\partial_yP$ in $y$. These give the right-minus-left and bottom-minus-top edge contributions, exactly the counterclockwise boundary integral. Tile a bounded planar region with piecewise smooth boundary, cancel internal edges and take limits. Requires $P,Q\in C^1$ near $\overline D$.

## 47. Green flux theorem

$$
\oint_{\partial D}(P\,dy-Q\,dx)=\iint_D(\partial_xP+\partial_yQ)\,dx\,dy.
$$

**Index proof.** Apply the previous theorem to the pair $(-Q,P)$. On a positively oriented boundary, the outward normal satisfies $\mathbf{n}\,ds=(dy,-dx)$, so the boundary form equals $(P,Q)\cdot\mathbf{n}\,ds$.

## 48. Scalar-vector integration by parts

$$
\int_V f\,\nabla\cdot\mathbf{A}\,dV=\int_{\partial V}f\mathbf{A}\cdot\mathbf{n}\,dS-\int_V\nabla f\cdot\mathbf{A}\,dV.
$$

**Index proof.** Integrate $\partial_i(fA_i)=f\partial_iA_i+(\partial_i f)A_i$ and use the divergence theorem on $f\mathbf{A}$.

## 49. Green first identity

$$
\int_V(f\nabla^2 g+\nabla f\cdot\nabla g)\,dV=\int_{\partial V}f\,\partial_n g\,dS.
$$

**Index proof.** Set $A_i=\partial_i g$ in the preceding identity. Then $\partial_iA_i=\nabla^2 g$, and $A_in_i=\partial_n g$. Take $f\in C^1$, $g\in C^2$ near the region.

## 50. Green second identity

$$
\int_V(f\nabla^2 g-g\nabla^2 f)\,dV=\int_{\partial V}(f\partial_n g-g\partial_n f)\,dS.
$$

**Index proof.** Write Green's first identity for $(f,g)$ and $(g,f)$ with both $C^2$. Subtract; $(\partial_i f)(\partial_i g)$ cancels. This is reciprocity for the Laplacian.

## 51. Curl integration by parts

$$
\int_V[\mathbf{B}\cdot\nabla\times\mathbf{A}-\mathbf{A}\cdot\nabla\times\mathbf{B}]\,dV=\int_{\partial V}\mathbf{n}\cdot(\mathbf{A}\times\mathbf{B})\,dS.
$$

**Index proof.** Integrate the cross-product divergence identity $\partial_i(\varepsilon_{ijk}A_jB_k)=B_i(\nabla\times\mathbf{A})_i-A_i(\nabla\times\mathbf{B})_i$ and apply the divergence theorem. The boundary sign is fixed by $\mathbf{n}\cdot(\mathbf{A}\times\mathbf{B})$.

## 52. Vector forms of surface integration

$$
\int_V\nabla f\,dV=\int_{\partial V}f\mathbf{n}\,dS,\quad \int_V\nabla\times\mathbf{A}\,dV=\int_{\partial V}\mathbf{n}\times\mathbf{A}\,dS.
$$

**Index proof.** For the first, apply the divergence theorem componentwise to $F_j=f\delta_{ij}$ with fixed $i$. For the second use $F_j=\varepsilon_{ijk}A_k$ with fixed $i$. Their divergences are $\partial_i f$ and $\varepsilon_{ijk}\partial_jA_k$ respectively.

## 53. Green representation formula (three dimensions)

$$
\begin{aligned}f(\mathbf{x})={}&\int_{\partial V}\left[\Gamma\,\partial_n f-f\,\partial_n\Gamma\right]dS-\int_V\Gamma\,\nabla^2 f\,dV,\\ &\Gamma(\mathbf{x},\mathbf y)=\frac1{4\pi|\mathbf{x}-\mathbf y|},\quad \mathbf{x}\in V.\end{aligned}
$$

**Index proof.** Assume $f\in C^2$ near a bounded smooth region and $\mathbf{x}$ strictly inside. In the $\mathbf y$ variable, $\nabla^2_{\mathbf y}\Gamma=-\delta^{(3)}(\mathbf y-\mathbf{x})$. Apply Green's second identity with $g=\Gamma$, excising a ball about $\mathbf{x}$ and taking its radius to zero (as in identity 42). The volume term becomes $-f(\mathbf{x})-\int_V\Gamma\nabla^2 f$. Rearranging the outer boundary term $\int_{\partial V}(f\partial_n\Gamma-\Gamma\partial_n f)$ yields the formula. Boundary points require a separate limiting formula.

## 54. The planar exactness condition

$$
\mathbf{F}=(P,Q)=\nabla\phi\ \Longrightarrow\ \frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}.
$$

**Index proof.** $P=\partial_x\phi$, $Q=\partial_y\phi$. For $C^2$ $\phi$, $\partial_yP=\partial_y\partial_x\phi=\partial_x\partial_y\phi=\partial_xQ$. In tensor language the Jacobian $J_{ij}=\partial_jF_i$ is symmetric. Conversely, for $C^1$ $\mathbf{F}$ on an open simply connected planar domain, this condition is sufficient for a single-valued global potential, by the path-independence argument below.
**Picture / use.** These are partial} derivatives because $P,Q$ depend on both variables. Compare the off-diagonal derivatives, not $P_x$ and $Q_y$.

## 55. Constructing a potential on a rectangle

$$
\phi(x,y)=\int_{x_0}^x P(s,y_0)\,ds+\int_{y_0}^y Q(x,t)\,dt.
$$

**Index proof.** Assume the rectangle lies in a $C^1$ domain and $P_y=Q_x$. Clearly $\phi_y=Q(x,y)$. Also $\phi_x=P(x,y_0)+\int_{y_0}^y Q_x(x,t)\,dt=P(x,y_0)+\int_{y_0}^y P_y(x,t)\,dt=P(x,y)$. Thus the mixed-partial test is constructively sufficient locally.

## 56. Closed-loop criterion and path independence

$$
\mathbf{F}=\nabla\phi\quad\Longleftrightarrow\quad\oint_C\mathbf{F}\cdot d\mathbf{x}=0\ \text{for every closed path }C.
$$

**Index proof.** On an open connected domain with $C^1$ $\mathbf{F}$, the forward implication is the gradient theorem. For the reverse, choose a base point and define $\phi(\mathbf{x})=\int_{\mathbf{x}_0}^{\mathbf{x}}\mathbf{F}\cdot d\boldsymbol\ell$. Two paths differ by a closed path, so the value is independent of path. Appending a short coordinate segment gives $\partial_i\phi=F_i$. Curl-free fields on a simply connected domain have zero loop integral: contract each loop to a point and use Stokes on smooth homotopy patches, where the normal curl is zero. General piecewise smooth loops follow by approximation. Simple connectivity is sufficient, not necessary for a particular field.
**Picture / use.** A hole permits a failure but does not force it. All closed-loop integrals being zero is the exact global test.

## 57. Three-dimensional condition and star-shaped construction

$$
\begin{gathered}\partial_iF_j=\partial_jF_i\quad\Longleftrightarrow\quad\nabla\times\mathbf{F}=0,\\ \phi(\mathbf{x})=\int_0^1 x_iF_i(t\mathbf{x})\,dt\quad\text{on a domain star-shaped about }0.\end{gathered}
$$

**Index proof.** Epsilon contraction shows $\nabla\times\mathbf{F}=0$ is equivalent to the antisymmetric part of $\partial_iF_j$ vanishing. For $C^1$ $\mathbf{F}$, differentiate the integral: $\partial_k\phi=\int_0^1[F_k(t\mathbf{x})+t x_i\partial_kF_i(t\mathbf{x})]dt$. Symmetry turns $\partial_kF_i$ into $\partial_iF_k$, making the integrand $d[tF_k(t\mathbf{x})]/dt$. Hence $\partial_k\phi=F_k(\mathbf{x})$. Translate the base point for any other star centre. In $(P,Q,R)$ notation, the conditions are $P_y=Q_x$, $P_z=R_x$, $Q_z=R_y$.
