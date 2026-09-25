import sys; sys.path.insert(0, '../lib')
from card import *
W, B = 'Medium', 'ExtraBold'
BL = hexc('#7899ce')
icon = Image.open('icon_destroy.png').convert('RGBA'); icon = icon.crop(icon.getchannel('A').getbbox())
N = ' '
labels = dict(WEAPONS=(579,123,704,150), RANGE=(744,137,844,161), RUN=(1164,979,1232,1003), DESTROY=(1065,1052,1215,1076),
              TEAM=(346,911,482,946), ACTION=(874,517,966,551))
title = dict(text='파쇄망치 (The Caber)', cx=1086, cy=348, color='#7798cd')
p1 = [('t', 'SLEDGE는 기울이기 상태에서는 파쇄망치를 사용할 수 없습니다.', W, WH)]
p2 = [('t', '배치,', B, BL), ('t', ' 얇은 벽 또는 바리케이드 중 1개를' + N + '무시', W, BL), ('t', ' —', W, WH),
      ('t', ' 목표' + N + '공간에서 파괴', W, WH), ('i', icon), ('t', '행동을 수행한 다음 자신의 미니어처를 그곳에 놓습니다.', W, WH),
      ('t', ' 그' + N + '후 새 위치에 인접한 공간' + N + '한' + N + '곳에서 사격' + N + '및/또는 파괴', W, WH), ('i', icon), ('t', '행동을' + N + '수행할' + N + '수' + N + '있습니다.', W, WH)]
paras = [dict(runs=p1, x_first=751, x_rest=751, cy=417, limit=517-12),
         dict(runs=p2, x_first=1037, x_rest=801, cy=534)]
size, paras = fit_size(paras, bottom_limit=939)
print('size', size)
for bg, back, out in (('bg_0.png', False, 'sledge_front.png'), ('bg_1.png', True, 'sledge_back.png')):
    r = build(bg, back, out, labels=labels, title=title, paras=paras)
    if not back: [print(k, v) for k, v in r.items() if k.startswith('p')]
