import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# YING
stun = ic('yg/icon_stun.png')
p = [('t', '배치,', B, BL), ('t', ' 얇은 벽 또는 바리케이드 1개까지 무시', M, BL), ('t', ' 또는 ', M, WH), ('t', '수직', B, BL), ('t', ' —', M, WH),
     ('t', ' 목표 공간을 포함하는 방의 모든 오퍼레이터는 YING을' + N + '제외하고', M, WH), ('i', stun), ('t', '를' + N + '받습니다.', M, WH)]
run_card('yg', 'ying', '칸델라', [dict(runs=p, x_first=953, x_rest=739, cy=436.5)], 674, label_override={'ACTION': [793, 419, 885, 453]})
# ZOFIA
stun, fire = ic('zf/icon_stun.png'), ic('zf/icon_fire.png')
p = [('t', '조준선,', B, BL), ('t', ' 바리케이드 1개까지 무시', M, BL), ('t', ' — 목표가 된 오퍼레이터는', M, WH), ('i', stun),
     ('t', '를 받고', M, WH), ('i', fire), ('t', '를' + N + '입습니다.', M, WH)]
run_card('zf', 'zofia', '생명선 (KS79)', [dict(runs=p, x_first=979, x_rest=731, cy=459)], 607, label_override={'ACTION': [819, 438, 911, 472]})
# ELA
stun = ic('el/icon_stun.png')
p = [('t', '방의 경계를 넘거나 자신의 위층 구역에서 진입로 칸으로 들어오는 상대' + N + '오퍼레이터는', M, WH), ('i', stun),
     ('t', '를 받습니다. 해당 오퍼레이터는 추가 행동 1회를 소비하여 이' + N + '효과를 무시할 수 있습니다.', M, WH)]
run_card('el', 'ela', 'GRZMOT 지뢰', [dict(runs=p, x_first=1002, x_rest=757, cy=430.5)], 673, label_override={'REACTION': [832, 409, 960, 447]})
