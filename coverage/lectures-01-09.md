# Source inspection and coverage: lectures 1–9

All **55 PDF pages** listed below were visually inspected from full-page Poppler renders on 19 October 2026. The PDFs are handwritten scans, so this mapping records visual reading rather than relying on empty or incomplete text extraction. Page numbers are PDF page numbers, including the title page. Chapters use original explanatory prose and independently organized derivations; no source pages are embedded or transcribed. Historical class administration is identified, not republished as current course policy.

## Lecture 1 — Stochastic differential equations (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture1.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | Course title/date, class logistics, audience and effective-theory motivation | `01-stochastic.qmd`, “Why hydrodynamics starts with noise”; administrative material described as historical context |
| 2 | Dissipative effective theory, translational symmetry, conservative free-particle Lagrangian, friction, positivity and time-reversal puzzles | “Why hydrodynamics starts with noise” |
| 3 | Independent random-walk jumps, mean displacement, mean-square displacement, definition of D | “From a random walk to diffusion” |
| 4 | Langevin equation, zero-mean delta-correlated Gaussian noise, variance integral, units of noise | “What white noise means” |
| 5 | Statistical reversibility of Brownian paths, multiplicative-noise ambiguity, beginning versus midpoint prescription | “What white noise means”; “Multiplicative noise needs a convention” |
| 6 | Quadratic variation, midpoint drift correction, Itô versus Stratonovich inequivalence at fixed drift | “Multiplicative noise needs a convention”; supplemental Itô chain rule |

Supplements: Wiener-process integral definition, test-function meaning of white noise, Itô formula, geometric Brownian motion, solved exercises. Clarification: free Brownian motion on an infinite line has no normalized stationary position ensemble.

## Lecture 2 — Fokker–Planck equation (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture2.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | Probability density, Itô SDE, statement of Fokker–Planck equation | `02-fokker-planck.qmd`, “Replace random trajectories by a probability density” |
| 2 | Test-function proof, short-time update/Taylor expansion, integration by parts, Gaussian higher moments versus non-Gaussian increments | “Derivation using a test function” |
| 3 | Free Brownian FPE, Fourier solution and Gaussian kernel, variance check | “Free diffusion and its Green function” |
| 4 | Overdamped noisy harmonic oscillator, Fourier-space characteristics, conditional Gaussian distribution and decaying mean | “The overdamped harmonic oscillator” |
| 5 | Stationary oscillator distribution, comparison to Gibbs distribution, fluctuation–dissipation, vector SDE and multivariable FPE | “Equilibrium fixes the noise strength”; “Many coordinates and probability current” |
| 6 | Probability current, closed domains and no-flux boundaries, reflecting interval cosine expansion, uniform stationary state | “Many coordinates and probability current” |

Supplements: normalized oscillator transition kernel, integrating-factor solution, forward/backward generators, absorbing versus reflecting distinction, solved exercises. Non-Gaussian dynamics are stated carefully as jump/general-generator possibilities rather than asserting arbitrary higher derivative truncations preserve positivity.

## Lecture 3 — Time-reversal symmetry (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture3.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | FPE and prescribed stationary weight, effective-operator perspective | `03-time-reversal.qmd`, “Build the generator from the steady state” |
| 2 | Normalization as a left divergence, stationarity as right (∂+μ) factor, leading Gaussian Q, stochastic transition kernel analogy | “Build the generator from the steady state”; “Reverse transition probabilities” |
| 3 | Transposed generator, equilibrium-weighted reverse generator, Q transposition, transition probability relation | “Reverse transition probabilities” |
| 4 | Detailed balance, symmetric Q and fluctuation–dissipation, unlikely reverse oscillator fluctuation, momentum-odd example | “Why detailed balance allows an arrow of time”; “Momentum is odd under time reversal” |
| 5 | Dissipationless Liouville equation, generalized time reversal with involution, strong versus weak conservation, derivative-shift symmetry | “Momentum is odd under time reversal”; “Strong and weak conservation” |
| 6 | Two momenta with anticorrelated noise, strong total-momentum conservation, weak conservation and common noise example | “Strong and weak conservation” |

Supplements: exact state-dependent Itô drift, relative-entropy monotonicity, Itô criteria for pathwise conservation, variance of weakly conserved momentum, solved exercises. Caveat: operator factorization is presented under local diffusion assumptions and appropriate boundaries, not as a theorem for arbitrary nonlocal/topologically nontrivial processes.

