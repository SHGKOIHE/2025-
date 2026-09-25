import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
OR = hexc('#ec8a42')
N = ' '
def ico(f): return Image.open(f).convert('RGBA')
elec, ticon = ico('icon_elec.png'), ico('icon_title.png')
labels = dict(WEAPONS=(580,122,705,149), RANGE=(745,135,844,160), RUN=(1164,978,1233,1002), DESTROY=(1066,1049,1215,1073),
              TEAM=(348,910,489,944))
title = dict(text='신호 방해기 (GC90)', cx=1086, cy=(399+429)/2, color='#df8d43')
p1 = [('t', '준비', B, OR), ('t', ' — 단단한 벽 섹션 2곳에 신호' + N + '방해기를 2개까지 배치합니다.', W, WH)]
p2 = [('t', '공격팀의 전자장비', W, WH), ('i', elec), ('t', '가젯은 신호' + N + '방해기가 있는 방의 공간을 목표로 하거나, 그 공간에 배치되거나, 그 공간에 들어갈 수 없습니다.', W, WH)]
paras = [dict(runs=p1, x_first=730, x_rest=730, cy=486.5), dict(runs=p2, x_first=736, x_rest=736, cy=None, fixed_cy=False)]
size, paras = fit_size(paras, bottom_limit=783)
print('size', size, [p['cy'] for p in paras])
for bg, back, out in (('bg_0.png', False, 'mute_front.png'), ('bg_1.png', True, 'mute_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras, title_icon=ticon, team='방어팀', team_color='#e66a14')
    if not back: [print(k, v) for k, v in r.items()]
