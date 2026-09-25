import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; OR = hexc('#ec8a42'); BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# VALKYRIE
pin = ic('vk/icon_pin.png')
p1 = [('t', '준비', B, OR), ('t', ' — 단단한 벽 섹션에 칠흑의 주시자를 1개 배치합니다.', M, WH)]
p2 = [('t', '투척', B, OR), ('t', ' — 목표 공간에 있는 단단한 벽 섹션에 칠흑의 주시자를 배치합니다.', M, WH)]
p3 = [('t', '목표 공간을 포함하는 방의 모든 상대' + N + '오퍼레이터는', M, WH), ('i', pin), ('t', '를' + N + '받습니다. 칠흑의' + N + '주시자는 일반 카메라처럼 작동합니다.', M, WH)]
run_card('vk', 'valkyrie', '칠흑의 주시자', [dict(runs=p1, x_first=738, x_rest=738, cy=405.5, limit=503-12),
         dict(runs=p2, x_first=953, x_rest=738, cy=536), dict(runs=p3, x_first=744, x_rest=744, cy=None, fixed_cy=False)], 865,
         title_icon=ic('vk/icon_title.png'), label_override={'ACTION': [803, 519, 895, 553]})
# DOKKAEBI
pin = ic('dk/icon_pin.png')
p1 = [('t', '투과', B, BL), ('t', ' — 선택된 오퍼레이터는', M, WH), ('br',), ('i', pin), ('t', '를' + N + '받습니다.', M, WH)]
p2 = [('t', '수직', B, BL), ('t', ' — 목표 공간이 있는 방에 있는 자신의 팀의 모든 오퍼레이터에게서', M, WH), ('br',), ('i', pin), ('t', '를' + N + '제거합니다.', M, WH)]
run_card('dk', 'dokkaebi', '논리 폭탄', [dict(runs=p1, x_first=957, x_rest=791, cy=429.5, limit=548-12),
         dict(runs=p2, x_first=940, x_rest=791, cy=565)], 691,
         label_override={'ACTION': [801, 413, 893, 446], 'ACTION2': [780, 548, 872, 582]})
# JACKAL
pin, up = ic('jk/icon_pin.png'), ic('jk/icon_up.png')
p1 = [('t', '자신의 위층 구역으로 이동하거나 그곳에서 나오는 상대' + N + '오퍼레이터는', M, WH), ('i', pin), ('t', '를' + N + '받습니다.', M, WH)]
p2 = [('i', up), ('t', '방이나 자신의 위층 구역에서, 상대의 위층' + N + '구역에 있는 위치가 발각된 오퍼레이터를 대상으로 사격 행동(근거리, 가벼운' + N + '엄폐)을 수행합니다.', M, WH)]
run_card('jk', 'jackal', '아이녹스 (EYENOX MK3)', [dict(runs=p1, x_first=731, x_rest=731, cy=393, limit=501-12),
         dict(runs=p2, x_first=997, x_rest=825, cy=518)], 763, label_override={'ACTION': [843, 501, 935, 535]})
