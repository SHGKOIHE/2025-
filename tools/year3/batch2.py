import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; BL = hexc('#7899ce'); OR = hexc('#ec8a42')
ic = lambda f: Image.open(f).convert('RGBA')
# MAVERICK
p = [('t', 'MAVERICK이 얇은 벽이나 강화된 벽 섹션이 있는 공간에 있다면, 그' + N + '벽을 크기가 일치하는 구멍 난 벽 토큰으로 덮은' + N + '후, 구멍 난 벽을 통과하는 사격 행동을 수행합니다.', M, WH)]
run_card('mv', 'maverick', '돌파용 토치 (Suri)', [dict(runs=p, x_first=982, x_rest=736, cy=428)], 691, label_override={'ACTION': [828, 410, 920, 444]})
# NOMAD
p = [('t', '투척', B, BL), ('t', ' — 목표 공간에 있는 상대 오퍼레이터를 인접한 비어 있는 공간 중 원하는 곳으로 이동시킵니다. 방향과 모든 상태 마커는 그대로 유지합니다. 목표로 정한 오퍼레이터가 기울이기 상태라면, 오퍼레이터를 이동시키기 전에 해당 기울이기 스탠디를 상대 플레이어의 공급처로' + N + '되돌립니다.', M, WH)]
run_card('nm', 'nomad', '기압탄 발사기', [dict(runs=p, x_first=943, x_rest=731, cy=396)], 746, label_override={'ACTION': [793, 375, 884, 409]})
# ALIBI
pin = ic('al/icon_pin.png')
p1 = [('t', '준비', B, OR), ('t', ' — ALIBI의 숨겨진 오퍼레이터 토큰 중 미끼 토큰 2개를 추가로 놓습니다.', M, WH)]
p2 = [('t', 'ALIBI의 미끼 토큰 중 하나가 공개되면 해당 토큰만 상자에 되돌려 놓습니다. ALIBI를 나타내는 숨겨진 오퍼레이터 토큰이 공개되면 ALIBI의 모든 숨겨진 오퍼레이터 토큰을 상자에 되돌려 놓습니다.', M, WH)]
p3 = [('t', 'ALIBI의 미끼 토큰 중 하나를 공개하고, 상자에 되돌려 놓기 전에 이동 포인트가 4인 것처럼 이동시킵니다. 미끼가 진입한 공간의 오퍼레이터는', M, WH), ('i', pin), ('t', '를' + N + '받습니다.', M, WH)]
run_card('al', 'alibi', '프리즈마 홀로그램', [dict(runs=p1, x_first=730, x_rest=730, cy=380.5),
         dict(runs=p2, x_first=730, x_rest=730, cy=489, limit=705 - 8),
         dict(runs=p3, x_first=910, x_rest=744, cy=722)], 955, label_override={'ACTION': [756, 705, 848, 739]})
