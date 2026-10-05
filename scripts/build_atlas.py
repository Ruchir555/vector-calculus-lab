#!/usr/bin/env python3
"""Generate the original LaTeX atlas and exact mathematical figures. Needs NumPy/Matplotlib and pdfLaTeX."""
from pathlib import Path
import subprocess
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; DOC=ROOT/'docs'; DOC.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white'})
x=np.linspace(-2,2,19); X,Y=np.meshgrid(x,x); R=np.hypot(X,Y)
fig,axs=plt.subplots(1,3,figsize=(10,3.3))
fields=[(2*X*Y+Y**2,X**2+2*X*Y+3*Y**2,'Exact: gradient of a polynomial'),(-Y,X,'Rotation: mixed partials differ'),(-Y/np.maximum(R**2,.08),X/np.maximum(R**2,.08),'Vortex: remove the origin')]
for ax,(U,V,title) in zip(axs,fields):
    norm=np.hypot(U,V); fac=np.maximum(norm,1); U,V=U/fac,V/fac
    if 'Vortex' in title: U=np.ma.masked_where(R<.3,U);V=np.ma.masked_where(R<.3,V);ax.add_patch(plt.Circle((0,0),.24,color='#dddddd'));ax.add_patch(plt.Circle((0,0),1.2,fill=False,color='#b67b27',lw=2))
    ax.quiver(X,Y,U,V,color='#236b59',angles='xy',scale_units='xy',scale=5);ax.set(xlim=(-2.1,2.1),ylim=(-2.1,2.1),aspect='equal',xlabel='x',ylabel='y',title=title)
fig.tight_layout();fig.savefig(DOC/'exactness-fields.pdf');plt.close(fig)
r=np.linspace(0,3,400); mag=np.where(r<=1,r,1/np.maximum(r,1e-8)**2);phi=np.where(r<=1,-(3-r*r)/2,-1/np.maximum(r,1e-8));rho=np.where(r<1,3/(4*np.pi),0)
fig,axs=plt.subplots(1,3,figsize=(10,3.1))
for ax,y,title,yl in zip(axs,[mag,phi,rho],['Gravity magnitude','Potential (zero at infinity)','Mass density'],['|g| / (GM/R²)','Φ / (GM/R)','ρ / (M/R³)']):
    ax.plot(r,y,color='#236b59',lw=2);ax.axvline(1,color='#b67b27',ls='--');ax.set(xlabel='radius / R',ylabel=yl,title=title);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(DOC/'gravity-sphere.pdf');plt.close(fig)

