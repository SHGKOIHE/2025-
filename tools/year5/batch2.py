import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; OR = hexc('#ec8a42'); BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# ZERO
pin, die = ic('zr/icon_pin.png'), ic('zr/icon_die.png')
p1 = [('t', '투척', B, BL), ('t', ' 또는 ', M, WH), ('t', '수직', B, BL), ('t', ' — 목표 공간에 있는 단단한 벽 섹션의 한쪽 면에 ARGUS 카메라 1개를 배치합니다.', M, WH)]
p2 = [('t', '상대 오퍼레이터가 ARGUS 카메라가 있는 방의 공간에 진입하거나, 그 공간에서 행동을 끝낼 때마다,', M, WH), ('i', pin), ('t', '를' + N + '받고 ', M, WH), ('i', die), ('t', '를' + N + '입습니다.', M, WH)]
run_card('zr', 'zero', 'ARGUS 발사기', [dict(runs=p1, x_first=992, x_rest=735, cy=455.5), dict(runs=p2, x_first=736, x_rest=736, cy=None, fixed_cy=False)], 831,
         title_icon=ic('zr/icon_title.png'), label_override={'ACTION': [819, 422, 911, 473]})
# ARUNI
stun, fire = ic('ar/icon_stun.png'), ic('ar/icon_fire.png')
p = [('t', '문이나 창문을 통해 컨트롤, 인질 또는 폭탄 목표 토큰이나 미니어처가 있는 방으로 이동한' + N + '후, 상대 오퍼레이터는', M, WH), ('i', stun), ('t', '를' + N + '받고 ', M, WH), ('i', fire), ('t', '를' + N + '입습니다.', M, WH), ('br',), ('t', '상대 오퍼레이터는 추가 행동 1회를 소모하여 이' + N + '효과를 무시할 수 있습니다.', M, WH)]
run_card('ar', 'aruni', 'Surya 게이트', [dict(runs=p, x_first=1011, x_rest=729, cy=416.5)], 719, label_override={'REACTION': [819, 397, 942, 434]})
# MELUSI
p1 = [('t', '준비', B, OR), ('t', ' — 밴시를 2개까지 강화된 벽 섹션' + N + '2곳에' + N + '놓습니다.', M, WH)]
p2 = [('t', '상대 오퍼레이터는 하나 이상의 밴시가 있는 방의 공간에 들어갈 때마다, 이동' + N + '포인트' + N + '1을 추가로 소비해야' + N + '합니다.', M, WH)]
run_card('ml', 'melusi', '밴시 음파 방어', [dict(runs=p1, x_first=730, x_rest=730, cy=489.5), dict(runs=p2, x_first=731, x_rest=731, cy=None, fixed_cy=False)], 806,
         title_icon=ic('ml/icon_title.png'))
