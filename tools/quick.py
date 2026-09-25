"""Build a card from info.json labels + given runs."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from card import *

def run_card(dirn, name, title_text, paras, bottom_limit, title_icon=None, label_override=None, team=None, team_color=None):
    info = json.load(open(f'{dirn}/info.json'))
    L = dict(info['labels'])
    if label_override: L.update(label_override)
    atk = 'ATTACKER' in L
    labels = dict(WEAPONS=L['WEAPONS'], RANGE=L['RANGE'], RUN=L['RUN'], DESTROY=L['DESTROY'], TEAM=L['ATTACKER' if atk else 'DEFENDER'])
    for k in ('ACTION', 'REACTION'):
        if k in L: labels[k] = L[k]
    t = L['title']
    title = dict(text=title_text, cx=1086, cy=(t[1]+t[3])/2, color=L['title_color'])
    size, paras = fit_size(paras, bottom_limit=bottom_limit)
    rep = None
    for k, back in ((0, False), (1, True)):
        r = build(f'{dirn}/bg_{k}.png', back, f'{dirn}/{name}_{"back" if back else "front"}.png', labels=labels, title=title, paras=paras,
                  title_icon=title_icon, team=team or ('공격팀' if atk else '방어팀'), team_color=team_color or ('#3676b9' if atk else '#e66a14'))
        if not back: rep = r
    print(name, 'size', size, {k: v for k, v in rep.items() if k.startswith('p')})
    return rep
