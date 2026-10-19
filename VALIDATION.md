# Validation record — 19 October 2026

Built with Quarto 1.10.18 and LuaLaTeX (TeX Live 2023). The final `quarto render` completed successfully for HTML and PDF, without unresolved-reference or missing-citation diagnostics.

- 28 lecture companions, plus foundations and study tools: 33 HTML pages.
- Combined PDF: `_site/hydrodynamics.pdf`, 146 A4 pages.
- All 28 source PDF checksums verified; 172 source pages visually inspected and mapped in `coverage/`.
- `python3 scripts/check_book.py`: 453 unique content labels, 106 source cross-references, and 2,700 local links/anchors checked after the attribution update. Lecture numbers match chapter numbers; source-page maps include every PDF page. Quarto's deliberately repeated alternate-theme stylesheet IDs are excluded from content-anchor duplication checks.
- Search index contains both introductory and advanced topics. Representative served HTML pages and the PDF were checked against the final files byte for byte. The external MathJax script responded successfully.
- `git diff --check`, Python compilation, and Node syntax checks passed.
- Interactive plotting handlers were exercised in a DOM stub at zero time, large diffusion width, zero wave number, pole merger, propagating poles, and capillary crossover endpoints. Redraws produced finite SVG paths.
- PDF pages inspected visually: title, contents, foundations, stochastic calculus, Galilean constitutive equations, anisotropic fluids, mixed-state symmetry, MHD, and laboratory plots. Revised contents and figure layouts were inspected again after the last build.

The chapters received independent mathematical consistency passes in addition to source inspection. Specific source-convention corrections and qualifications are recorded in the lecture audits. The exact kinetic resolvent in Lecture 23 was additionally compared with direct numerical matrix inversion.

The attribution update was rebuilt in both formats with the companion's author field left blank. Andrew Lucas is acknowledged for his source lectures in the page footers, title-page source note, and acknowledgments, without assigning him authorship or responsibility for this companion. Author bylines, ORCID, and affiliations were removed and checked across the source, rendered HTML, search index, and PDF. The revised title page, opening acknowledgments, and source-guide acknowledgments were inspected visually in the PDF. Supplemental material is distinguished from Lucas' original lectures.

## Verification limits

Live browser automation was unavailable: no browser surface was connected and the in-app browser could not be created. Responsive layout, visual light/dark behavior, search interaction, and rendered MathJax therefore still warrant a live browser check. HTTP, source structure, asset availability, event-handler execution, and PDF rendering were checked directly; these do not substitute for that browser check.

The GitHub Actions deployment workflow is prepared but has not run on GitHub. No remote repository or hosted deployment was created. The README gives the later publication steps. The scientific text is an editable first edition, not an externally peer-reviewed textbook.
