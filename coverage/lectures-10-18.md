# Source coverage: lectures 10–18

All pages of each original handwritten PDF were downloaded and visually inspected after rendering with `pdftoppm` at 1800 pixels on the long side. Contact sheets were used for complete page inventory. Titles, equations, examples, boundary conditions, diagrams, and explanatory qualifications were checked. The book chapters are original expositions with supplemental derivations; this table maps scientific subject coverage rather than copied text. Original PDFs are linked in every chapter and retained only in the ignored local cache.

The source URL pattern is `https://www.alucasphys.com/p7810s2026/p7810s2026_lectureN.pdf`. Local source names are `.cache/sources/lecture-NN.pdf`; contact sheets and rendered pages are in `.cache/pages/`. Page numbers below count the title page as page 1.

## Lecture 10: Incompressible inviscid flows (6 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Inviscid and constant density assumptions; mass and Euler equations; sound wave timescales; water and air sound speeds; slow nearly incompressible sector | `10-inviscid.qmd`, `sec-l10-limit` |
| 2 | Expansion of density in inverse sound speed squared; incompressibility with finite pressure gradient; Bernoulli along streamlines; irrotational potential and Laplace equation | `sec-l10-limit`, `sec-l10-bernoulli` |
| 3 | Harmonic real part of analytic potential; Cauchy–Riemann identities; stream function constant on streamlines; complex velocity; orthogonal coordinate picture | `sec-l10-complex` |
| 4 | Flow outside disk; no penetration and far field conditions; uniform plus dipole complex potential; pressure force on a solid and Bernoulli | `sec-l10-cylinder`, `sec-l10-lift` |
| 5 | Contour algebra and Blasius theorem; zero force without circulation; circulation term needed for lift; distant contour evaluation | `sec-l10-lift`, including supplemental contour derivation |
| 6 | Residue and Kutta–Joukowski lift; logarithmic vortex potential; real circulation versus source/sink; explicit velocity components | `sec-l10-lift`, exercises |

Clarifications: counterclockwise circulation and counterclockwise body contour are stated so the lift sign is unambiguous. Forces are per unit cylinder length. The incompressible density limit is distinguished from setting the dynamic pressure gradient to zero. No unresolved source topic remains.

## Lecture 11: Vortex dynamics (6 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Tensor and vector vorticity; kinematic viscosity; curl of Navier–Stokes; convection, stretching, diffusion | `11-vortices.qmd`, `sec-l11-vorticity` |
| 2 | Two dimensional transport; distributional point vortex; heat kernel vorticity; integration to obtain circulating velocity | `sec-l11-diffusion` |
| 3 | Viscous vortex velocity; radial pressure deficit; central pressure and tornado estimate; point vortices advect one another; equal and opposite vortex pairs | `sec-l11-diffusion`, `sec-l11-point`, exercises |
| 4 | Hamiltonian point vortices, Poisson bracket, first order action; applications; image vortex at wall; three dimensional vortex line concept | `sec-l11-point`, supplemental action derivation, `sec-l11-kelvin` |
| 5 | Biot–Savart line integral; motion with local fluid velocity; Kelvin material circulation derivation | `sec-l11-kelvin` |
| 6 | Frozen-in motion sketch; circular vortex ring self velocity, logarithmic divergence and core cutoff; axial propagation | `sec-l11-kelvin` |

Clarifications: Hamiltonian sums use unordered pairs to avoid double counting; the symplectic convention is explicit. The central pressure integral is evaluated with the Gaussian core. Ring speed is given as a leading logarithmic estimate with a core-dependent subleading constant. The wall image enforces slip/no penetration, not no slip. No unresolved source topic remains.

## Lecture 12: Incompressible viscous flows (6 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Constant density/temperature approximation; plane Poiseuille ansatz; vanished nonlinear acceleration; no slip and quadratic profile | `12-viscous.qmd`, `sec-l12-equations`, `sec-l12-poiseuille` |
| 2 | Flux and width scaling; electrical resistor analogy; junction conservation; hydraulic resistance; dominant balance and pressure constraint | `sec-l12-poiseuille`, `sec-l12-resistance`, `sec-l12-reynolds` |
| 3 | Reynolds number and everyday scale; creeping flow; sphere drag setup; divergence free vector potential; axisymmetry and vector Laplacian caution | `sec-l12-reynolds`, `sec-l12-sphere` |
| 4 | Radial power ansatz, allowed powers, far field and no slip conditions; force from stress | `sec-l12-sphere` |
| 5 | Stress components and pressure; surface integral; Stokes force; checking approximation by dominant balance | `sec-l12-sphere`, `sec-l12-matching` |
| 6 | Large distance nonuniformity; length R/Re; inner creeping and outer inertial regions; matched asymptotic expansion sketch | `sec-l12-matching` |

