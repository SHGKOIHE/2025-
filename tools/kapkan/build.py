import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
BL = hexc('#7899ce')
N = ' '
NAME = sys.argv[1] if len(sys.argv) > 1 else 'kapkan'
labels = dict(WEAPONS=(579,122,705,149), RANGE=(745,135,844,160), RUN=(1164,978,1233,1002), DESTROY=(1053,1050,1203,1074),
              TEAM=(348,910,489,944), REACTION=(802,434,925,453))
title = dict(text='진입 방지 폭약 (EDD)', cx=1086, cy=(341+379)/2, color='#df8b41')
dmg = Image.open('icon_dmg2.png').convert('RGBA')
runs = [('t', '문이나 창문을 통과하여 이동한' + N + '후, 상대' + N + '오퍼레이터는', W, WH), ('i', dmg),
        ('t', '를 입습니다. 상대' + N + '오퍼레이터는 추가 행동 1회를 소비하여 이' + N + '효과를 무시할 수 있습니다.', W, WH)]
paras = [dict(runs=runs, x_first=963, x_rest=752, cy=443.5)]
size, paras = fit_size(paras, bottom_limit=669)
print('size', size)
for bg, back, out in (('bg_0.png', False, f'{NAME}_front.png'), ('bg_1.png', True, f'{NAME}_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras, team='방어팀', team_color='#e66a14')
    if not back: [print(k, v) for k, v in r.items()]
