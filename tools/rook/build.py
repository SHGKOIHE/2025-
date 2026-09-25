import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
OR = hexc('#ec8a42')
N = ' '
dmg = Image.open('icon_dmg.png').convert('RGBA')
labels = dict(WEAPONS=(579,122,705,149), RANGE=(744,135,845,160), RUN=(1175,978,1244,1002), DESTROY=(1053,1050,1203,1074),
              TEAM=(348,910,489,944))
title = dict(text='방탄판 팩 (R1N)', cx=1086, cy=(389+419)/2, color='#df8d43')
p1 = [('t', '준비', B, OR), ('t', ' — 체력 수치가 5 이하인 다른 오퍼레이터 3명의 프로필에 방탄판' + N + '토큰을' + N + '놓습니다.', W, WH)]
p2 = [('t', '오퍼레이터는', W, WH), ('i', dmg), ('t', '를 받는 대신 자신의 방탄판 토큰을 박스에 되돌려' + N + '놓아야' + N + '합니다.', W, WH)]
paras = [dict(runs=p1, x_first=752, x_rest=752, cy=495), dict(runs=p2, x_first=752, x_rest=752, cy=None, fixed_cy=False)]
size, paras = fit_size(paras, bottom_limit=810)
print('size', size, [p['cy'] for p in paras])
for bg, back, out in (('bg_0.png', False, 'rook_front.png'), ('bg_1.png', True, 'rook_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras, team='방어팀', team_color='#e66a14')
    if not back: [print(k, v) for k, v in r.items() if k.startswith('p') or k=='title']
