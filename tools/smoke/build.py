import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
OR = hexc('#ec8a42')
N = ' '
dmg = Image.open('icon_dmg.png').convert('RGBA')
labels = dict(WEAPONS=(579,122,705,149), RANGE=(745,135,844,160), RUN=(1164,978,1233,1002), DESTROY=(1066,1052,1215,1076),
              TEAM=(348,910,489,944), ACTION=(810,401,901,434))
title = dict(text='원격 가스탄 (Z8 화합물)', cx=1086, cy=(318+348)/2, color='#ec8a42')
p1 = [('t', '투척', B, OR), ('t', ' — 가스' + N + '오버레이', W, OR), ('t', ' —', W, WH), ('br',),
      ('t', '가스 오버레이가 있는 공간의 오퍼레이터 (SMOKE 제외)는 즉시', W, WH), ('i', dmg), ('t', '를' + N + '입습니다.', W, WH)]
p2 = [('t', '가스 오버레이가 있는 공간은 ', W, WH), ('t', '조준선', B, WH), ('t', '을 차단합니다. 오퍼레이터(SMOKE' + N + '제외)가 그' + N + '공간에 들어가거나 그곳에서 행동을 끝낼 때마다', W, WH),
      ('i', dmg), ('t', '를' + N + '입습니다.', W, WH)]
paras = [dict(runs=p1, x_first=975, x_rest=732, cy=417.5), dict(runs=p2, x_first=732, x_rest=732, cy=None, fixed_cy=False)]
size, paras = fit_size(paras, bottom_limit=868)
print('size', size, [p['cy'] for p in paras])
for bg, back, out in (('bg_0.png', False, 'smoke_front.png'), ('bg_1.png', True, 'smoke_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras, team='방어팀', team_color='#e66a14')
    if not back: [print(k, v) for k, v in r.items() if k.startswith('p') or k in ('title','ACTION')]