## Lecture 4 — MSR Lagrangian (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture4.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | FPE-to-MSR goal, equilibrium generator recap, quantum path-integral analogy | `04-msr.qmd`, “Why introduce another variable?” |
| 2 | Constraint delta functional, discretized paths, Itô normalization/Jacobian, Fourier representation, Gaussian noise average | “Derive the action step by step” |
| 3 | Noise integration, complex MSR action, drift/covariance form, stochastic Hamiltonian rules | “Derive the action step by step”; “Rules for an effective stochastic theory” |
| 4 | Conservation response shifts, time-reversal transformation, state-dependent drift/ordering warning, detailed balance from boundary term | “Rules for an effective stochastic theory”; “Detailed balance as a boundary term”; coefficient-ordering callout |
| 5 | Thermal damped velocity, positivity of damping, fluctuation–dissipation, spin Poisson brackets | “Worked example: a damped velocity”; “Worked example: fixed-length spin dynamics” |
| 6 | Antisymmetric Hamiltonian spin motion, spin-length conservation, invariant transverse response building blocks, allowed dissipative spin dynamics | “Worked example: fixed-length spin dynamics”; supplemental stochastic-geometry note |

Supplements: clearly fixed response-contour convention, conversion to physical friction/noise, transverse projector and Lyapunov calculation, exact caution on curvature drift for constrained Itô noise, solved exercises. The damping sign is fixed by decreasing Φ and positive covariance.

## Lecture 5 — Diffusion (7 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture5.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | Recap of MSR symmetries, hydrodynamics as dissipative field theory | `05-diffusion.qmd`, “From stochastic particles to hydrodynamic fields”; “Functional derivatives and conservation” |
| 2 | Dye-density conservation, boundary/volume argument for slow fields, continuum limit from cell variables | Same first two sections |
| 3 | Functional Euler–Lagrange equations, conserved-number response shift, time reversal, local equilibrium functional, susceptibility, central-limit argument | “Functional derivatives and conservation”; “The equilibrium functional and susceptibility” |
| 4 | Gaussian density weight, invariant response-gradient motif, conductivity positivity, diffusion equation, Einstein relation | “Construct the leading action” |
| 5 | Heat-kernel density solution, distinction from one-particle probability, quasinormal modes, constitutive current, conserved current noise/FDT | “Constitutive relation and fluctuating current”; “Spreading and hydrodynamic modes” |
| 6 | General nonlinear/gradient equilibrium functional, RG scaling dimensions, response dimension, z=2 | “Supplemental derivation: why the leading theory is universal” |
| 7 | Irrelevance of higher response powers, density nonlinearities and derivatives; long-scale validity | Same scaling section |

Supplements: finite-volume sinusoidal relaxation, explicit cutoff/criticality caveats, local-versus-global conservation qualification, solved exercises. χ and σ use the dimensionless-equilibrium-functional convention throughout.

## Lecture 6 — Quasihydrodynamics and correlation functions (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture6.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | Relaxing T to PT, one-derivative f(μ) term and total-derivative variation | `06-quasihydrodynamics.qmd`, “Combined parity and time reversal permits drift” |
| 2 | Boundary term, biased-diffusion mode, left/right movers and conserved versus relative number, separate response shifts | “Combined parity and time reversal permits drift”; “A microscopic cartoon: left and right movers” |
| 3 | Collision MSR coupling, coupled species equations, exact eigenvalue branches, hydrodynamic versus gapped poles, effective diffusivity | “A microscopic cartoon”; “Supplemental derivation: integrate out the fast imbalance” |
| 4 | Mean free path, short-time/wavelength breakdown, quasihydrodynamics definition, symmetric/retarded correlators | “Supplemental derivation: integrate out the fast imbalance”; “What experiments measure” |
| 5 | Translation-invariant correlators, overlap with density, Gaussian MSR integral, symmetrized Fourier quadratic matrix | “What experiments measure: fluctuations and response” |
| 6 | Inverse quadratic matrix, symmetric density spectrum, singular limits, response propagator, source vertex and normalized retarded density susceptibility | “What experiments measure”; “Supplemental derivation: fix the response normalization” |

Supplements: telegrapher equation, explicit elimination of imbalance, equal-time covariance and classical FDT, source units, solved exercises. Correction: the source's small-k nonhydrodynamic annotation writes a gap α; its own exact two-species matrix gives 2α. The chapter uses the exact result. Bare response-field propagator is distinguished from physical susceptibility, including its σk² vertex.

## Lecture 7 — Navier–Stokes equations (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture7.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | Fluid conserved N,P,E and angular momentum, first law including volume and momentum | `07-navier-stokes.qmd`, “The slow variables of a fluid”; “Thermodynamics with momentum” |
| 2 | Density first law, Gibbs–Duhem, entropy weight and conjugates, parity, response fields and current-based Hamiltonian | “Thermodynamics with momentum”; “Ideal constitutive relations” |
| 3 | Rotation-invariant ideal A,B,C,D ansatz, time-reversal/divergence constraint, expansion in thermal conjugate variables | “Ideal constitutive relations”; supplemental divergence verification |
| 4 | B,D as pressure derivatives, identification C=P, ideal currents, general dissipative motifs | “Ideal constitutive relations”; “Dissipation as a positive matrix” |
| 5 | Shear/bulk viscosity tensor and positivity, thermoelectric matrix, velocity-dependent mixed rank-four tensors, simplified NS currents and Onsager reciprocity | “Dissipation as a positive matrix”; “The resulting Navier–Stokes constitutive equations” |
| 6 | Generic transport-matrix notation, deterministic EOM, entropy current, local entropy production, positivity from noise | “Supplemental derivation: the local second law” |

