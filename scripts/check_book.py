#!/usr/bin/env python3
"""Check the built book's local links, anchors, references, and source coverage."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
errors = []

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids, self.links = set(), []
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if 'id' in a:
            # Quarto intentionally repeats IDs across alternate theme stylesheets.
            theme_link = (tag == 'link' and a['id'] in
                          {'quarto-text-highlighting-styles', 'quarto-bootstrap'}
                          and 'quarto-color-scheme' in a.get('class', ''))
            if a['id'] in self.ids and not theme_link:
                errors.append(f'Duplicate HTML id: {a["id"]}')
            self.ids.add(a['id'])
        if tag == 'a' and a.get('name'):
            self.ids.add(a['name'])
        for key in ('href', 'src', 'poster'):
            if a.get(key):
                self.links.append(a[key])

chapters = re.findall(r'^\s*-\s+([\w-]+\.qmd)\s*$', (ROOT / '_quarto.yml').read_text(), re.M)
labels = {}
refs = []
for name in chapters:
    path = ROOT / name
    if not path.exists():
        errors.append(f'Missing chapter {name}')
        continue
    text = path.read_text()
    for label in re.findall(r'\{[^}\n]*#((?:eq|sec|fig|tbl)-[\w-]+)[^}\n]*\}', text):
        if label in labels:
            errors.append(f'Duplicate label {label} in {name} and {labels[label]}')
        labels[label] = name
    refs += [(name, r) for r in re.findall(r'@((?:eq|sec|fig|tbl)-[\w-]+)', text)]
    if re.search(r'\b(?:TODO|TBD|FIXME|lorem ipsum)\b', text, re.I):
        errors.append(f'Unfinished placeholder in {name}')
    if not (SITE / path.with_suffix('.html').name).exists():
        errors.append(f'Missing rendered chapter {name}')
for name, ref in refs:
    if ref not in labels:
        errors.append(f'Unresolved source reference @{ref} in {name}')

lecture_files = sorted(p for p in ROOT.glob('[0-9][0-9]-*.qmd'))
if len(lecture_files) != 28:
    errors.append(f'Expected 28 lecture chapters, found {len(lecture_files)}')
for n, p in enumerate(lecture_files, 1):
    if not p.name.startswith(f'{n:02}-'):
        errors.append(f'Lecture sequence mismatch: {p.name}')
    if f'p7810s2026_lecture{n}.pdf' not in p.read_text():
        errors.append(f'Missing original lecture link in {p.name}')

manifest = json.loads((ROOT / 'coverage/source-manifest.json').read_text())
if [e['lecture'] for e in manifest['lectures']] != list(range(1, 29)):
    errors.append('Source manifest must contain all lectures in sequence')
for name in ('lectures-01-09.md', 'lectures-10-18.md', 'lectures-19-28.md'):
    audit_path = ROOT / 'coverage' / name
    if not audit_path.is_file():
        errors.append(f'Missing source coverage audit {name}')
        continue
    sections = re.split(r'^## Lecture (\d+)[^\n]*\n', audit_path.read_text(), flags=re.M)
    for i in range(1, len(sections), 2):
        n = int(sections[i])
        pages = [int(p) for p in re.findall(r'^\|\s*(\d+)\s*\|', sections[i+1], re.M)]
        expected = list(range(1, manifest['lectures'][n-1]['pages'] + 1))
        if pages != expected:
            errors.append(f'Incomplete source-page map for lecture {n}: {pages}, expected {expected}')

documents = {}
for path in SITE.rglob('*.html'):
    source = path.read_text()
    documents[path.resolve()] = Document(source)
    if re.search(r'class="[^"]*quarto-unresolved-ref', source) or 'citation-not-found' in source:
        errors.append(f'Unresolved rendered reference in {path.relative_to(SITE)}')
for n, path in enumerate(lecture_files, 1):
    rendered = SITE / path.with_suffix('.html').name
    if rendered.is_file():
        heading = re.search(r'<h1\b[^>]*class="title"[^>]*>(.*?)</h1>', rendered.read_text(), re.S)
        if not heading or not re.search(rf'class="chapter-number">{n}</span>', heading[1]):
            errors.append(f'Incorrect displayed chapter number in {rendered.name}')

link_count = 0
for path, document in documents.items():
    for url in document.links:
        u = urlsplit(url)
        if u.scheme or u.netloc:
            continue
        if u.path.startswith('/'):
            errors.append(f'Root-relative URL will break under a repository path: {path.name}: {url}')
            continue
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'Broken link in {path.name}: {url}')
        elif u.fragment and target.suffix == '.html' and target in documents:
            if unquote(u.fragment) not in documents[target].ids:
                errors.append(f'Missing anchor in {path.name}: {url}')
        link_count += 1
if not (SITE / 'hydrodynamics.pdf').is_file():
    errors.append('Missing combined PDF: _site/hydrodynamics.pdf')

if errors:
    raise SystemExit('\n'.join(dict.fromkeys(errors)))
print(f'PASS: {len(chapters)} chapters, {len(labels)} labels, {len(refs)} cross-references, '
      f'{len(documents)} HTML documents, {link_count} local links/anchors; 28-source manifest and PDF present.')
