# Vector Calculus: A Visual Learning Guide

Use the live lab to move the parameters for each example. Start with the meaning, predict a change, then use the algebra to explain it.

## 1. Gradient

**∇f = (∂ₓf, ∂ᵧf, ∂𝓏f)**

Type: scalar → vector.

Imagine f as height. The gradient points towards the steepest increase. Its magnitude is the steepest slope, not the height itself.

**Experiment:** f = a x² + b y² + ½xy + 0.2z²

Change a or b to turn the bowl into a saddle. Click a point: the arrow should cross the local contour at a right angle. At a stationary point the gradient vanishes even if the height is nonzero.

**Common confusion:** A gradient is not a path and not a velocity by definition. The arrows are a field of local slopes. The plot shows its x–y components; the readout also includes z.

**Worked argument:**

1. A small displacement gives Δf ≈ ∇f · Δr.
2. Along a unit direction u, the slope is ∇f · u.
3. This is largest when u points along ∇f. A contour has Δf = 0, so its tangent is perpendicular to the gradient.

**Predict:** If you double f everywhere, what happens to its gradient?

<details><summary>Explanation</summary>

Its gradient doubles. The contour shapes stay the same, but their values and slopes change.

</details>

## 2. Divergence

**∇·F = ∂ₓFₓ + ∂ᵧFᵧ + ∂𝓏F𝓏**

Type: vector → scalar.

Put a tiny box around a point. Divergence asks whether more field flows out than in, divided by the box volume. A fast uniform flow still has zero divergence.

**Experiment:** F = (ax − by, bx + ay, 0); div F = 2a

a controls expansion; b controls rotation. Set a = 0 and increase b: the arrows rotate, but there is no net outward flux. The orange square is a finite area probe.

**Common confusion:** Divergence is not the arrow length. It measures how the field changes across opposite faces. Here F𝓏 = 0 and there is no z dependence, so 3D divergence equals the planar divergence.

**Worked argument:**

1. Right minus left flux ≈ (∂ₓFₓ) Δx Δy Δz.
2. Add the other two pairs of faces.
3. Divide by Δx Δy Δz and take the small-box limit.

**Predict:** Can a field have both divergence and curl?

<details><summary>Explanation</summary>

Yes. F = (ax − by, bx + ay, 0) has divergence 2a and curl (0,0,2b). Expansion and rotation are independent here.

</details>

## 3. Curl

**(∇×F)𝓏 = ∂ₓFᵧ − ∂ᵧFₓ**

Type: vector → vector.

Curl measures circulation per oriented area in the small-loop limit. In this plane, positive z-curl means counterclockwise circulation when viewed from +z.

**Experiment:** F = (ax − by, bx + ay, 0); curl F = (0,0,2b)

Set b = 0 and vary a: expansion has no curl. Set a = 0 and change the sign of b: circulation reverses. A blue dot means towards you (+z); a cross means away (−z).

**Common confusion:** Curved arrows are not enough to establish nonzero curl. Curl is local, and its direction follows the right-hand rule. For rigid rotation, angular velocity is half the curl.

**Worked argument:**

1. For a small counterclockwise rectangle, bottom plus top contributions give −∂ᵧFₓ times area.
2. Right plus left contributions give ∂ₓFᵧ times area.
3. Their sum is (∇×F)𝓏 times area. The other components use other oriented planes.

**Predict:** For F = (−by, bx, 0), is the curl b or 2b?

<details><summary>Explanation</summary>

It is (0,0,2b). Both velocity gradients contribute. The rigid-body angular velocity is b along z.

</details>

## 4. Laplacian

**∇·(∇f) = ∇²f**

Type: scalar → vector → scalar.

The Laplacian sums the curvature in each coordinate direction. Positive values mean the local neighbour average exceeds the centre value, in the small-neighbourhood limit.

**Experiment:** f = a x² + b y² + ½xy + 0.2z²; ∇²f = 2a + 2b + 0.4

Change a and b independently. A saddle can have zero Laplacian when positive and negative curvatures cancel. The small z curvature in this example adds 0.4.

**Common confusion:** Zero Laplacian does not mean flat or constant. For example x² − y² is harmonic but has a nonzero gradient away from the origin.

**Worked argument:**

1. ∇f = (fₓ,fᵧ,f𝓏).
2. Taking divergence gives fₓₓ + fᵧᵧ + f𝓏𝓏.
3. That sum is the scalar Laplacian.

