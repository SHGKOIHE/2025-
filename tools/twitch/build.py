import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
BL = hexc('#6990c9')
def ico(f): return Image.open(f).convert('RGBA')
die, elec, dest, telec = ico('icon_die.png'), ico('icon_elec.png'), ico('icon_destroy.png'), ico('icon_elec_title.png')
labels = dict(WEAPONS=(579,122,705,149), RANGE=(745,135,844,160), RUN=(1164,978,1233,1002), DESTROY=(1053,1050,1203,1074),
              TEAM=(346,910,482,945), ACTION=(809,421,900,454))
title = dict(text='감전 드론 (RSD 모델 1)', cx=1086, cy=(336+366)/2, color='#6990c9')
runs = [('t', '드론', B, BL), ('t', ' — 스캔을 완료하면', W, WH), ('i', die), ('t', '를 굴립니다. 나온 타격 하나당 스캔한 방의 전자장비 가젯', W, WH),
        ('i', elec), ('t', '하나에 파괴', W, WH), ('i', dest), ('t', '행동을 수행합니다.', W, WH)]
paras = [dict(runs=runs, x_first=967, x_rest=726, cy=437.5)]
size, paras = fit_size(paras, bottom_limit=651)
print('size', size)
for bg, back, out in (('bg_0.png', False, 'twitch_front.png'), ('bg_1.png', True, 'twitch_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras, title_icon=telec)
    if not back: [print(k, v) for k, v in r.items()]