Supplements: correct role of fixed conserved sectors in entropy weight, explicit heat/particle transport matrix and determinant bound, shear worked example, solved exercises. Mixed scalar/momentum transport is explicitly described and its isotropic tensor decomposition retained; as in the source it is set to zero only in the simplified displayed NS currents.

## Lecture 8 — Galilean invariance (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture8.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | Conserved fluid densities recap, rotational invariance and angular-momentum derivative | `08-galilean.qmd`, “Angular momentum makes the stress symmetric” |
| 2 | Momentum equals mass current, pressure boost constraint, rest-frame equation of state, kinetic energy split, ideal currents | “Boost symmetry relates mass current and momentum” |
| 3 | Allowed boost-invariant dissipative combinations, shear/bulk/heat motifs, full simple-fluid NS currents | “Dissipation must also respect boosts” |
| 4 | Convective derivative, linearized density/energy/momentum equations, transverse shear mode | “The material derivative”; “Linearize around equilibrium”; “Shear diffusion” |
| 5 | Longitudinal matrix, leading sound speeds, adiabatic derivative, attenuation, third pressure-free mode | “Sound and its thermodynamic speed”; supplemental attenuation derivation; “The third mode” |
| 6 | Thermal/incoherent diffusion eigenvector, full thermal diffusivity, liquid heat-capacity approximation | “The third mode: thermal or incoherent diffusion” |

Supplements: mass versus particle-density convention, explicit response-gradient placement preserving conservation, full attenuation derivation, standard heat-capacity form, complete mode counting and solved exercises. Correction: the handwritten thermal sound-attenuation prefactor is not general for P(ρ,ε). The book derives Γ_s=η_L/(2ρ₀)+κ P_ε[T_ρ+(w₀/ρ₀)T_ε]/(2c_s²) directly from the source's full linearized matrix and explains this correction. The viscosity, sound speed, and thermal diffusivity agree with that matrix.

## Lecture 9 — Shock and rarefaction waves (6 pages)

Source: <https://www.alucasphys.com/p7810s2026/p7810s2026_lecture9.pdf>

| PDF page | Inspected topics | Book correspondence |
|---|---|---|
| 1 | Linear sound, nonlinear Riemann step setup, ideal/no-energy-equation simplification, split-wave linear limit | `09-shocks.qmd`, “A step disturbance beyond linear sound” |
| 2 | Shock versus rarefaction, shock-frame mass/momentum matching, degree-of-freedom counting, ξ=x/t ansatz | “Shock waves”; “Rarefaction waves” |
| 3 | Self-similar mass/momentum equations, zero determinant and local sound speed, fan matching and free parameters | “Rarefaction waves: a continuous expanding fan” |
| 4 | Need for two-wave patterns RR/RS/SR/SS, nonunique weak solutions, second-law selection, viscosity negligible in late fan but essential inside shock, width estimate | “Entropy selects the physical weak solution”; supplemental shock thickness |
| 5 | P=Aρ^γ, high-to-low density initial step at rest, rarefaction velocity/density profile and edge matching, central state, shock speed | “Worked construction: a polytropic pressure law” |
| 6 | Nonlinear shock matching equation, γ=5/3 numerical trend of shock Mach number versus density contrast | Same worked construction, explicit matched numerical example |

Supplements: integrated Rankine–Hugoniot derivation, characteristic invariants, Lax/compressive interpretation for the worked example, one-scalar bracketed matching algorithm, and solved exercises. Corrections/limits: the source's inverse-viscosity shock-width scaling is inconsistent with its own entropy-production balance; the book derives ℓ∝η_L/(ρΔv). The source neglects energy conservation: its fixed-A polytropic jump is explicitly identified as a barotropic two-equation model rather than a complete thermodynamic ideal-gas shock. Entropy selection is distinguished from uniqueness of unrestricted weak solutions.

## Reading limitations and editorial policy

All pages in this range were readable at rendered full-page resolution, and no scientific section was omitted because it was unreadable. Some handwritten shorthand suppresses temperature factors, operator ordering, Fourier normalizations, or held-fixed derivative variables. The book supplies a consistent explicit convention and explains the consequential corrections above. This is comprehensive topic coverage, not a claim that every handwritten algebraic intermediate, sketch, historical administrative sentence, or literal sentence has been reproduced. Sources remain linked for side-by-side study.
