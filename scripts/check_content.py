#!/usr/bin/env python3
"""Validate recipe coverage, local navigation and VideoWeb entry contracts."""
from pathlib import Path
import re
import json
import unicodedata
from urllib.parse import unquote
ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(ok, message):
    if not ok: errors.append(message)
def anchors(text):
    found=set(re.findall(r'<a\s+(?:name|id)=[\"\']([^\"\']+)', text))
    counts={}
    for heading in re.findall(r'^#{1,6}\s+(.+)', text, re.M):
        heading=re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading)
        heading=heading.replace('`','').replace('*','').lower()
        slug=''.join(c for c in heading if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ','-')
        n=counts.get(slug,0);counts[slug]=n+1
        found.add(slug+(f'-{n}' if n else ''))
    return found
recipes=list((ROOT/'prompts').glob('[0-9]*.md'))
ids=[]
for p in recipes: ids+=re.findall(r'^## ([A-Z]{3}-\d{3})\b',p.read_text(),re.M)
check(len(recipes)==24,f'Expected 24 categories, got {len(recipes)}')
check(len(ids)==84 and len(set(ids))==84,f'Expected 84 unique recipes, got {len(ids)}')
for p in ROOT.rglob('*.md'):
    text=p.read_text()
    links = re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
    links += re.findall(r'(?:src|href)=["\']([^"\']+)["\']', text)
    for url in links:
        if re.match(r'[a-zA-Z]+:',url): continue
        path,_,fragment=unquote(url).partition('#')
        target=(p.parent/path).resolve() if path else p
        check(target.exists(),f'{p.relative_to(ROOT)}: missing {url}')
        if target.is_file() and target.suffix=='.md' and fragment:
            check(fragment in anchors(target.read_text()),f'{p.relative_to(ROOT)}: missing anchor {url}')
for p in ROOT.glob('README*.md'):
    text=p.read_text()
    for url in ('https://videoweb.ai/model/minimax-h3/','https://videoweb.ai/free-minimax-h3/','https://videoweb.ai/affiliate-program/'):
        check(url in text,f'{p.name}: missing {url}')
    check('<details' not in text, f'{p.name}: homepage content must stay expanded')
    check('github.com/flaqai/' not in text,f'{p.name}: stale contribution link')
    check('https://flaq.ai/affiliate' not in text,f'{p.name}: wrong affiliate program')
check(len(list((ROOT/'assets').rglob('*.webp')))==12,'Expected 12 visual assets')
# Community examples are attributed external sources, not additional original recipes.
manifest=json.loads((ROOT/'docs/x-community-sources.json').read_text())
entries=manifest['entries']
showcase=(ROOT/'docs/x-community-showcase.md').read_text()
check(len(entries)==15, 'Expected 15 community examples')
check(len({e['id'] for e in entries})==len(entries), 'Duplicate community ID')
check(len({e['source_url'].rsplit('/',1)[-1] for e in entries})==len(entries), 'Duplicate X post ID')
check(len(list(ROOT.glob('README*.md')))==8, 'Expected eight README language entry pages')
for e in entries:
    for key in ('author','source_url','prompt_url','video_url','thumbnail_url','checked_at','retrieval_method','verification','rights','prompt_excerpt'):
        check(bool(e.get(key)), f"{e['id']}: missing {key}")
    check(e['id'].lower() in anchors(showcase), f"{e['id']}: missing showcase anchor")
    for key in ('source_url','prompt_url','video_url','thumbnail_url','prompt_excerpt'):
        check(e[key] in showcase, f"{e['id']}: showcase missing {key}")
    for p in ROOT.glob('README*.md'):
        check('#'+e['id'].lower() in p.read_text(), f"{p.name}: missing {e['id']}")
        check(e['thumbnail_url'] in p.read_text(), f"{p.name}: missing visible preview for {e['id']}")
# Warnings must remain visible before a reader opens the flashing clip.
notice_words = {'README.md': 'jump scare / flashing', 'README_zh.md': '惊吓与闪屏',
                'README_ja.md': '恐怖演出・点滅', 'README_ko.md': '공포·깜박임',
                'README_es.md': 'susto repentino y destellos', 'README_fr.md': 'sursaut et flashs',
                'README_de.md': 'Schreckmoment und Blitze', 'README_pt.md': 'susto repentino e flashes'}
for name, notice in notice_words.items():
    line = next((l for l in (ROOT/name).read_text().splitlines() if '#xh3-009)' in l), '')
    check(notice in line, f'{name}: missing XH3-009 playback notice')
for p in ROOT.glob('README*.md'):
    check(not re.search(r' · @[A-Za-z0-9_]+', p.read_text()), f'{p.name}: unlinked X author handle')
for p in recipes:
    for block in re.split(r'(?=^## [A-Z]{3}-\d{3}\b)', p.read_text(), flags=re.M)[1:]:
        recipe_id = re.match(r'## ([A-Z]{3}-\d{3})', block).group(1)
        statuses = re.findall(r'^\*\*Status:\*\* (.+)$', block, re.M)
        check(len(statuses) == 1 and statuses[0] in ('Concept — not independently tested', 'Tested'), f'{recipe_id}: missing or invalid status')
        check('```text' in block, f'{recipe_id}: missing copyable prompt block')
        if statuses == ['Tested']:
            record = re.search(r'^\*\*Generation record:\*\* \[[^\]]+\]\(([^)]+)\)', block, re.M)
            check(bool(record), f'{recipe_id}: tested recipe requires a generation record')
            if record:
                target = (p.parent / record.group(1)).resolve()
                check(target.is_relative_to(ROOT) and target.is_file() and target.suffix == '.md', f'{recipe_id}: generation record must be a local Markdown file')
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print('PASS: 84 recipes, 24 categories, local links/anchors, eight VideoWeb entry pages, 12 assets and 15 attributed X cases')
