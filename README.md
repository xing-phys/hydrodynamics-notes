# Hydrodynamics — a graduate study companion

An independent web book following all 28 lectures in [Andrew Lucas' PHYS 7810, Spring 2026](https://www.alucasphys.com/s2026.html). Includes foundations, original explanations, worked derivations, solved exercises, an interactive laboratory, source-page coverage records, and a combined PDF. This is companion material, not an authorized edition of Lucas' notes.

## Read and build locally

Install [Quarto](https://quarto.org/docs/get-started/) (tested with 1.10.18). For PDF output, install a TeX distribution, or run `quarto install tinytex` once.

```sh
quarto render                       # All HTML chapters + _site/hydrodynamics.pdf
python3 scripts/check_book.py        # Check rendered links, anchors, labels, and coverage
quarto preview --no-browser          # Prints the local preview URL
```

For a faster content pass use `quarto render --to html`; it does not regenerate the PDF. For a static preview of the completed build, use `python3 -m http.server 8246 --directory _site` and visit `http://localhost:8246`. Browser scripts and navigation should be checked over HTTP. MathJax is loaded from a CDN by Quarto, so the HTML math renderer requires internet on first load; the PDF is self-contained for offline reading.

## Files you will edit

- `01-*.qmd` through `28-*.qmd`: one chapter per lecture. The filename prefix preserves Lucas' lecture number; the book's displayed chapter numbering counts lecture chapters only.
- `prerequisites.qmd`, `notation.qmd`, `laboratory.qmd`: graduate-level study support.
- `_quarto.yml`: chapter order, six thematic parts, navigation, HTML and PDF options.
- `assets/`: themes, browser scripts, APS citation style, bibliography, and math macros. Keep macro definitions equivalent in `macros.sty` and `mathjax-config.html`.
- `coverage/`: a page-by-page topic map from the inspected source PDFs to the explanations here, including interpretation notes. `source-manifest.json` pins PDF checksums and page counts.
- `figs/`: exported figures; `scripts/figures.jl` regenerates the original analytic illustrations using Julia and CairoMakie. The exported files are committed, so readers and CI do not need Julia.
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

The accompanying explanations were drafted with AI assistance and checked against all source pages. This is an editable first edition; the coverage records document the audit and specific interpretive choices rather than asserting an external scientific peer review. Original lecture authorship remains with Andrew Lucas. See `NOTICE.md` for attribution.
