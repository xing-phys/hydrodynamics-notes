# Source audit: lectures 19–28

Prepared after visual inspection of **every page** of all ten source PDFs, downloaded from the links on Andrew Lucas's PHYS 7810 Spring 2026 course page. The sources are handwritten image scans; PDF text extraction is not a substitute for the visual audit. Local ignored audit material is `.cache/sources/lecture-NN.pdf` and `.cache/pages/NN/` (rendered at 1400-pixel maximum dimension, contact sheet plus individual pages). Detailed pages were enlarged separately where tensor formulas or sign conventions needed checking.

This is a topic-coverage audit, not a claim that the prose transcribes or reproduces the original notes. Chapters provide independent explanatory derivations, adopt stated notation, and identify model assumptions and clarifications below.

## Lecture 19: Fluids with modified spacetime symmetries (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Reduced spacetime symmetry; conserved density/momentum MSR action; generalized time reversal using orthogonal A; entropy-current/divergence constraint | Which parts of fluid mechanics come from symmetry? |
| 2 | Generated ideal currents and stress; Galilean check; derivative corrections; aligned cylindrical particles and their symmetries | Which parts…; Aligned rods |
| 3 | δ and axis projector invariants; no invariant directed axis; ideal vector with two functions; nonsymmetric xz stress; dissipative scalar conductivity and viscosity motifs; time-reversal restriction on cross terms | Aligned rods |
| 4 | Full uniaxial viscosity tensor; extra pair equalities and positivity example; planar combined reflection/time reversal; exclusion of an ideal epsilon term | Aligned rods; A two-dimensional fluid… |
| 5 | Hall conductivity; nondissipative antisymmetric coefficient; Hall-viscosity tensor and angular-momentum restriction; examples of chiral/electronic/active matter | A two-dimensional fluid…; introductory applications |
| 6 | Hall force absorbed into pressure for incompressible constant coefficients; Poiseuille profile; transverse pressure difference | Supplementary worked example |

Clarifications: component/flux stress indices are fixed consistently as `∂t g_i+∂j τ_ij=0`; generated stress is `τ_ij=∂S_j/∂v_i`. Raw tensor-coefficient positivity is replaced by positivity of defined projected quadratic-form blocks. The handwritten additional pair equalities are not presented as consequences of uniaxial covariance alone, because stress symmetry/angular-momentum assumptions matter. The Hall pressure sign is fixed by explicitly stated epsilon and vorticity conventions.

## Lecture 20: BBGKY hierarchy (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Scope of weakly interacting kinetic theory; N-particle Hamiltonian; canonical variables and Poisson bracket | From trajectories to a distribution |
| 2 | Liouville continuity equation; one-particle density; phase-space moments; permutation symmetry; reduced s-particle distribution and normalization | From trajectories…; Reduced distributions |
| 3 | Integrating Liouville; first exact hierarchy equation; streaming vs collision term; general hierarchy | Reduced distributions; Why there is a hierarchy |
| 4 | Explicit pair equation; streaming/encounter/collision time scales; dilute condition; neglecting triples; relative coordinates | Why there is a hierarchy; The dilute-gas approximation |
| 5 | Separation into center and relative coordinates; integrating relative derivative; pre/post encounter distributions; molecular chaos; gain minus loss | The dilute-gas approximation; The collision integral |
| 6 | Scattering rate with energy/momentum delta functions; locality; full Boltzmann equation; bosonic stimulation and fermionic blocking | The collision integral |

Clarifications: the incoming-pair meaning of molecular chaos is emphasized; quantum occupation factors are additional quantum input rather than a derivation from classical Liouville evolution. A supplementary equal-mass 1D example explains why generic thermalization is not guaranteed by the one-dimensional pedagogical hierarchy.

## Lecture 21: Boltzmann equation (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Streaming plus binary collision operator; scattering rates and elastic conservation | Reversible streaming and irreversible collisions |
| 2 | Classical H theorem; streaming boundary term; rate reversibility; incoming/outgoing symmetrization | Entropy production |
| 3 | Positivity of `(X−Y)(log X−log Y)`; collision invariants; Maxwell, Bose, and Fermi equilibria | Entropy production; Equilibrium… |
| 4 | Quantum entropy; moments of collision invariants; local equilibrium and ideal hydrodynamic limit | Equilibrium…; Taking moments |
| 5 | Local equilibrium vs nonhydrodynamic distortion; density, momentum, energy and currents; Gaussian ideal-gas density and current | Taking moments; Supplementary derivation |
| 6 | Ideal stress, ideal gas law, kinetic/internal energy split, enthalpy energy current | Supplementary derivation |

Clarifications: reversibility and boundary hypotheses are explicit; genericity of the collision-invariant space is an assumption; local equilibrium makes the collision term zero, not the full streaming operator. Quantum entropy is written with one checked Bose/Fermi sign convention.

