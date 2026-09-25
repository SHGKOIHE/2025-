import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
BL = hexc('#7798cd')
def ico(f): return Image.open(f).convert('RGBA')
elec, dest = ico('icon_elec.png'), ico('icon_destroy.png')
BR = ('br',)
labels = dict(WEAPONS=(579,123,704,150), RANGE=(744,137,844,161), RUN=(1164,979,1232,1003), DESTROY=(1053,1050,1203,1074),
              TEAM=(346,911,482,946), ACTION=(801,424,893,457))
title = dict(text='EMP 수류탄 (EG MKO)', cx=1086, cy=(356+386)/2, color='#7899ce')
runs = [('t', '투척', B, BL), ('t', ' — 목표 공간을 포함하는 방의 모든 전자장비', W, WH), ('i', elec), ('t', '가젯에 파괴', W, WH), ('i', dest), ('t', '행동을 수행합니다.', W, WH)]
paras = [dict(runs=runs, x_first=944, x_rest=727, cy=440.5)]
for bg, back, out in (('bg_0.png', False, 'thatcher_front.png'), ('bg_1.png', True, 'thatcher_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras)
    if not back: [print(k, v) for k, v in r.items()]
