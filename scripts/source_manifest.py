#!/usr/bin/env python3
"""Record or verify source PDFs without adding them to the repository."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'coverage/source-manifest.json'
CACHE = ROOT / '.cache/sources'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', action='store_true', help='Record all cached PDFs as a new source snapshot')
    parser.add_argument('--fetch', action='store_true', help='Fetch missing PDFs and verify the pinned checksums')
    args = parser.parse_args()
    if args.record:
        entries = []
        for n in range(1, 29):
            path = CACHE / f'lecture-{n:02}.pdf'
            info = subprocess.check_output(['pdfinfo', str(path)], text=True)
            entries.append({
                'lecture': n,
                'url': f'https://www.alucasphys.com/p7810s2026/p7810s2026_lecture{n}.pdf',
                'cache_file': str(path.relative_to(ROOT)),
                'pages': int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1]),
                'sha256': digest(path),
            })
        data = {'course_url': 'https://www.alucasphys.com/s2026.html',
                'retrieved_on': '2026-10-19', 'lectures': entries}
        MANIFEST.write_text(json.dumps(data, indent=2) + '\n')
        print(f'Recorded {len(entries)} PDFs, {sum(e["pages"] for e in entries)} pages.')
        return
    data = json.loads(MANIFEST.read_text())
    CACHE.mkdir(parents=True, exist_ok=True)
    count = 0
    for entry in data['lectures']:
        path = ROOT / entry['cache_file']
        if args.fetch and not path.exists():
            request = urllib.request.Request(entry['url'], headers={'User-Agent': 'HydrodynamicsStudyCompanion/1.0'})
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read()
            if not payload.startswith(b'%PDF-'):
                raise SystemExit(f'Source is not a PDF: {entry["url"]}')
            path.write_bytes(payload)
        if not path.exists():
            raise SystemExit(f'Missing {path}; use --fetch to download originals.')
        if digest(path) != entry['sha256']:
            raise SystemExit(f'Source changed: lecture {entry["lecture"]}. Review it before updating the snapshot.')
        count += 1
    print(f'Verified {count} source PDF checksums.')

if __name__ == '__main__':
    main()