Clarifications: planar flux is explicitly per unit breadth, with a separate circular pipe calculation giving fourth power radius scaling. Stress conventions and whether the sphere or fluid moves are stated. Radius-based and diameter-based Reynolds numbers and projected versus wetted area are distinguished. No unresolved source topic remains.

## Lecture 13: Boundary layers (7 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Flat plate flow; no slip conflict with inviscid exterior; arbitrary length scale and large Reynolds limit | `13-boundary-layers.qmd`, `sec-l13-singular` |
| 2 | Infinite plate oscillatory flow; translation symmetry and continuity; Fourier diffusion solution; square root viscous thickness | `sec-l13-oscillatory` |
| 3 | Steady layer thickness; guessed pressure and derivative hierarchies; stream function equation; dimensionless variables; similarity ansatz | `sec-l13-prandtl`, `sec-l13-blasius` |
| 4 | Similarity exponent relations; far field velocity condition; Blasius ODE; no slip/no penetration boundary data | `sec-l13-blasius` |
| 5 | Numerical profile; near wall and outer behavior; derivative hierarchy; transverse pressure estimate and leading edge failure | `sec-l13-blasius`, `sec-l13-consistency` |
| 6 | Small streamwise pressure correction; shear stress integrated over both faces; drag coefficient and Re^(-1/2) scaling | `sec-l13-consistency`, `sec-l13-drag` |
| 7 | Comparison with sphere creeping drag; different Reynolds scaling; boundary layers versus creeping regime | `sec-l13-drag`, common pitfalls |

Clarifications: oscillating wall and externally accelerated outer flow are both described, with pressure forcing needed in the latter. The coefficient 1.328 is tied to wetted area and a laminar attached layer. Source geometry sketches are described in words. No unresolved source topic remains.

## Lecture 14: Instabilities of viscous flows (6 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Exact plane Poiseuille profile; existence versus stability; small perturbations; long time growth question | `14-instabilities.qmd`, `sec-l14-base` |
| 2 | Linearized momentum/continuity; background shear; Fourier stream function; pressure elimination; generalized eigenvalue problem | `sec-l14-linear`, `sec-l14-os` |
| 3 | Complex temporal frequency; why k is real; boundary driven instability; nondimensional Orr–Sommerfeld equation; spectral solution and discrete spectrum | `sec-l14-os` |
| 4 | Neutral curve and Rc approximately 5772; unstable wave number interval; turbulent versus laminar possibilities; experimental finite amplitude structures below linear threshold | `sec-l14-threshold` |
| 5 | Critical mode and damped modes; symmetry constrained amplitude equation; intensity equation; supercritical square root amplitude; possible negative cubic coefficient | `sec-l14-amplitude` |
| 6 | Quintic saturation; nonzero branches; subcritical interval and finite amplitude perturbation threshold | `sec-l14-amplitude`, exercises |

Clarifications: Reynolds number is based on maximum velocity and channel half-width; the numerical threshold is not a universal transition criterion. Plane channel and pipe puff terminology are distinguished. The amplitude model is labeled phenomenology and not asserted to derive fully developed turbulence. No unresolved source topic remains.

## Lecture 15: Turbulence (7 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Reynolds regimes past obstacle; nonlinear predictable versus turbulent flow; chaos, multiple scales, large and dissipative eddies | `15-turbulence.qmd`, `sec-l15-overview` |
| 2 | Three dimensional direct cascade; limitations of theory; mean/fluctuation decomposition; averaged momentum equation; unclosed higher moments | `sec-l15-overview`, `sec-l15-rans` |
| 3 | Eddy viscosity closure; mixing estimate; wake example; order one drag scaling; Gaussian downstream deficit | `sec-l15-rans`, `sec-l15-wake` |
| 4 | Self consistent turbulent viscosity; momentum deficit fixes wake integral; square root wake width; comparison with laminar layer; entrainment; setup of K41 | `sec-l15-wake`, `sec-l15-k41` |
| 5 | Isotropic driven cascade; statistically constant energy flux; spectrum and dimensions; energy per mass injection rate | `sec-l15-k41` |
| 6 | Dimensional exponents 2/3 and -5/3; local Reynolds number; dissipative cutoff; Re^(3/4) scale range; dimensional caveat | `sec-l15-k41`, `sec-l15-cutoff` |
| 7 | Two dimensional inverse energy cascade; quasi-two-dimensional atmosphere; persistent large vortices | `sec-l15-inverse` |

Clarifications/corrections: the eddy stress sign is chosen so positive eddy viscosity diffuses mean momentum. The source's crude subtraction of upstream/downstream squared velocities produces an order-one wake drag coefficient that is not an exact momentum-deficit formula; the book states the proper recovered-pressure deficit and explains why displacement mass flux matters. All turbulence scalings and closures are labeled as phenomenology and their assumptions stated. The total versus mass-specific energy spectrum distinction is explicit. No unresolved source topic remains.