**Predict:** What is ∇²(x² − y²)?

<details><summary>Explanation</summary>

2 − 2 = 0. The two curvatures cancel, even though the surface is a saddle.

</details>

## 5. Curl of a gradient

**∇×(∇f) = 0**

Type: scalar → vector → vector.

A smooth height function cannot keep increasing as you walk around a tiny closed loop and return to your starting point. The local circulation of its gradient cancels.

**Experiment:** f = a x² + b y² + ½xy + 0.2z²

Make the contours into a saddle. The gradient arrows change substantially, while every component of their curl stays zero (apart from numerical roundoff).

**Common confusion:** The identity requires continuous second partial derivatives. The reverse statement, curl-free implies a global scalar potential, needs domain conditions too.

**Worked argument:**

1. The z component is ∂ₓ(fᵧ) − ∂ᵧ(fₓ).
2. For a C² scalar field, fᵧₓ = fₓᵧ.
3. The x and y components cancel by the same mixed-partial argument.

**Predict:** Does ∇×∇f = 0 mean ∇f itself is zero?

<details><summary>Explanation</summary>

No. A nonconstant smooth potential usually has a nonzero gradient. Its curl is zero, not the gradient.

</details>

## 6. Divergence of a curl

**∇·(∇×A) = 0**

Type: vector → vector → scalar.

Flux generated by a smooth curl has no net source. Contributions cancel through paired mixed partial derivatives. This is a local differential statement.

**Experiment:** A = (ayz, bxz, xy); curl A = ((1−b)x, (a−1)y, (b−a)z)

Here the x–y projection can appear to expand. Move the z slice and inspect the full vector: the z derivative balances the planar divergence. A 2D picture alone can be misleading.

**Common confusion:** Do not calculate only ∂ₓFₓ + ∂ᵧFᵧ for a 3D field. The missing ∂𝓏F𝓏 can be exactly the term that cancels the apparent source.

**Worked argument:**

1. Expand the six terms: ∂ₓ∂ᵧA𝓏 − ∂ₓ∂𝓏Aᵧ + ∂ᵧ∂𝓏Aₓ − ∂ᵧ∂ₓA𝓏 + ∂𝓏∂ₓAᵧ − ∂𝓏∂ᵧAₓ.
2. Pair equal mixed partials with opposite signs.
3. Every term cancels for a C² field.

**Predict:** Can the x–y projection of a divergence-free field look like a source?

<details><summary>Explanation</summary>

Yes. Its planar divergence can be balanced by variation of the out-of-plane component with z.

</details>

## 7. Curl of a curl

**∇×(∇×F) = ∇(∇·F) − ∇²F**

Type: vector → vector.

The double curl is not generally zero. It combines variation of the source strength with a subtraction of the componentwise curvature of the field.

**Experiment:** F = (axy, bx², 0); double curl = (0,a−2b,0)

Toggle the two right-hand terms. At a = 2b they cancel in this example; away from that setting the double curl points along y.

**Common confusion:** ∇²F means apply the scalar Laplacian to each Cartesian component. If div F = 0, double curl equals −∇²F, not zero in general.

**Worked argument:**

1. The x component expands to ∂ₓ∂ᵧFᵧ + ∂ₓ∂𝓏F𝓏 − ∂ᵧ²Fₓ − ∂𝓏²Fₓ.
2. Add and subtract ∂ₓ²Fₓ.
3. Group as ∂ₓ(div F) − ∇²Fₓ; repeat for y and z.

**Predict:** If div F = 0, does curl curl F vanish?

<details><summary>Explanation</summary>

Only if ∇²F also vanishes. In general curl curl F = −∇²F for a divergence-free field.

</details>

## 8. Gradient of a product

**∇(fg) = f∇g + g∇f**

Type: scalar × scalar → vector.

When you move, fg changes because g changes and because f changes. Each contribution is weighted by the value of the other factor.

**Experiment:** f = x+ay; g = cos(bx)+y²+0.1z

Turn off either contribution on the right. You will usually lose agreement. Click different points: a term can vanish locally without vanishing everywhere.

**Common confusion:** ∇ is a differential operator, so it acts on both factors. You cannot treat it as an ordinary vector and distribute without the product rule.

**Worked argument:**

1. For each coordinate i, ∂ᵢ(fg) = f∂ᵢg + g∂ᵢf.
2. Put the three component equations into one vector.
3. The result is f∇g + g∇f.

