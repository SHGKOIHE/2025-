import sys; sys.path.insert(0, '../lib')
from card import *
W = 'Medium'
N = ' '
dmg = Image.open('icon_dmg2.png').convert('RGBA')
labels = dict(WEAPONS=(579,122,705,149), RANGE=(745,135,844,160), RUN=(1164,978,1233,1002), DESTROY=(1053,1050,1203,1074),
              TEAM=(346,910,482,945), REACTION=(882,443,1005,476))
title = dict(text='소총 방패 (TARS MK 0)', cx=1086, cy=(355+385)/2, color='#6d92ca')
runs = [('t', 'BLACKBEARD가 사격의 목표가 되었을 때', W, WH), ('i', dmg), ('t', '를' + N + '무시합니다.', W, WH)]
paras = [dict(runs=runs, x_first=1051, x_rest=818, cy=459.5)]
size, paras = fit_size(paras, bottom_limit=589)
print('size', size)
for bg, back, out in (('bg_0.png', False, 'blackbeard_front.png'), ('bg_1.png', True, 'blackbeard_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras)
    if not back: [print(k, v) for k, v in r.items() if k.startswith('p') or k in ('title','REACTION')]