## Lecture 22: Hydrodynamics from kinetic theory (7 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Linearization via an energy-like perturbation around equilibrium; classical and quantum possibility | Linearizing the distribution |
| 2 | Linearized collision operator; hydrodynamic and fast functions; weighted inner product; positive quadratic form | Linearizing…; Why conserved densities are slow |
| 3 | Null space; stability/eigenvalues; conserved modes; hydrodynamic vs fast poles | Why conserved densities are slow |
| 4 | Slow/fast block decomposition; elimination of fast block; order-k² damping; interpretation of density moments | Eliminating the fast sector; Susceptibilities… |
| 5 | Number-energy nonorthogonal susceptibilities; Gaussian values; thermodynamic metric; ideal particle equation; traceless stress split and pressure | Susceptibilities…; Ideal equations… |
| 6 | Viscosity as a fast-space inverse matrix element; general dissipative coefficients; vanishing bulk viscosity in the monatomic model; relaxation-time eta=P tau | Ideal equations…; Relaxation time… |
| 7 | Weak interactions imply large kinetic viscosity; limitations and preview of ballistic crossover | Relaxation time… |

Clarifications: the inverse is restricted to the nonconserved subspace. A nonorthogonal-basis projector is supplied explicitly. The zero bulk viscosity is model dependent, and the hydrodynamic limit must be taken before interpreting tau→infinity.

## Lecture 23: Ballistic-to-viscous crossover (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Projected Boltzmann operator; inverse-collision transport problem | How can an inverse collision operator be calculated? |
| 2 | Chapman–Enskog variational principle; finite-dimensional derivation; trial basis and symmetry; shear-viscosity lower bound | How can… |
| 3 | Current matrix elements and projection; collision-controlled hydro/ballistic regimes; 1D massless model; conserving relaxation operator | A controlled breakdown…; A solvable… |
| 4 | Kinetic correlation resolvent; finite-rank Dyson sum; orthonormal slow basis; norms | A solvable…; Supplementary derivation |
| 5 | Full projected free resolvent matrix; density response expression; sound and diffusive/relaxing poles; exact energy–momentum closure | Supplementary derivation; Following the modes |
| 6 | Incoherent density diffusion; mode collision/crossover; other fast paired modes; higher-dimensional shear and sound attenuation | Following the modes |

Clarifications: phase-space measure is explicitly `∫dp` in the 1D model. The density-resolvent numerator sign is corrected relative to the handwritten first term by requiring the exact k=0 conservation limit Rnn=i chi/omega. The displayed kinetic density resolvent is distinguished from a retarded susceptibility, which requires the source/static factors. Poles must have nonzero residues to be visible in an observable. The undamped sound is a special property of the model and not generic 1D thermalization.

## Lecture 24: Superfluids (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Spontaneous symmetry breaking; liquid vs solid motivation; global U(1) density; nonlinear Schrodinger model | A broken symmetry adds a slow field |
| 2 | Density-phase variables; gradient energy and canonical bracket; normal redundant phase shift vs superfluid stiffness; ideal Josephson/density equations | A broken symmetry…; Stiffness… |
| 3 | Illustrative quartic-potential phase selection; stiffness vs density; entropy/MSR construction and two dissipative coefficients | Stiffness…; Dissipation… |
| 4 | Integrating density; phase sound; dissipative sound attenuation; normal limit; finite-temperature ordering question | Supplementary derivation; Dissipation…; Thermal phase fluctuations |
| 5 | Order diagnosed by correlations; ferromagnet analogy; Gaussian inverse Laplacian and dimensional infrared behavior | Thermal phase fluctuations |
| 6 | Vortex phase and core; logarithmic energy; placement entropy; BKT free-energy estimate; bound pairs and algebraic order | Vortices and the BKT estimate |

Clarifications: the source's informal absence-of-superfluidity language for d≤2 is sharpened to absence of true continuous-symmetry long-range order at nonzero T for short-range systems. Two-dimensional finite-stiffness BKT superfluidity remains possible. The transition stiffness in the universal relation is renormalized, not generally the bare Hamiltonian parameter. Quantum pressure remains relevant at cores.

## Lecture 25: Superfluids with energy and momentum (5 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Entropy functional including phase gradient at leading order; conjugates; thermal time-reversal shifts | What are the two fluids? |
| 2 | MSR ideal-current divergence condition; rotational ansatz for mass, energy and stress; coefficient matching | Constitutive relations… |
| 3 | Integrability of phase gradient; thermodynamic coefficient identities; Josephson equation; superfluid and normal density; Landau–Tisza interpretation | Constitutive relations… |
| 4 | Linear density/energy/phase/momentum equations; entropy equation; small thermal expansion approximation; first/second sound and polarization | Linearized equations…; Supplementary derivation |
| 5 | Low-normal-density limitation and pure-superfluid limit; ordinary dissipative terms; extra superfluid diagonal/cross bulk coefficients; matrix positivity | Supplementary derivation; Dissipation and positivity |

