#!/usr/bin/env python3
"""add.py <mod-name>: add or refresh one mod in the marketplace from its GitHub repo's plugin.json."""
import json, subprocess, sys, base64
name = sys.argv[1]
raw = subprocess.check_output(['gh', 'api', f'repos/ccdwyer/{name}/contents/.claude-plugin/plugin.json', '-q', '.content'])
manifest = json.loads(base64.b64decode(raw))
path = '.claude-plugin/marketplace.json'
market = json.load(open(path))
entry = {'name': name, 'source': {'source': 'github', 'repo': f'ccdwyer/{name}'}, 'description': manifest['description']}
market['plugins'] = [p for p in market['plugins'] if p['name'] != name] + [entry]
json.dump(market, open(path, 'w'), indent=2); open(path, 'a').write('\n')

# Regenerate the README table from the marketplace.
rows = ['| Mod | What it does | Install |', '|---|---|---|']
for p in market['plugins']:
    rows.append(f"| [{p['name']}](https://github.com/{p['source']['repo']}) | {p['description']} | `/plugin install {p['name']}@ccdwyer-mods` |")
readme = open('README.md').read()
start, end = '<!-- mods:start -->', '<!-- mods:end -->'
head, rest = readme.split(start)
_, tail = rest.split(end)
open('README.md', 'w').write(head + start + '\n' + '\n'.join(rows) + '\n' + end + tail)

# Keep install.sh's mod list in sync.
import re as _re
names=' '.join(p['name'] for p in market['plugins'])
sh=open('install.sh').read()
sh=_re.sub(r'^MODS=".*"$', f'MODS="{names}"', sh, flags=_re.M)
sh=_re.sub(r'case " .* " in', f'case " {names} " in', sh)
open('install.sh','w').write(sh)
