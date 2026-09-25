import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
BL = hexc('#7899ce')
def ico(f): return Image.open(f).convert('RGBA')
elec, dest = ico('icon_elec.png'), ico('icon_destroy.png')
labels = dict(WEAPONS=(579,123,704,150), RANGE=(744,137,844,161), RUN=(1164,979,1232,1003), DESTROY=(1065,1052,1215,1076),
              TEAM=(346,911,482,946), ACTION=(792,425,883,458))
title = dict(text='발열성 폭약 (BC-3)', cx=1086, cy=(330+359)/2, color='#3977ba')
runs = [('t', '배치', B, BL), ('t', ' — 목표로 지정한 공간과 그\u00a0공간에 인접한 모든 공간에서 파괴', W, WH), ('i', dest),
        ('t', '행동을 수행합니다.', W, WH), ('br',), ('t', '칸막이는 발열성\u00a0폭약의 효과 범위를 차단하지\u00a0않습니다.', W, WH)]
paras = [dict(runs=runs, x_first=949, x_rest=728, cy=441.5)]
size, paras = fit_size(paras, bottom_limit=685)
print('size', size)
for bg, back, out in (('bg_0.png', False, 'thermite_front.png'), ('bg_1.png', True, 'thermite_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras, title_icon=elec)
    if not back: [print(k, v) for k, v in r.items()]