preamble=r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}\usepackage{lmodern,amsmath,amssymb,geometry,graphicx,xcolor,hyperref,booktabs,fancyhdr,microtype}
\geometry{margin=0.85in}\definecolor{forest}{HTML}{236B59}\definecolor{gold}{HTML}{A76F26}
\hypersetup{colorlinks=true,linkcolor=forest,urlcolor=forest,pdftitle={Vector Calculus: An Identity and Proof Atlas},pdfauthor={Vector Calculus Lab}}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{\small Vector Calculus Lab}\fancyhead[R]{\small Identity and proof atlas}\fancyfoot[C]{\thepage}\setlength{\headheight}{14pt}
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt}\allowdisplaybreaks\setlength{\emergencystretch}{1em}
\newcommand{\A}{\mathbf A}\newcommand{\B}{\mathbf B}\newcommand{\C}{\mathbf C}\newcommand{\F}{\mathbf F}\newcommand{\xx}{\mathbf x}\newcommand{\nn}{\mathbf n}\newcommand{\grad}{\nabla}\newcommand{\divg}{\nabla\!\cdot}\newcommand{\curl}{\nabla\!\times}\newcommand{\lap}{\nabla^2}\newcommand{\eps}{\varepsilon}
\newcounter{identity}\newcommand{\identity}[2]{\refstepcounter{identity}\subsection*{\textcolor{forest}{\theidentity. #1}}\addcontentsline{toc}{subsection}{\theidentity. #1}\[ #2 \]}
\newcommand{\proof}{\textbf{Index proof. } }\newcommand{\sense}{\textbf{Picture / use. } }
\begin{document}
\begin{titlepage}\vspace*{1cm}{\color{forest}\Huge\bfseries Vector Calculus\\[8pt] An Identity and Proof Atlas}\vspace{1cm}

{\Large From pictures to tensor algebra}

A companion to the interactive Vector Calculus Lab. A comprehensive standard catalogue of Cartesian vector algebra, differential rules, radial fields, integral theorems, and potential tests, with a component or index proof for every numbered statement.

\vspace{0.6cm}\includegraphics[width=\textwidth]{exactness-fields.pdf}

\textbf{Start with a question.} Is this field describing uphill slopes, sources, or circulation? Then track which index is free, which indices are summed, and where the derivative acts.

\vfill\href{https://ruchir555.github.io/vector-calculus-lab/}{Open the interactive guide}\quad\href{https://github.com/Ruchir555/vector-calculus-lab}{Repository and source}\\Version 2.0\quad October 2026
\end{titlepage}\tableofcontents\newpage
\section{How to read the proofs}
This is a broad standard repertoire, not a claim to enumerate every identity that can be derived. Scalar fields are $f,g$; vector fields are $\A,\B,\F$. Work in oriented, orthonormal Cartesian coordinates in Euclidean $\mathbb R^3$. Indices $i,j,k,\ell,m$ run from 1 to 3; repeated indices are summed. A \emph{free} index labels the output component and must match on both sides. Write $\partial_i=\partial/\partial x_i$.
\[
(\grad f)_i=\partial_i f,\quad \divg\A=\partial_i A_i,\quad (\curl\A)_i=\eps_{ijk}\partial_j A_k,\quad \lap f=\partial_j\partial_j f.
\]
The vector Laplacian means $(\lap\A)_i=\partial_j\partial_j A_i$. The directional derivative is $[(\A\cdot\grad)\B]_i=A_j\partial_jB_i$. It differentiates $\B$, not $\A$. Use $J_{ij}=\partial_j F_i$ for a Jacobian, $H_{ij}=\partial_i\partial_j f$ for a Hessian, and $(\A\otimes\B)_{ij}=A_iB_j$ for a dyad. Our tensor divergence is $(\divg T)_i=\partial_jT_{ij}$.

\textbf{Regularity.} First-order identities assume $C^1$ fields on an open domain; second-order identities assume $C^2$; third-order commutations assume $C^3$. Scalars in denominators must be nonzero. Constants are spatially constant. Extra assumptions for integral theorems, potentials, singularities and coordinate systems appear where needed. Mixed derivatives commute only when justified by regularity.

\textbf{Proof recipe.} (1) Write a component. (2) Expand a product or contract two $\eps$ symbols. (3) Relabel dummy indices. (4) Recognise the vector expression. Tensor algebra proves the differential rules. Integral theorems additionally need the one-dimensional fundamental theorem of calculus and geometric patching; those ingredients are made explicit.

\textbf{A sign check.} $\eps_{123}=+1$; odd permutations change sign, even ones do not, and any repeated index makes $\eps$ zero. A blue dot in the lab means $+z$; a cross means $-z$.
'''
parts=[preamble]
def section(s): parts.append('\\section{'+s+'}\n')
def entry(title,formula,proof,sense=''):
    parts.append('\\identity{'+title+'}{'+formula+'}\n\\proof '+proof+'\n'+('\\sense '+sense+'\n' if sense else ''))
section('The algebra behind every curl')
entry('Delta as the identity tensor',r'\delta_{ij}a_j=a_i,\qquad\delta_{ij}\delta_{jk}=\delta_{ik},\qquad\delta_{ii}=3.',r'By definition $\delta_{ij}=1$ when $i=j$, otherwise zero. The sum selects the matching component. The matrix product selects $j=i=k$. The trace counts the three coordinates.')
entry('Epsilon contraction',r'\eps_{ijk}\eps_{i\ell m}=\delta_{j\ell}\delta_{km}-\delta_{jm}\delta_{k\ell}.',r'If $j=k$ or $\ell=m$, both sides vanish. Otherwise the left side can be nonzero only when the ordered pairs $(j,k)$ and $(\ell,m)$ contain the same two distinct indices. Its value is $+1$ for the same order and $-1$ for the reversed order, exactly the right side. In particular $\eps_{ijk}\eps_{ij\ell}=2\delta_{k\ell}$ and $\eps_{ijk}\eps_{ijk}=6$.',r'This is the reusable engine for double curls and cross-product identities.')
entry('Cross-product antisymmetry and orthogonality',r'\A\times\B=-\B\times\A,\quad \A\cdot(\A\times\B)=0,\quad\A\times\A=0.',r'$\eps_{ijk}A_jB_k=-\eps_{ikj}A_jB_k=-\eps_{ijk}B_jA_k$. Also $\eps_{ijk}A_iA_jB_k=0$ because $A_iA_j$ is symmetric in $i,j$ while $\eps$ is antisymmetric. The same argument sets $\eps_{ijk}A_jA_k=0$.')
entry('Scalar triple product',r'\A\cdot(\B\times\C)=\B\cdot(\C\times\A)=\C\cdot(\A\times\B).',r'The first expression is $\eps_{ijk}A_iB_jC_k$. Cyclic relabelling $(i,j,k)\mapsto(j,k,i)$ preserves $\eps$, giving the other expressions. Interchanging any two vectors changes the sign.',r'The signed volume of a parallelepiped is unchanged by cyclic relabelling.')
entry('Vector triple product (BAC-CAB)',r'\A\times(\B\times\C)=\B(\A\cdot\C)-\C(\A\cdot\B).',r'$[\A\times(\B\times\C)]_i=\eps_{ijk}\eps_{k\ell m}A_jB_\ell C_m=(\delta_{i\ell}\delta_{jm}-\delta_{im}\delta_{j\ell})A_jB_\ell C_m$. Contract to get $B_iA_jC_j-C_iA_jB_j$. Antisymmetry also gives $(\A\times\B)\times\C=\B(\A\cdot\C)-\A(\B\cdot\C)$.',r'Cross products are not associative. Parentheses matter.')
entry('Lagrange identity and cross-product magnitude',r'(\A\times\B)\cdot(\C\times\mathbf D)=(\A\cdot\C)(\B\cdot\mathbf D)-(\A\cdot\mathbf D)(\B\cdot\C).',r'Contract $\eps_{ijk}\eps_{i\ell m}A_jB_kC_\ell D_m$ using identity 2. Setting $\C=\A$, $\mathbf D=\B$ yields $|\A\times\B|^2=|\A|^2|\B|^2-(\A\cdot\B)^2$.')
entry('Dyad action and transpose',r'(\A\otimes\B)\C=\A(\B\cdot\C),\quad (\A\otimes\B)^T=\B\otimes\A.',r'$A_iB_jC_j$ is $A_i$ times the scalar $B_jC_j$. Transposition exchanges $i,j$, producing $B_iA_j$. The trace is $A_iB_i=\A\cdot\B$.')
section('First derivatives: product, quotient, and chain rules')
entry('Linearity',r'D(af+bg)=aDf+bDg,\qquad D(a\A+b\B)=aD\A+bD\B.',r'Here $D$ is any type-compatible operator among gradient, divergence, curl and Laplacian, and $a,b$ are constants. Each component is a linear combination of partial derivatives. For example $\eps_{ijk}\partial_j(aA_k+bB_k)=a\eps_{ijk}\partial_jA_k+b\eps_{ijk}\partial_jB_k$.')
entry('Gradient of a scalar product',r'\grad(fg)=f\grad g+g\grad f.',r'$\partial_i(fg)=f\partial_i g+g\partial_i f$ for each free index $i$.',r'Both factors can change as you move.')
entry('Divergence of a scaled vector',r'\divg(f\A)=f\divg\A+\grad f\cdot\A.',r'$\partial_i(fA_i)=f\partial_iA_i+(\partial_i f)A_i$.',r'A changing weight can create sources even when $\divg\A=0$.')
entry('Curl of a scaled vector',r'\curl(f\A)=f\curl\A+\grad f\times\A.',r'$\eps_{ijk}\partial_j(fA_k)=f\eps_{ijk}\partial_jA_k+\eps_{ijk}(\partial_jf)A_k$.',r'Keep the order $\grad f\times\A$.')
entry('Scalar quotient gradient',r'\grad(f/g)=\frac{g\grad f-f\grad g}{g^2}.',r'$\partial_i(fg^{-1})=g^{-1}\partial_i f-fg^{-2}\partial_i g$, on a region where $g\ne0$.')
entry('Vector quotient divergence and curl',r'\begin{aligned}\divg(\A/f)&=\frac{\divg\A}{f}-\frac{\grad f\cdot\A}{f^2},\\ \curl(\A/f)&=\frac{\curl\A}{f}-\frac{\grad f\times\A}{f^2}.\end{aligned}',r'For $f\ne0$, expand $\partial_i(f^{-1}A_i)$ and $\eps_{ijk}\partial_j(f^{-1}A_k)$ respectively. Use $\partial_j f^{-1}=-f^{-2}\partial_jf$.')
entry('Scalar chain rule',r'\grad h(f)=h^{\prime}(f)\grad f.',r'$\partial_i h(f)=h^{\prime}(f)\partial_i f$. More generally $\partial_i h(f,g)=h_f\partial_i f+h_g\partial_i g$.')
entry('Directional product rules',r'\begin{aligned}(\A\cdot\grad)(fg)&=f(\A\cdot\grad)g+g(\A\cdot\grad)f,\\ (\A\cdot\grad)(f\B)&=f(\A\cdot\grad)\B+[(\A\cdot\grad)f]\B.\end{aligned}',r'Multiply $\partial_j(fg)$ or $\partial_j(fB_i)$ by $A_j$, then apply the ordinary product rule. The operator acts on what follows its parentheses.')
entry('Divergence of a cross product',r'\divg(\A\times\B)=\B\cdot\curl\A-\A\cdot\curl\B.',r'$\partial_i(\eps_{ijk}A_jB_k)=\eps_{ijk}(\partial_iA_j)B_k+\eps_{ijk}A_j\partial_iB_k$. In the first term $\eps_{ijk}=\eps_{kij}$; in the second $\eps_{ijk}=-\eps_{jik}$. Thus the terms are $B_k(\curl\A)_k-A_j(\curl\B)_j$.')
entry('Curl of a cross product',r'\begin{aligned}\curl(\A\times\B)={}&\A\,\divg\B-\B\,\divg\A\\ &+(\B\cdot\grad)\A-(\A\cdot\grad)\B.\end{aligned}',r'$\eps_{ijk}\partial_j(\eps_{k\ell m}A_\ell B_m)=\partial_j(A_iB_j-A_jB_i)$. Expand the two products: $A_i\partial_jB_j-B_i\partial_jA_j+B_j\partial_jA_i-A_j\partial_jB_i$.')
entry('Gradient of a dot product',r'\begin{aligned}\grad(\A\cdot\B)={}&(\A\cdot\grad)\B+(\B\cdot\grad)\A\\ &+\A\times\curl\B+\B\times\curl\A.\end{aligned}',r'$[\A\times\curl\B]_i=A_j\partial_iB_j-A_j\partial_jB_i$ by contracting two epsilons. Similarly $[\B\times\curl\A]_i=B_j\partial_iA_j-B_j\partial_jA_i$. Adding the two directional derivatives cancels the negative terms, leaving $\partial_i(A_jB_j)$.')
entry('Convective acceleration identity',r'(\A\cdot\grad)\A=\grad\!\left(\frac{|\A|^2}{2}\right)-\A\times\curl\A.',r'Set $\B=\A$ in the previous identity and divide by two. Directly, $\partial_i(A_jA_j/2)=A_j\partial_iA_j$, while $[\A\times\curl\A]_i=A_j\partial_iA_j-A_j\partial_jA_i$.',r'A steady curved flow can accelerate even if its speed is constant.')
entry('Divergence of a dyadic field',r'\divg(\A\otimes\B)=(\B\cdot\grad)\A+\A\,\divg\B.',r'With our stated convention, $\partial_j(A_iB_j)=B_j\partial_jA_i+A_i\partial_jB_j$. Consequently $\divg(\mathbf v\otimes\mathbf v)=(\mathbf v\cdot\grad)\mathbf v+\mathbf v\,\divg\mathbf v$.',r'This connects momentum flux to advective acceleration. Tensor-divergence conventions must be stated.')
entry('Curl of a gradient cross gradient',r'\begin{aligned}\curl(\grad f\times\grad g)={}&\grad f\,\lap g-\grad g\,\lap f\\ &+(\grad g\cdot\grad)\grad f-(\grad f\cdot\grad)\grad g.\end{aligned}',r'Apply identity 17 to $A_i=\partial_i f$, $B_i=\partial_i g$; alternatively expand $\partial_j((\partial_i f)(\partial_j g)-(\partial_j f)(\partial_i g))$.')
section('Second derivatives and cancellations')
entry('Divergence of a gradient',r'\divg\grad f=\lap f.',r'$\partial_i(\partial_i f)=\partial_1^2 f+\partial_2^2 f+\partial_3^2 f$. This is the definition of the Cartesian scalar Laplacian.',r'Sum the curvatures; a saddle can have zero sum without being flat.')
entry('Curl of a gradient',r'\curl\grad f=\mathbf0.',r'$\eps_{ijk}\partial_j\partial_k f=0$: the $C^2$ Hessian is symmetric in $j,k$, while $\eps$ is antisymmetric. Pair each term with the same term after swapping $j,k$.',r'A globally defined smooth height function gives zero circulation around every closed path.')
entry('Divergence of a curl',r'\divg\curl\A=0.',r'$\partial_i\eps_{ijk}\partial_jA_k=\eps_{ijk}\partial_i\partial_jA_k=0$ by symmetry of the $i,j$ derivatives and antisymmetry of $\eps$. The Cartesian epsilon is constant.')
entry('Double curl',r'\curl\curl\A=\grad(\divg\A)-\lap\A.',r'$\eps_{ijk}\eps_{k\ell m}\partial_j\partial_\ell A_m=(\delta_{i\ell}\delta_{jm}-\delta_{im}\delta_{j\ell})\partial_j\partial_\ell A_m=\partial_i\partial_j A_j-\partial_j\partial_j A_i$.',r'Divergence-free does not mean double curl is zero; it means double curl equals $-\lap\A$.')
entry('Laplacian of a scalar product',r'\lap(fg)=f\lap g+g\lap f+2\grad f\cdot\grad g.',r'$\partial_i\partial_i(fg)=\partial_i[f\partial_i g+g\partial_i f]$. Expanding gives $f\partial_i^2g+g\partial_i^2f+2(\partial_i f)(\partial_i g)$.')
entry('Laplacian of a scaled vector',r'\lap(f\A)=f\lap\A+\A\lap f+2(\grad f\cdot\grad)\A.',r'For each free index $i$, apply the previous scalar product rule to $fA_i$: $\partial_j\partial_j(fA_i)=f\partial_j\partial_jA_i+A_i\partial_j\partial_jf+2(\partial_j f)(\partial_j A_i)$.')
entry('Laplacian chain rule',r'\lap h(f)=h^{\prime}(f)\lap f+h^{\prime\prime}(f)|\grad f|^2.',r'$\partial_i\partial_i h(f)=\partial_i[h^{\prime}(f)\partial_i f]=h^{\prime}(f)\partial_i^2 f+h^{\prime\prime}(f)(\partial_i f)^2$. Sum over $i$.')
entry('Laplacian of a dot product',r'\lap(\A\cdot\B)=(\lap\A)\cdot\B+\A\cdot\lap\B+2(\partial_j A_i)(\partial_j B_i).',r'Expand $\partial_j\partial_j(A_iB_i)$ twice with the product rule. The last term sums both $i,j$; it is twice the Frobenius inner product of the two Jacobians, not generally $2(\divg\A)(\divg\B)$.')
entry('Laplacian of a cross product',r'\lap(\A\times\B)=(\lap\A)\times\B+\A\times\lap\B+2\sum_j(\partial_j\A)\times(\partial_j\B).',r'Apply $\partial_\ell\partial_\ell$ to $\eps_{ijk}A_jB_k$. Since epsilon is constant, the three component terms are $\eps_{ijk}[(\lap A_j)B_k+A_j\lap B_k+2(\partial_\ell A_j)(\partial_\ell B_k)]$.')
entry('Laplacian commutes with gradient',r'\lap\grad f=\grad\lap f.',r'For $C^3$ $f$, $\partial_j\partial_j\partial_i f=\partial_i\partial_j\partial_j f$ by commuting partial derivatives. This is a Cartesian statement with constant coefficients.')
entry('Laplacian commutes with divergence and curl',r'\lap(\divg\A)=\divg(\lap\A),\qquad \lap(\curl\A)=\curl(\lap\A).',r'For $C^3$ $\A$, move $\partial_\ell\partial_\ell$ through $\partial_i$ in $\partial_\ell\partial_\ell\partial_iA_i$, or through $\eps_{ijk}\partial_j$ in $\partial_\ell\partial_\ell\eps_{ijk}\partial_jA_k$.')
entry('Triple curl',r'\curl\curl\curl\A=-\lap(\curl\A).',r'Apply double curl to $\curl\A$. Its divergence is zero, so the gradient-of-divergence term vanishes. The result follows for $C^3$ fields.')
entry('Curl of a scalar times a gradient',r'\curl(f\grad g)=\grad f\times\grad g.',r'$\eps_{ijk}\partial_j(f\partial_k g)=\eps_{ijk}(\partial_j f)(\partial_k g)+f\eps_{ijk}\partial_j\partial_k g$. The second term vanishes by Hessian symmetry.')
entry('Divergence of two crossed gradients',r'\divg(\grad f\times\grad g)=0.',r'Expand $\eps_{ijk}\partial_i[(\partial_j f)(\partial_k g)]$. The term with $\partial_i\partial_j f$ vanishes by symmetry in $i,j$, and the term with $\partial_i\partial_k g$ vanishes by symmetry in $i,k$.')
entry('Curl energy and the antisymmetric Jacobian',r'|\curl\A|^2=(\partial_iA_j)(\partial_iA_j)-(\partial_iA_j)(\partial_jA_i).',r'Contract $\eps_{kij}\eps_{k\ell m}(\partial_iA_j)(\partial_\ell A_m)$ to obtain the right side. If $W=(J-J^T)/2$ then $|\curl\A|^2=2W_{ij}W_{ij}$.',r'Curl records the antisymmetric part of local velocity variation; symmetric strain is different.')
section('Radial fields: the gravity toolkit')
parts.append(r'Here $r=|\xx|>0$, $\widehat{\mathbf r}=\xx/r$, and space has dimension three. These formulas do not include the origin unless a distributional statement explicitly says so.'+'\n')
entry('Position and radius derivatives',r'\partial_i x_j=\delta_{ij},\quad \partial_i r=\frac{x_i}{r},\quad\partial_i\widehat r_j=\frac{\delta_{ij}-\widehat r_i\widehat r_j}{r}.',r'Differentiate $r^2=x_jx_j$: $2r\partial_i r=2x_i$. Apply the quotient rule to $x_j/r$ to get $\delta_{ij}/r-x_ix_j/r^3$.')
entry('Radial scalar gradient and Hessian',r'\begin{aligned}\grad u(r)&=u^{\prime}(r)\widehat{\mathbf r},\\ \partial_i\partial_j u(r)&=u^{\prime\prime}\widehat r_i\widehat r_j+\frac{u^{\prime}}r(\delta_{ij}-\widehat r_i\widehat r_j).\end{aligned}',r'First use $\partial_i u=u^{\prime}x_i/r$. Differentiate again and insert the unit-radius derivative from the preceding identity. The Hessian has a radial eigenvalue $u^{\prime\prime}$ and two tangential eigenvalues $u^{\prime}/r$.')
entry('Radial scalar Laplacian',r'\lap u(r)=u^{\prime\prime}(r)+\frac{2}{r}u^{\prime}(r)=\frac1{r^2}\frac{d}{dr}\big(r^2u^{\prime}(r)\big).',r'Trace the radial Hessian: $\widehat r_i\widehat r_i=1$ and $\delta_{ii}=3$. Thus the trace is $u^{\prime\prime}+(3-1)u^{\prime}/r$. Expand the ordinary derivative to obtain the final form.')
entry('Radial divergence and curl',r'\divg[a(r)\widehat{\mathbf r}]=a^{\prime}+\frac{2a}{r},\quad\curl[a(r)\widehat{\mathbf r}]=\mathbf0.',r'Write $F_i=a(r)x_i/r$. Then $\partial_i F_i=a^{\prime}x_ix_i/r^2+a(3/r-r^2/r^3)$. For curl, $\partial_jF_k$ is a linear combination of $\delta_{jk}$ and $x_jx_k$, both symmetric; contraction with $\eps_{ijk}$ vanishes.')
entry('Power-law Laplacian and inverse-square flux',r'\lap r^n=n(n+1)r^{n-2},\quad\lap\frac1r=0\ (r>0),\quad\int_{S_R}\frac{\xx}{r^3}\cdot\nn\,dS=4\pi.',r'Insert $u^{\prime}=nr^{n-1}$ and $u^{\prime\prime}=n(n-1)r^{n-2}$ into the radial Laplacian. On the sphere $r=R$, $\nn=\xx/R$, so $x_in_i/r^3=1/R^2$. Multiply by surface area $4\pi R^2$.',r'Zero ordinary divergence away from a source does not mean zero flux around it.')
entry('Point-source distribution',r'\divg\frac{\xx}{r^3}=4\pi\delta^{(3)}(\xx),\qquad \lap\frac1r=-4\pi\delta^{(3)}(\xx).',r'For a compactly supported smooth test function $\psi$, distributional divergence gives $-\int (x_i/r^3)\partial_i\psi\,d^3x$. Excise a ball of radius $\eta$. Ordinary divergence is zero outside it, and the outward normal of the excised domain is $-\widehat{\mathbf r}$. Integration by parts gives $\int_{S_\eta}\psi/\eta^2\,dS\to4\pi\psi(0)$. The omitted ball contribution tends to zero because $r^{-2}$ is locally integrable in three dimensions. Since $\grad(1/r)=-\xx/r^3$, the Laplacian identity follows. No extra point term appears in this first derivative because the corresponding boundary term scales as $\eta$.',r'The delta is a source concentrated at a point, not an ordinary finite value assigned at the origin.')
section('From local derivatives to integral theorems')
parts.append(r'Use piecewise smooth boundaries and compatible orientations. Fields extend with the stated regularity to a neighbourhood of the integration region, except in the explicitly excised point-source construction. A boundary component surrounding a hole has the induced opposite orientation.'+'\n')
entry('Gradient theorem',r'\int_C\grad f\cdot d\xx=f(\xx(b))-f(\xx(a)).',r'For a piecewise $C^1$ parameterisation $x_i(t)$ and $C^1$ $f$, $\partial_i f(x(t))\dot x_i(t)=d f(x(t))/dt$. Integrate and apply the one-dimensional fundamental theorem on each segment; endpoint terms telescope.',r'For a mechanical force $\F=-\grad U$, work is $U(a)-U(b)$.')
entry('Divergence theorem',r'\int_{\partial V}F_i n_i\,dS=\int_V\partial_iF_i\,dV.',r'For a rectangular box, integrate $\partial_iF_i$ first in $x_i$. The fundamental theorem gives the value of $F_i$ on its two opposite faces with normals $+e_i,-e_i$. Sum $i$. Subdividing a general bounded region with piecewise smooth (or Lipschitz) boundary cancels all internal face fluxes. The boundary and volume Riemann sums converge to the displayed integrals for $C^1$ $\F$.',r'Only outer faces survive when neighbouring boxes are combined.')
entry('Stokes theorem',r'\int_{\partial S}F_i\,dx_i=\int_S\eps_{ijk}\partial_jF_k\,n_i\,dS.',r'On a smooth parameterised patch $x_i(u,v)$, set $a=F_ix_{i,u}$ and $b=F_ix_{i,v}$. Green\textquotesingle s rectangle argument gives $\oint(a\,du+b\,dv)=\iint(\partial_u b-\partial_v a)\,du\,dv$. The mixed derivatives of $x_i$ cancel, leaving $(\partial_jF_i)(x_{j,u}x_{i,v}-x_{j,v}x_{i,u})$. Epsilon contraction identifies this with $(\curl\F)_k\eps_{k\ell m}x_{\ell,u}x_{m,v}$. Patch boundaries cancel on an oriented piecewise smooth surface. Use $C^1$ $\F$ and $C^2$ patches.',r'The induced boundary direction follows the right-hand rule. A singular point on the surface invalidates the ordinary theorem.')
entry('Green circulation theorem',r'\oint_{\partial D}(P\,dx+Q\,dy)=\iint_D(\partial_x Q-\partial_y P)\,dx\,dy.',r'On $[a,b]\times[c,d]$, integrate $\partial_xQ$ in $x$ and $-\partial_yP$ in $y$. These give the right-minus-left and bottom-minus-top edge contributions, exactly the counterclockwise boundary integral. Tile a bounded planar region with piecewise smooth boundary, cancel internal edges and take limits. Requires $P,Q\in C^1$ near $\overline D$.')
entry('Green flux theorem',r'\oint_{\partial D}(P\,dy-Q\,dx)=\iint_D(\partial_xP+\partial_yQ)\,dx\,dy.',r'Apply the previous theorem to the pair $(-Q,P)$. On a positively oriented boundary, the outward normal satisfies $\nn\,ds=(dy,-dx)$, so the boundary form equals $(P,Q)\cdot\nn\,ds$.')
entry('Scalar-vector integration by parts',r'\int_V f\,\divg\A\,dV=\int_{\partial V}f\A\cdot\nn\,dS-\int_V\grad f\cdot\A\,dV.',r'Integrate $\partial_i(fA_i)=f\partial_iA_i+(\partial_i f)A_i$ and use the divergence theorem on $f\A$.')
entry('Green first identity',r'\int_V(f\lap g+\grad f\cdot\grad g)\,dV=\int_{\partial V}f\,\partial_n g\,dS.',r'Set $A_i=\partial_i g$ in the preceding identity. Then $\partial_iA_i=\lap g$, and $A_in_i=\partial_n g$. Take $f\in C^1$, $g\in C^2$ near the region.')
entry('Green second identity',r'\int_V(f\lap g-g\lap f)\,dV=\int_{\partial V}(f\partial_n g-g\partial_n f)\,dS.',r'Write Green\textquotesingle s first identity for $(f,g)$ and $(g,f)$ with both $C^2$. Subtract; $(\partial_i f)(\partial_i g)$ cancels. This is reciprocity for the Laplacian.')
entry('Curl integration by parts',r'\int_V[\B\cdot\curl\A-\A\cdot\curl\B]\,dV=\int_{\partial V}\nn\cdot(\A\times\B)\,dS.',r'Integrate the cross-product divergence identity $\partial_i(\eps_{ijk}A_jB_k)=B_i(\curl\A)_i-A_i(\curl\B)_i$ and apply the divergence theorem. The boundary sign is fixed by $\nn\cdot(\A\times\B)$.')
entry('Vector forms of surface integration',r'\int_V\grad f\,dV=\int_{\partial V}f\nn\,dS,\quad \int_V\curl\A\,dV=\int_{\partial V}\nn\times\A\,dS.',r'For the first, apply the divergence theorem componentwise to $F_j=f\delta_{ij}$ with fixed $i$. For the second use $F_j=\eps_{ijk}A_k$ with fixed $i$. Their divergences are $\partial_i f$ and $\eps_{ijk}\partial_jA_k$ respectively.')
entry('Green representation formula (three dimensions)',r'\begin{aligned}f(\xx)={}&\int_{\partial V}\left[\Gamma\,\partial_n f-f\,\partial_n\Gamma\right]dS-\int_V\Gamma\,\lap f\,dV,\\ &\Gamma(\xx,\mathbf y)=\frac1{4\pi|\xx-\mathbf y|},\quad \xx\in V.\end{aligned}',r'Assume $f\in C^2$ near a bounded smooth region and $\xx$ strictly inside. In the $\mathbf y$ variable, $\lap_{\mathbf y}\Gamma=-\delta^{(3)}(\mathbf y-\xx)$. Apply Green\textquotesingle s second identity with $g=\Gamma$, excising a ball about $\xx$ and taking its radius to zero (as in identity 42). The volume term becomes $-f(\xx)-\int_V\Gamma\lap f$. Rearranging the outer boundary term $\int_{\partial V}(f\partial_n\Gamma-\Gamma\partial_n f)$ yields the formula. Boundary points require a separate limiting formula.')
section('Potentials and the condition P sub y equals Q sub x')
entry('The planar exactness condition',r'\F=(P,Q)=\grad\phi\ \Longrightarrow\ \frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}.',r'$P=\partial_x\phi$, $Q=\partial_y\phi$. For $C^2$ $\phi$, $\partial_yP=\partial_y\partial_x\phi=\partial_x\partial_y\phi=\partial_xQ$. In tensor language the Jacobian $J_{ij}=\partial_jF_i$ is symmetric. Conversely, for $C^1$ $\F$ on an open simply connected planar domain, this condition is sufficient for a single-valued global potential, by the path-independence argument below.',r'These are \emph{partial} derivatives because $P,Q$ depend on both variables. Compare the off-diagonal derivatives, not $P_x$ and $Q_y$.')
entry('Constructing a potential on a rectangle',r'\phi(x,y)=\int_{x_0}^x P(s,y_0)\,ds+\int_{y_0}^y Q(x,t)\,dt.',r'Assume the rectangle lies in a $C^1$ domain and $P_y=Q_x$. Clearly $\phi_y=Q(x,y)$. Also $\phi_x=P(x,y_0)+\int_{y_0}^y Q_x(x,t)\,dt=P(x,y_0)+\int_{y_0}^y P_y(x,t)\,dt=P(x,y)$. Thus the mixed-partial test is constructively sufficient locally.')
entry('Closed-loop criterion and path independence',r'\F=\grad\phi\quad\Longleftrightarrow\quad\oint_C\F\cdot d\xx=0\ \text{for every closed path }C.',r'On an open connected domain with $C^1$ $\F$, the forward implication is the gradient theorem. For the reverse, choose a base point and define $\phi(\xx)=\int_{\xx_0}^{\xx}\F\cdot d\boldsymbol\ell$. Two paths differ by a closed path, so the value is independent of path. Appending a short coordinate segment gives $\partial_i\phi=F_i$. Curl-free fields on a simply connected domain have zero loop integral: contract each loop to a point and use Stokes on smooth homotopy patches, where the normal curl is zero. General piecewise smooth loops follow by approximation. Simple connectivity is sufficient, not necessary for a particular field.',r'A hole permits a failure but does not force it. All closed-loop integrals being zero is the exact global test.')
entry('Three-dimensional condition and star-shaped construction',r'\begin{gathered}\partial_iF_j=\partial_jF_i\quad\Longleftrightarrow\quad\curl\F=0,\\ \phi(\xx)=\int_0^1 x_iF_i(t\xx)\,dt\quad\text{on a domain star-shaped about }0.\end{gathered}',r'Epsilon contraction shows $\curl\F=0$ is equivalent to the antisymmetric part of $\partial_iF_j$ vanishing. For $C^1$ $\F$, differentiate the integral: $\partial_k\phi=\int_0^1[F_k(t\xx)+t x_i\partial_kF_i(t\xx)]dt$. Symmetry turns $\partial_kF_i$ into $\partial_iF_k$, making the integrand $d[tF_k(t\xx)]/dt$. Hence $\partial_k\phi=F_k(\xx)$. Translate the base point for any other star centre. In $(P,Q,R)$ notation, the conditions are $P_y=Q_x$, $P_z=R_x$, $Q_z=R_y$.')
parts.append(r'''\subsection{Worked example: find a potential rather than guess}
Let $P=2xy+y^2$ and $Q=x^2+2xy+3y^2$. Then $P_y=2x+2y=Q_x$ on all of $\mathbb R^2$. Integrate $\phi_x=P$:
\[\phi=x^2y+xy^2+h(y),\qquad \phi_y=x^2+2xy+h'(y)=Q.\]
Therefore $h'=3y^2$ and $\phi=x^2y+xy^2+y^3+C$. From $(0,0)$ to $(1,1)$, every path has $\int\F\cdot d\xx=3$. On the horizontal-then-vertical path, the first segment contributes zero and the second gives $\int_0^1(1+2y+3y^2)dy=3$. On the diagonal $x=y=t$, $P=3t^2$, $Q=6t^2$, so $\int_0^1 9t^2dt=3$.

\subsection{Worked example: a failed condition}
For $P=-\omega y$, $Q=\omega x$, $P_y=-\omega$ and $Q_x=\omega$. Unless $\omega=0$, they differ, the curl is $2\omega$, and a counterclockwise radius-$R$ circle has circulation $2\pi\omega R^2$. From $(0,0)$ to $(1,1)$, horizontal-then-vertical work is $\omega$; vertical-then-horizontal work is $-\omega$. The difference $2\omega$ equals the curl integral over the unit square.

\subsection{Worked example: equal mixed partials, no global potential}
On $\mathbb R^2\setminus\{0\}$, take $P=-by/(x^2+y^2)$ and $Q=bx/(x^2+y^2)$. With $s=x^2+y^2$,
\[P_y=b(y^2-x^2)/s^2=Q_x.\]
Nevertheless $\xx(\theta)=R(\cos\theta,\sin\theta)$ gives
\[\F\cdot d\xx=b\,d\theta,\qquad\oint\F\cdot d\xx=2\pi b.\]
For $b\ne0$ there is no single-valued global scalar potential. On a slit plane a branch of $\phi=b\arg(x+iy)$ works; its derivative gives the field, but its angle cannot be continuous and single valued on the whole punctured plane. Stokes cannot span the loop with a disk containing the undefined origin. On an annulus the outer and oppositely oriented inner boundary circulations cancel, agreeing with zero ordinary curl on the annulus.

\textbf{Dimension matters.} The punctured plane is not simply connected. In contrast, $\mathbb R^3\setminus\{0\}$ is simply connected: a loop can move around a missing point in the third dimension. Point-mass gravity has the global potential $-GM/r$ there. A missing \emph{line} in three dimensions can reproduce the planar vortex obstruction.
''')
section('Physics and geometry: worked examples')
parts.append(r'''\subsection{Gravity of a point mass: signs, sources, and work}
Newtonian potential per unit test mass and acceleration are
\[\Phi=-\frac{GM}{r},\qquad g_i=-\partial_i\Phi=-GM\frac{x_i}{r^3}.\]
Using the radial gradient identity gives the inward direction immediately. Direct differentiation away from $r=0$ gives
\[\partial_jg_i=-GM\left(\frac{\delta_{ij}}{r^3}-\frac{3x_ix_j}{r^5}\right).\]
This Jacobian is symmetric, so $\curl\mathbf g=0$. Its trace is $-GM(3/r^3-3r^2/r^5)=0$, so vacuum has zero ordinary divergence. Yet sphere flux is $-4\pi GM$. The point-source identity resolves the difference:
\[\divg\mathbf g=-4\pi GM\delta^{(3)}(\xx),\qquad\lap\Phi=4\pi GM\delta^{(3)}(\xx).\]
For a smooth mass density, linear superposition gives $\lap\Phi=4\pi G\rho$ and $\divg\mathbf g=-4\pi G\rho$. Negative divergence describes inward flux to positive mass. A test mass $m$ moving from radius $r_a$ to $r_b$ receives work $m[\Phi(r_a)-\Phi(r_b)]=GMm(1/r_b-1/r_a)$.

\textbf{Planar mixed-partial check.} In the equatorial plane let $P=-GMx/s^{3/2}$, $Q=-GMy/s^{3/2}$ with $s=x^2+y^2>0$. Then $P_y=3GMxy/s^{5/2}=Q_x$. The potential is explicitly $-GM/\sqrt{s}$. Zero planar curl agrees with this. Do not compute a two-dimensional divergence and interpret it as the three-dimensional vacuum divergence: the missing $\partial_z g_z$ is essential.

\subsection{A uniform massive sphere: what changes inside matter?}
For radius $R$, total mass $M$, and density $\rho=3M/(4\pi R^3)$ inside, spherical symmetry and the divergence theorem give
\[4\pi r^2g_r=-4\pi G M_{\rm enclosed}(r),\qquad g_r=-\frac{GM_{\rm enclosed}(r)}{r^2}.\]
Integrating the density gives $M_{\rm enclosed}=M(r/R)^3$ for $r<R$ and $M$ for $r\ge R$. Hence
\[\mathbf g=\begin{cases}-GM\xx/R^3,&r<R,\\-GM\xx/r^3,&r>R,\end{cases}\qquad
\Phi=\begin{cases}-\dfrac{GM}{2R^3}(3R^2-r^2),&r\le R,\\-GM/r,&r\ge R.\end{cases}\]
Integrate $\Phi'=-g_r$, impose zero at infinity, and match at $R$ to obtain this potential. Inside, $\partial_i g_i=-3GM/R^3=-4\pi G\rho$ and $\eps_{ijk}\partial_jg_k=0$; outside use the point-mass calculation. Both potential and normal field are continuous at $R$. Second derivatives jump, so the classical piecewise equations hold away from the boundary, and the Poisson equation holds weakly across it. There is no surface delta because the normal field has no jump.

\includegraphics[width=\textwidth]{gravity-sphere.pdf}
The acceleration magnitude rises linearly from zero at the centre, reaches its maximum at the surface, then decays as $r^{-2}$. The potential is a smooth bowl inside and negative everywhere. The dashed line is the surface; these plots use $GM=R=1$.

\subsection{Gravity close to Earth: constant-field approximation}
With upward height $z$, use $\Phi=g_0 z+C$ and $\mathbf g=(0,0,-g_0)$ on a small patch where $g_0$ is nearly constant. Every spatial derivative of $\mathbf g$ is zero, so both divergence and curl vanish in this approximation. It is not a global model of Earth or its mass distribution. Lifting mass $m$ through height $h$ changes potential energy by $mg_0h$.

\subsection{Electrostatics: same machinery, different sign}
For a positive point charge $q$, $V=q/(4\pi\eps_0r)$ and $\mathbf E=-\grad V=q\xx/(4\pi\eps_0r^3)$. The radial identities give $\curl\mathbf E=0$ away from the source and $\divg\mathbf E=q\delta^{(3)}(\xx)/\eps_0$ distributionally. For a smooth density, $\lap V=-\rho_e/\eps_0$. Gravity draws arrows inward to positive mass; a positive electric charge sends arrows outward. Electrostatic curl is zero, whereas time-varying electromagnetic fields can have $\curl\mathbf E=-\partial_t\mathbf B$.

\textbf{The smooth cloud used in the sliders.} To avoid a singularity in the electric-source experiment, use $V=q/(4\pi\sqrt{r^2+s^2})$ with $s>0$ and $\eps_0=1$. Differentiation gives $E_i=qx_i/[4\pi(r^2+s^2)^{3/2}]$. Tracing its Jacobian gives $\rho_e=3qs^2/[4\pi(r^2+s^2)^{5/2}]$. The outward flux through radius $r$ is $q r^3/(r^2+s^2)^{3/2}$, which tends to $q$ at infinity. Thus the cloud has total charge $q$, not a point source at its centre.

\subsection{Fluid flow: divergence, vorticity, and acceleration}
Rigid rotation $\mathbf v=(-\omega y,\omega x,0)$ has $\partial_i v_i=0$ but $(\curl\mathbf v)_z=\partial_xv_y-\partial_yv_x=2\omega$. Its convective acceleration is
\[(\mathbf v\cdot\grad)\mathbf v=(-\omega^2x,-\omega^2y,0).\]
The kinetic-energy gradient is $(\omega^2x,\omega^2y,0)$, while $\mathbf v\times\curl\mathbf v=(2\omega^2x,2\omega^2y,0)$; their difference matches the inward acceleration. Here no compression is needed for rotation.

Straight shear $\mathbf v=(\gamma y,0,0)$ also has zero divergence but curl $(0,0,-\gamma)$, even though its streamlines are straight. Its convective acceleration is zero because $v_j\partial_jv_i=\gamma y\,\partial_xv_i=0$. The gradient $\grad(|\mathbf v|^2/2)=(0,\gamma^2y,0)$ equals $\mathbf v\times\curl\mathbf v$ and cancels. Curl measures local circulation, not simply whether the drawn streamlines bend.

\subsection{Harmonic saddles and diffusion}
For temperature $T=a x^2+b y^2+c z^2$, $\partial_i\partial_iT=2(a+b+c)$. A saddle $x^2-y^2$ is harmonic even though its gradient $(2x,-2y,0)$ is nonzero almost everywhere. In homogeneous diffusion $\partial_tT=\kappa\lap T$ with constant $\kappa$, summed curvature controls the instantaneous local change. The bowl $x^2+y^2$ has $\lap T=4$; the saddle has zero local diffusion rate for that ideal field. Initial and boundary conditions are still required to solve an evolution problem.

\subsection{Double curl in electromagnetic waves}
In a homogeneous, source-free region with constant $\mu,\eps$,
\[\curl\mathbf E=-\partial_t\mathbf B,\quad\curl\mathbf B=\mu\eps\partial_t\mathbf E,\quad\divg\mathbf E=0.\]
Taking curl of the first equation and commuting smooth space/time derivatives gives $\curl\curl\mathbf E=-\mu\eps\partial_t^2\mathbf E$. The double-curl identity reduces the left side to $-\lap\mathbf E$, yielding $\lap\mathbf E=\mu\eps\partial_t^2\mathbf E$. Plane waves therefore have speed $1/\sqrt{\mu\eps}$. This reduction relies on the stated constitutive and source assumptions.
''')
section('Using the atlas responsibly')
parts.append(r'''\subsection{Curvilinear coordinates and tensor notation}
These proofs used a fixed Cartesian basis. In cylindrical or spherical coordinates, basis vectors vary with position. Simply replacing Cartesian partial derivatives with derivatives of physical spherical components gives wrong answers. In arbitrary coordinates on flat Euclidean space, use the metric $g_{ij}$ and its covariant derivative $\nabla_i$, with appropriate index raising: $\operatorname{div}\A=\nabla_iA^i$, $(\operatorname{grad}f)^i=g^{ij}\partial_j f$ and $\Delta f=\nabla_i\nabla^i f$. The volume Levi-Civita \emph{tensor} replaces the constant symbol. Flat-space identities remain valid when all objects are transformed consistently. On curved manifolds derivative commutations can introduce curvature terms, so the Cartesian double-curl proof cannot be transplanted blindly.

\subsection{A short study route}
First master identities 1--5 and the meanings of free and dummy indices. Next prove the three scaled-field rules without looking. Then use epsilon contraction to derive double curl and curl of a cross product. Finally test potentials: calculate the off-diagonal derivatives, inspect the domain, construct a potential when possible, and verify its gradient. Use the gravity examples to practise the difference between a smooth vacuum calculation and a source represented distributionally.

\newpage\subsection{Further reading and conventions}
The proofs and worked examples in this atlas are original expositions of standard identities. The following primary educational sources provide additional background:
\begin{itemize}
\item OpenStax, \emph{Calculus Volume 3}, sections 6.3--6.7: conservative fields, Green, Stokes and divergence theorems.\\{\small\url{https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields}}
\item MIT OpenCourseWare, \emph{18.02SC Multivariable Calculus}, vector fields and line integrals.\\{\small\url{https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/}}
\item Richard Fitzpatrick, University of Texas, \emph{Gravitational Potential of Uniform Spheroid}, for Poisson-equation methods in gravity.\\{\small\url{https://farside.ph.utexas.edu/teaching/355/Surveyhtml/node61.html}}
\end{itemize}
\textbf{Rebuild.} Run \texttt{python scripts/build\_atlas.py} from the repository. Python needs NumPy and Matplotlib; a TeX installation needs pdfLaTeX and the packages listed in the source preamble. The script regenerates the two exact figures, the LaTeX source and this PDF. No network access is required during the build.
\end{document}
''')
(DOC/'vector-calculus-atlas.tex').write_text(''.join(parts))
# Accessible Markdown companion uses exactly the same statements and proofs.
import re
aliases={r'\A':r'\mathbf{A}',r'\B':r'\mathbf{B}',r'\C':r'\mathbf{C}',r'\F':r'\mathbf{F}',r'\xx':r'\mathbf{x}',r'\nn':r'\mathbf{n}',r'\grad':r'\nabla',r'\divg':r'\nabla\cdot',r'\curl':r'\nabla\times',r'\lap':r'\nabla^2',r'\eps':r'\varepsilon'}
def expand(text):
    text=re.sub(r'\\[A-Za-z]+',lambda m:aliases.get(m[0],m[0]),text)
    text=text.replace(r'\emph{','').replace(r'\textquotesingle s',"'s")
    return text
md=['# Vector calculus identity and proof catalogue\n\n[Download the typeset PDF](docs/vector-calculus-atlas.pdf). '
    'These 57 standard statements use oriented Cartesian coordinates in Euclidean 3D. '
    'Repeated indices are summed. First-order rules require C¹, second-order rules C², '
    'and third-order commutations C³. Integral and domain assumptions appear in the proofs. '
    'This is a comprehensive standard repertoire, not every possible derived identity.\n']
count=0
for part in parts:
    if not part.startswith(r'\identity'):continue
    # Extract the two balanced-brace macro arguments.
    pos=len(r'\identity');args=[]
    for _ in range(2):
        start=pos+1;level=1;pos=start
        while level:
            if part[pos]=='{':level+=1
            elif part[pos]=='}':level-=1
            pos+=1
        args.append(part[start:pos-1])
    count+=1
    proof=part[pos:].strip().replace(r'\proof ','**Index proof.** ').replace(r'\sense ','**Picture / use.** ')
    md.append(f'\n## {count}. {args[0]}\n\n$$\n{expand(args[1])}\n$$\n\n{expand(proof)}\n')
(ROOT/'IDENTITIES.md').write_text(''.join(md))

for _ in range(4):
    subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','vector-calculus-atlas.tex'],cwd=DOC,stdout=subprocess.DEVNULL,check=True)
print(f'{len([p for p in parts if p.startswith(chr(92)+"identity")])} numbered identities; {DOC / "vector-calculus-atlas.pdf"}')