**Predict:** Why are there two terms rather than just f∇g?

<details><summary>Explanation</summary>

Because f may change with position too. The g∇f term measures that additional change.

</details>

## 9. Divergence of a scaled field

**∇·(fA) = f(∇·A) + (∇f)·A**

Type: scalar × vector → scalar.

Scaling a field by a spatially varying f changes its flux balance in two ways: the original sources are weighted, and the weighting changes along the arrows.

**Experiment:** f = 1+ax; A = (x−by, bx+y, 0)

At a = 0, f is constant and the second term disappears. Increase a: the spatially changing weight makes a new contribution.

**Common confusion:** A divergence-free A does not imply fA is divergence-free. The directional change of f along A can still create net flux.

**Worked argument:**

1. Expand ∑ᵢ ∂ᵢ(fAᵢ).
2. Apply the ordinary product rule: ∑ᵢ f∂ᵢAᵢ + ∑ᵢ Aᵢ∂ᵢf.
3. Recognise f div A + ∇f · A.

**Predict:** When does a divergence-free field remain divergence-free after scaling?

<details><summary>Explanation</summary>

When A · ∇f = 0, so f does not change along the field direction.

</details>

## 10. Curl of a scaled field

**∇×(fA) = f(∇×A) + (∇f)×A**

Type: scalar × vector → vector.

The original circulation is weighted by f. A gradient of the weight across the flow also contributes circulation, through ∇f × A.

**Experiment:** f = 1+ax; A = (x−by, bx+y, 0)

Set b = 0: the original A has no curl, but weighting it unevenly can produce curl. Toggle each term and follow the dot/cross symbols.

**Common confusion:** Cross-product order matters: ∇f × A is the negative of A × ∇f. This is a common sign mistake.

**Worked argument:**

1. The z component is ∂ₓ(fAᵧ) − ∂ᵧ(fAₓ).
2. Expand: f(∂ₓAᵧ − ∂ᵧAₓ) + fₓAᵧ − fᵧAₓ.
3. Recognise f(curl A)𝓏 + (∇f × A)𝓏.

**Predict:** Can multiplying a curl-free field by f introduce curl?

<details><summary>Explanation</summary>

Yes, when ∇f × A is nonzero. A weight gradient across the flow introduces local shear.

</details>

## 11. Divergence of a cross product

**∇·(A×B) = B·(∇×A) − A·(∇×B)**

Type: vector × vector → scalar.

The cross product builds a perpendicular field. Its sources are controlled by how A and B turn, projected onto the other field.

**Experiment:** A = (0,0,1+axy); B = (x−by, bx+y, 0)

Toggle B · curl A and −A · curl B separately. The minus sign is essential. At a = 0 the first term vanishes but the second can remain.

**Common confusion:** A and B are not interchangeable here. Swapping them changes A×B to −A×B and reverses the entire identity.

**Worked argument:**

1. Expand A×B into components, then take divergence.
2. Collect derivatives of A into B · curl A.
3. Collect derivatives of B into −A · curl B.

**Predict:** What changes if A and B are swapped?

<details><summary>Explanation</summary>

Both sides reverse sign, because the cross product is antisymmetric.

</details>

## 12. Curl of a cross product

**∇×(A×B) = A(∇·B) − B(∇·A) + (B·∇)A − (A·∇)B**

Type: vector × vector → vector.

Two terms describe source strengths, and two describe how one field changes as you move along the other. Keep these pairs separate in your mind.

**Experiment:** A = (ay,x,z); B = (x,bz,y)

Switch off terms one by one. Change the z slice: the in-plane arrows do not contain the whole 3D story.

**Common confusion:** (B·∇)A is a directional derivative of A, not B times div A. Its i component is Bₓ∂ₓAᵢ + Bᵧ∂ᵧAᵢ + B𝓏∂𝓏Aᵢ.

**Worked argument:**

1. Use (A×B)ᵢ = εᵢⱼₖ AⱼBₖ and contract the two Levi-Civita symbols.
2. The component result is ∂ⱼ(AᵢBⱼ − AⱼBᵢ).
3. Apply the product rule to those two products to obtain the four terms.

**Predict:** What does (B·∇)A mean geometrically?

<details><summary>Explanation</summary>

Move a small distance in direction B and measure how every component of A changes. It is a vector.