Notation issue requiring care: page 3 writes a minus superfluid term in the current with its intermediate u variable, while page 4 uses a plus term in linear density continuity. Rather than propagate ambiguous phase/chemical-potential signs, the companion fixes the physical convention J=rho_n v_n+rho_s v_s and v_s=grad(theta) throughout. It derives sound using the conserved total momentum, entropy density (not entropy per mass), and explicitly defined heat capacity. The decoupled sound formulas are identified as approximations, not general eigenvalues. No unresolved numerical claim is copied from the ambiguous intermediate notation.

## Lecture 26: Strong-to-weak spontaneous symmetry breaking (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Phase response as multiplier; eliminating density via Josephson; relabeling r/a fields; conserved/superfluid current in phase variables | From the MSR density action… |
| 2 | Quadratic doubled action; thermal reversal; normal spatial shift vs superfluid constant shift; two U(1)s; open-system interpretation | From the MSR…; Why the quantum contour… |
| 3 | Pure-state symmetry and long-range order; Z2 cat/GHZ example; reduced mixture and indistinguishability by few-body observables | Pure states, cats, and local order |
| 4 | Fixed-charge vs charge-fluctuating ensembles; local equivalence; strong/weak density-matrix definitions; U(1) verification | Strong and weak symmetry… |
| 5 | SWSSB interpretation of ensemble equivalence; strong/weak Goldstone fields; reservoir charge exchange; explicit strong breaking and a gapped density mode | Why revisit…; From the MSR…; Supplementary derivation |
| 6 | Forward/backward density-matrix contour; r/a fields; S[a=0]=0; Im S≥0; thermal imaginary-time leg; KMS origin of thermal time reversal and a subleading quantum correction | Why the quantum contour… |

Independent primary verification: https://doi.org/10.1103/PhysRevB.111.125147 and https://arxiv.org/html/2407.08760v2 were opened and checked. They identify authors, publication and the diffusion/SWSSB framework. The companion distinguishes the finite-matrix algebraic definition from thermodynamic spontaneous breaking and distinguishes global fixed-charge evolution from the local equilibrium description. It does not infer a literal loss of total-charge conservation from ensemble equivalence. r/a normalization factors are stated rather than mixed between conventions.

## Lecture 27: Higher-form symmetries (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Weighted conserved charges as response shifts; dipole conservation; second-derivative action | More conservation laws…; Dipole-conserving matter |
| 2 | k^4 subdiffusion; dipole-preserving lattice moves; row/column subsystem conservation | Dipole-conserving matter; Subsystem conservation |
| 3 | kx²ky² relaxation; vector charge; trace/symmetric/antisymmetric gradient sectors; trace-only flux-conserving example | Subsystem conservation; A conserved quantity… |
| 4 | Curl test fields and Biot–Savart/line-integral construction; antisymmetric-only sector; p-form antisymmetric current | A conserved quantity…; The geometry… |
| 5 | Surface charge proof; d=3 two-form dualization and curve charges; general d−p dimensional support; one-form stochastic diffusion action | The geometry…; Supplementary derivation |
| 6 | Vector diffusion equation; static longitudinal sector; diffusive transverse polarization | Supplementary derivation |

Clarifications: distinguishes higher-form symmetries from dipole/subsystem scalar conservation. Correct spatial charge-support dimension is d−p, with closed cycles and boundary qualifications. Frozen divergence of the extended spatial PDE is distinguished from the div b=0 condition in the full source-free antisymmetric-current conservation law and from dynamical transverse diffusion, and source geometrical illustrations are explained in those terms.

## Lecture 28: Magnetohydrodynamics (6 pages)

| Source page | Scientific content | Companion sections |
|---|---|---|
| 1 | Magnetic flux as one-form charge; Faraday/Gauss laws; Ohm and Ampere laws | Magnetic flux…; Magnetic diffusion… |
| 2 | One-form magnetic diffusion; coupling momentum; divergence constraint and surface deformations/translation charge issue; MSR formulation | Magnetic diffusion…; Magnetic flux…; Thermodynamic constraints… |
| 3 | Thermodynamic conjugates; modified divergence identity with constraint multiplier; generating-vector construction; ideal E and stress | Thermodynamic constraints… |
| 4 | Local rest electric field; quadratic energy and Maxwell stress; linearization; five-variable wave matrix | Thermodynamic constraints…; Supplementary derivation; Magnetic compression… |
| 5 | Zero/fast magnetic/Alfven eigenvalues and polarizations; resistive noise tensor; axisymmetric viscosity motifs | Magnetic compression…; Resistivity and viscosity… |
| 6 | Perspective: symmetry construction exposes transport terms absent from naive isotropic Maxwell-plus-Navier–Stokes | Resistivity and viscosity… |

Clarifications: displacement current is neglected only in the slow conducting regime. The five-variable matrix is explicitly identified as the pressureless magnetic-wave sector, not a generic compressible or incompressible MHD spectrum. A supplementary magnetosonic formula restores a finite sound speed. Positivity refers to the full viscosity quadratic form; Hall and additional transport require relaxing the specified field-reversal/reciprocity assumptions.
