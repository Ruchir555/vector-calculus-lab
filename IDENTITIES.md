# Read the types first

The symbol ∇ is a differential operator. Dot and cross do not make it an
ordinary constant vector. It acts on position-dependent factors.

| Operation | Input | Output | What to picture |
| --- | --- | --- | --- |
| ∇f | Scalar | Vector | Steepest local increase |
| ∇·A | Vector | Scalar | Outward flux per tiny volume |
| ∇×A | Vector | Vector | Circulation per tiny oriented area |
| ∇²f | Scalar | Scalar | Sum of coordinate curvatures |
| ∇²A | Vector | Vector | Laplacian of each Cartesian component |
| (A·∇)B | Two vectors | Vector | How B changes along A |

## Operator identities

- ∇·∇f = ∇²f.
- ∇×∇f = 0.
- ∇·(∇×A) = 0.
- ∇×(∇×A) = ∇(∇·A) − ∇²A.

The middle two and double curl use equality of mixed partials for C² fields.
A zero operation result does not mean its input field is zero.

## Product identities

- ∇(fg) = f∇g + g∇f.
- ∇·(fA) = f(∇·A) + (∇f)·A.
- ∇×(fA) = f(∇×A) + (∇f)×A.
- ∇·(A×B) = B·(∇×A) − A·(∇×B).
- ∇×(A×B) = A(∇·B) − B(∇·A) + (B·∇)A − (A·∇)B.
- ∇(A·B) = (A·∇)B + (B·∇)A + A×(∇×B) + B×(∇×A).

One useful special case is

**(A·∇)A = ½∇|A|² − A×(∇×A).**

The operators are also linear: gradient, divergence, curl, and Laplacian
distribute over sums and constant scalar multiples.

## Integral statements

- **Gradient theorem:** the integral of ∇f along a path equals f(end) − f(start),
  for a single-valued differentiable potential and a suitable path.
- **Divergence theorem:** the outward flux through a closed boundary equals the
  volume integral of divergence over the interior.
- **Stokes’ theorem:** circulation along an oriented boundary equals the surface
  integral of curl dotted with the consistent normal.

For the last two, the field must have the required smoothness throughout the
relevant region or a neighbourhood of the surface, respectively.

## Sign and domain checks

1. What type should the answer have?
2. Which quantities vary with position?
3. Which factors must be differentiated?
4. Did you reverse a cross product and therefore reverse its sign?
5. Are you using all three derivatives, even though the drawing is 2D?
6. Is the field smooth on the entire domain or spanning surface?
7. Does the boundary orientation match the normal?

“Curl-free implies a global potential” has a domain condition: a simply
connected domain is sufficient for a smooth curl-free field. The punctured
plane vortex in the guide is the useful counterexample.