</details>

## 13. Gradient of a dot product

**∇(A·B) = (A·∇)B + (B·∇)A + A×(∇×B) + B×(∇×A)**

Type: vector · vector → scalar → vector.

The dot product measures alignment and magnitude together. Its spatial gradient involves directional changes plus the curls needed to account for turning.

**Experiment:** A = (ay,x,0); B = (x,by,0); A·B = (a+b)xy

Change a: it changes curl A. In this example curl B is zero, so one term is always zero. The other three still reconstruct the full gradient.

**Common confusion:** This is not just two directional derivatives. Those alone generally miss the curl terms.

**Worked argument:**

1. Differentiate AⱼBⱼ with respect to coordinate i.
2. Rewrite Aⱼ∂ᵢBⱼ as Aⱼ∂ⱼBᵢ + [A×curl B]ᵢ.
3. Do the same for the derivative of A to get all four terms.

**Predict:** When do the two cross-with-curl terms disappear?

<details><summary>Explanation</summary>

When both A and B are curl-free, though individual cross terms can also vanish for other reasons such as parallel vectors.

</details>

## 14. Divergence theorem

**∯∂V F·n dS = ∭V ∇·F dV**

Type: boundary integral = volume integral.

Divide a region into tiny boxes. Flux on shared interior faces cancels, leaving only the outer boundary. The sum of the local source strengths equals outward flux.

**Experiment:** F = (ax−by, bx+ay, 0); square side 2r; flux = 8ar²

This is the planar analogue on a square. Resize the square: total flux scales with its area. Change b: rotation contributes no net outward flux.

**Common confusion:** Use a closed boundary and outward normals. This demo displays the 2D theorem; it is also a unit-height prism example because F has no z component or dependence.

**Worked argument:**

1. Each small box has outward flux ≈ divergence × its volume.
2. Adjacent boxes have opposite normals on a shared face. Their internal fluxes cancel.
3. Only the external faces survive when all boxes are added.

**Predict:** If the square is twice as wide, how does total flux change here?

<details><summary>Explanation</summary>

It becomes four times as large, because the divergence is uniform and the planar area quadruples.

</details>

## 15. Stokes’ theorem

**∮∂S F·dr = ∬S (∇×F)·n dS**

Type: boundary integral = surface integral.

Tile a surface with tiny loops. Shared edges are traversed in opposite directions and cancel. Only the outside edge remains.

**Experiment:** F = (ax−by, bx+ay, 0); square side 2r; circulation = 8br²

Resize the counterclockwise square. Circulation grows with area here. Change a: expansion contributes no circulation. The normal is +z.

**Common confusion:** Boundary orientation and surface normal must agree by the right-hand rule. Smoothness must hold on a neighbourhood of the entire spanning surface.

**Worked argument:**

1. Each small loop has circulation ≈ normal curl × its area.
2. Shared edges cancel when the loops are summed.
3. The remaining outer loop has the same circulation as the integral of curl over the surface.

**Predict:** Why can’t you apply the ordinary disk version to the singular vortex in the next lesson?

<details><summary>Explanation</summary>

The vortex is undefined at the origin, so it is not smooth on the entire disk spanning the loop.

</details>

## 16. The hole in the domain

**curl F = 0 away from 0; ∮ F·dr = 2πb around 0**

Type: local derivatives ≠ global topology.

A field can turn around a missing point while having zero curl wherever it is defined. A loop around the hole cannot be shrunk to a point inside the domain.

**Experiment:** F = b(−y,x,0)/(x²+y²), x²+y² > 0; a is unused

Increase b: circulation around the origin increases, while the local curl away from the hole stays zero. The shaded disk is excluded from sampling; the true singularity is the origin.

**Common confusion:** No contradiction: the field fails to be smooth at the origin, so Stokes’ theorem cannot use a disk that includes it. A simply connected domain is a sufficient condition for a smooth curl-free field to have a global potential.

**Worked argument:**

1. For F = b(−y,x,0)/(x²+y²), direct differentiation gives zero curl at r > 0.
2. On a circle of radius R, F = (b/R)eθ and dr = R eθ dθ.
3. The circulation is ∫₀²π b dθ = 2πb, independent of R.

**Predict:** Does zero curl everywhere in a punctured plane guarantee path independence?

<details><summary>Explanation</summary>

No. Loops that wind around the missing origin have nonzero circulation.

</details>