## Lecture 16: Surface tension and gravity waves (6 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Interfacial area energy; small slope height graph; local geometry | `16-surface-waves.qmd`, `sec-l16-energy` |
| 2 | Area expansion; variational surface force; pillbox stress balance; curvature pressure; spherical interface example | `sec-l16-energy`, `sec-l16-laplace` |
| 3 | Pressure inside bubble; soap film and minimal area; capillary action and hydrostatic pressure; cylindrical meniscus equation | `sec-l16-laplace`, `sec-l16-capillary` |
| 4 | Parabolic meniscus; wall slope angle; Jurin law; gravity wave geometry; potential flow; dynamic and kinematic surface conditions | `sec-l16-capillary`, `sec-l16-wave-setup` |
| 5 | Bottom condition; Fourier/cosh solution; finite depth gravity–capillary dispersion; deep/shallow water limits | `sec-l16-dispersion` |
| 6 | Inverted water/air interface; gravity sign change; unstable long waves and surface tension cutoff; centimeter scale estimate | `sec-l16-inverted` |

Clarifications: a single spherical interface has 2 alpha/R pressure jump; a soap bubble has two interfaces and 4 alpha/R. The source's small wall slope angle and the conventional liquid contact angle are distinguished. The inverted cutoff is a characteristic instability scale, not a universal droplet diameter. A supplemental two-fluid deep-water relation checks the density assumptions. No unresolved source topic remains.

## Lecture 17: Atmospheric fluid flows (6 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Rotating coordinate transformation; Coriolis/centrifugal forces; modified pressure; rotating incompressible equation | `17-atmosphere.qmd`, `sec-l17-rotating` |
| 2 | Reynolds and Rossby comparisons; atmospheric scales; steady geostrophic balance; pressure difference estimate | `sec-l17-numbers` |
| 3 | Curl of geostrophy and Taylor–Proudman; quasi-two-dimensional columns; wall viscous layer; exterior geostrophic flow | `sec-l17-taylor-proudman`, `sec-l17-ekman` |
| 4 | Ekman ODE, complex solution, spiraling components and thickness; boundary-driven mixing; effective rotation on Earth; gravity/Coriolis ratio | `sec-l17-ekman`, `sec-l17-gravity` |
| 5 | Hydrostatic centrifugal level surface; thin atmosphere; small vertical speed; local rotation projection and horizontal 2D equations | `sec-l17-gravity` |
| 6 | Local horizontal equation; low pressure circulation in both hemispheres; geostrophic ocean height slope and meter over 1000 km estimate | `sec-l17-gravity`, `sec-l17-examples` |

Clarifications/corrections: the displayed characteristic values U=10 m/s, L=1000 km and nu=10^(-5) m²/s give Re=10^12, so the book uses this arithmetic rather than a looser exponent in the handwritten estimate. Colatitude versus latitude and the factor two in Rossby number are explicit. Geostrophic and homogeneous Taylor–Proudman assumptions are separated from a real stratified atmosphere; equatorial breakdown is stated. No unresolved source topic remains.

## Lecture 18: Convection (7 pages)

| Source page | Topics inspected | Book coverage |
|---|---|---|
| 1 | Full mass/momentum/energy equations; viscous tensor; kinetic plus specific internal energy; entropy variables | `18-convection.qmd`, `sec-l18-energy` |
| 2 | Thermodynamic differential; cancellation of kinetic and pressure work terms; material entropy/heat equation; meaning of convection | `sec-l18-temperature` |
| 3 | Constant pressure specific heat approximation; Brinkman number; thermal diffusivity; heated plate; Prandtl number; low Prandtl thermal thickness | `sec-l18-temperature`, `sec-l18-forced` |
| 4 | Wall heat flux; high Prandtl near wall shear estimate and cube root thickness; thermal expansion coefficient; small density contrast | `sec-l18-forced`, `sec-l18-boussinesq` |
| 5 | Pressure compression criterion; Boussinesq equations; side heated box; small flow and conductive temperature approximation | `sec-l18-boussinesq`, `sec-l18-box` |
| 6 | Linear conductive profile; pressure elimination and biharmonic stream function; particular solution plus wall correction; viscous speed scale; ideal gas expansion estimate | `sec-l18-box`, `sec-l18-inertial` |
| 7 | Failure of viscous velocity estimate; inertial buoyancy balance; realistic free-fall speed | `sec-l18-inertial` |

Clarifications: specific entropy is separated from entropy density and internal from total energy. The pressure term omitted by a constant-pressure temperature approximation is stated. The stream function forcing sign follows an explicitly upward vertical axis; its magnitude matches the source. A particular biharmonic polynomial is not claimed to satisfy no slip until a homogeneous correction is added. The conductive temperature assumption also requires small Péclet number. A supplemental Grashof/Rayleigh discussion distinguishes a side heated cavity from a bottom heated onset problem. No unresolved source topic remains.
