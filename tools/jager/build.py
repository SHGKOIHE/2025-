import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
BL = hexc('#7899ce')
N = ' '
NAME = sys.argv[1] if len(sys.argv) > 1 else 'jager'
labels = dict(WEAPONS=(579,122,705,149), RANGE=(745,135,844,160), RUN=(1164,978,1233,1002), DESTROY=(1053,1050,1203,1074),
              TEAM=(348,910,489,944), REACTION=(789,410,912,429))
title = dict(text='선제 방어 (ADS-MKIV)', cx=1086, cy=(317+347)/2, color='#df8b41')
runs = [('t', '상대 오퍼레이터가 방 안으로 ', W, WH), ('t', '투척', B, BL),
        ('t', ' 가젯을 던지면, 해당 가젯을 무시합니다. 해당 가젯의 충전량은 소실됩니다. 상대' + N + '오퍼레이터는 추가 행동을 소비하여 이' + N + '효과를 무시할 수 있습니다.', W, WH)]
paras = [dict(runs=runs, x_first=966, x_rest=729, cy=419.5)]
size, paras = fit_size(paras, bottom_limit=672)
print('size', size)
for bg, back, out in (('bg_0.png', False, f'{NAME}_front.png'), ('bg_1.png', True, f'{NAME}_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras, team='방어팀', team_color='#e66a14')
    if not back: [print(k, v) for k, v in r.items()]
