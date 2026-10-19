# Hydrodynamics — a graduate study companion

**Original course and lecture notes: Andrew Lucas, University of Colorado Boulder.** This web book is an unofficial study companion to his [Hydrodynamics course, PHYS 7810, Spring 2026](https://www.alucasphys.com/s2026.html), following all 28 lectures.

## Attribution and acknowledgments

All credit for the original course and lecture material belongs to **Andrew Lucas**. This project gratefully acknowledges his work in developing the lectures and making his handwritten notes publicly available. The original notes are the authoritative source for the course; readers should cite them when referring to the lecture material.

This repository is an unofficial reading aid and claims no original scientific contribution. The author field of this companion is left blank. Andrew Lucas is acknowledged solely as the author of the original lectures; he is not the author of this companion and is not responsible for its contents. No review or endorsement by him is implied. Supplemental explanations, derivations, exercises, and illustrations are additions to the lectures, and any errors in them should not be attributed to him.

The companion includes foundations, worked derivations, solved exercises, an interactive laboratory, source-page coverage records, and a combined PDF. See [NOTICE.md](NOTICE.md) for attribution and [the source guide](sources.qmd) for the original lecture links.

The initial edition builds to 33 web pages and a 146-page PDF. See [VALIDATION.md](VALIDATION.md) for the completed checks and the remaining live-browser verification limit.

## Read and build locally

Install [Quarto](https://quarto.org/docs/get-started/) (tested with 1.10.18). For PDF output, install a TeX distribution, or run `quarto install tinytex` once.

```sh
quarto render                       # All HTML chapters + _site/hydrodynamics.pdf
python3 scripts/check_book.py        # Check rendered links, anchors, labels, and coverage
quarto preview --no-browser          # Prints the local preview URL
```

For a faster content pass use `quarto render --to html --no-clean`; it preserves the existing PDF without regenerating it. For a static preview of the completed build, use `python3 -m http.server 8246 --directory _site` and visit `http://localhost:8246`. Browser scripts and navigation should be checked over HTTP. MathJax is loaded from a CDN by Quarto, so the HTML math renderer requires internet on first load; the PDF is self-contained for offline reading.

## Files you will edit

- `01-*.qmd` through `28-*.qmd`: one chapter per lecture. The filename prefix preserves Lucas' lecture number; the book's displayed chapter numbering counts lecture chapters only.
- `prerequisites.qmd`, `notation.qmd`, `laboratory.qmd`: graduate-level study support.
- `_quarto.yml`: chapter order, six thematic parts, navigation, HTML and PDF options.
- `assets/`: themes, browser scripts, APS citation style, bibliography, and math macros. Keep macro definitions equivalent in `macros.sty` and `mathjax-config.html`.
- `coverage/`: a page-by-page topic map from the inspected source PDFs to the explanations here, including interpretation notes. `source-manifest.json` pins PDF checksums and page counts.
- `figs/`: exported figures; `julia --startup-file=no scripts/figures.jl` regenerates the original analytic illustrations using Julia, CairoMakie, and Inkscape (for the cover SVG-to-PDF export). The exported files are committed, so readers and CI do not need these figure-generation tools.
- `scripts/check_book.py`: dependency-free structural and local-link checks.

Temporary original PDFs, rendered source images, generated site files, and Quarto caches are ignored by Git. The source PDFs are linked to the author's website and are not redistributed. `scripts/source_manifest.py --fetch` optionally re-downloads and verifies the pinned source versions. Normal builds do not download them.

## Publish to GitHub Pages later

The repository is local on branch `main`; no remote is configured and no site has been published.

1. Create an empty repository on GitHub.
2. Add its SSH or HTTPS URL as `origin`, then push:

   ```sh
   git remote add origin <YOUR_REPOSITORY_URL>
   git push -u origin main
   ```

3. In the repository's **Settings → Pages**, set **Source** to **GitHub Actions**. If the first run started before this setting was enabled, rerun the workflow.
4. Run **Build and publish the web book** in the Actions tab, or push another commit. The workflow builds both formats, checks local links, and deploys `_site`. The Pages environment reports the published URL.

All page and asset links are relative, so the same build works at `username.github.io/repository/` and at a user-site root. No custom domain or account-specific URL is hard-coded. The workflow follows the official [GitHub custom Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and [Quarto setup action](https://github.com/quarto-dev/quarto-actions/tree/main/setup) documentation.

To version an edit:

```sh
git add <CHANGED_FILES>
git commit -m "Explain the derivation of ..."
git push
```

## Scientific and editorial conventions

Equations use native Quarto labels, e.g. `{#eq-l05-diffusion}`, and references such as `@eq-l05-diffusion`. Lecture numbers, source links, assumptions, and distinctions between exact results, approximations, and empirical statements belong in the chapter. New supplements should be marked as supplements. Do not silently import a different Fourier sign, noise normalization, stress convention, or electromagnetic unit system.

The accompanying explanations were checked against all source pages. This is an editable first edition; the coverage records document the audit and specific interpretive choices rather than asserting an external scientific peer review. Credit for the original lectures belongs to Andrew Lucas; the supplemental text does not imply his authorship, approval, or responsibility for this companion.
