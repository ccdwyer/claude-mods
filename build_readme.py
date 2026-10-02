#!/usr/bin/env python3
"""build_readme.py: regenerate README.md from mods.json. Embeds each mod's demo GIF only once it exists in that mod's repo."""
import json, subprocess

GROUPS = ['Guardrails', 'Feedback loops', 'Workflow', 'Visuals', 'Fun']
mods = json.load(open('mods.json'))
listed = {p['name'] for p in json.load(open('.claude-plugin/marketplace.json'))['plugins']}
mods = [m for m in mods if m['name'] in listed]

def has_demo(name):
    r = subprocess.run(['gh', 'api', f'repos/ccdwyer/{name}/contents/media/demo.gif', '--silent'], capture_output=True)
    return r.returncode == 0

raw = lambda n, f: f'https://github.com/ccdwyer/{n}/raw/main/media/{f}'
anchor = lambda t: t.lower().replace(' ', '-')
out = ['# ccdwyer-mods', '',
       f'{len(mods)} [Claude Code mods](https://claude.dev/blog/getting-started-with-claude-code-mods/): plugins of function hooks that change what Claude Code does and draw UI inside it. Each mod lives in its own repo; this repo is the marketplace that lists them all.', '',
       '## Install', '', 'All of them (needs the `claude` CLI on your PATH):', '',
       '```sh', 'curl -fsSL https://raw.githubusercontent.com/ccdwyer/claude-mods/main/install.sh | sh', '```', '',
       'Or from inside Claude Code, add the marketplace once, then install whichever mods you want (commands are under each mod below):', '',
       '```', '/plugin marketplace add ccdwyer/claude-mods', '/plugin install <mod>@ccdwyer-mods', '/reload-plugins', '```', '',
       '## Contents', '']
for g in GROUPS:
    items = [m for m in mods if m['group'] == g]
    if items:
        out.append(f'- **{g}:** ' + ' · '.join(f"[{m['title']}](#{anchor(m['title'])})" for m in items))
out.append('')
for g in GROUPS:
    items = [m for m in mods if m['group'] == g]
    if not items:
        continue
    out += [f'## {g}', '']
    for m in items:
        n, t = m['name'], m['title']
        out += [f'### {t}', '', m['blurb'], '']
        if has_demo(n):
            links = [f"[Watch the MP4](https://github.com/ccdwyer/claude-mods/raw/main/media/{n}.mp4)"]
            if m.get('screenshot'):
                links.append(f"[Screenshot]({raw(n, m['screenshot'])})")
            out += [f"![{t} demo]({raw(n, 'demo.gif')})", '', ' · '.join(links + [f'[Repo](https://github.com/ccdwyer/{n})']), '']
        else:
            out += [f'*Demo recording coming soon.* · [Repo](https://github.com/ccdwyer/{n})', '']
        out += ['```', f'/plugin install {n}@ccdwyer-mods', '```', '']
out += ['---', '', "Every mod is validated, type-checked and tested with `claude plugin test`, and went through review rounds with GPT-6-Astra and Grok 4.7. Each repo's README lists what it does not cover.", '']
open('README.md', 'w').write('\n'.join(out))
print(f'README: {len(mods)} mods')
