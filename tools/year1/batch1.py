import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# BUCK
p1 = [('t', '조준선', B, BL), ('t', ' 또는 ', M, WH), ('t', '수직', B, BL), ('t', ' —', M, WH), ('br',),
      ('t', '목표 공간에 구멍 난 천장 토큰을 놓습니다. 목표 공간은 비어 있어야 합니다.', M, WH)]
p2 = [('t', '구멍 난 천장 토큰이 있는 공간은 진입로 공간으로 취급합니다. 그 위에 진입로 감시 토큰을 놓을 수 있지만, 오퍼레이터는 이를 사용하여 자신의 위층 구역을 드나들 수 없습니다. 구멍 난 천장 토큰은 가젯이 아니며 파괴할' + N + '수' + N + '없습니다.', M, WH)]
run_card('bk', 'buck', '부착식 산탄총 (SK 4-12)', [dict(runs=p1, x_first=959, x_rest=729, cy=413.5), dict(runs=p2, x_first=729, x_rest=729, cy=None, fixed_cy=False)], 885)
# CAPITAO
fire = ic('cp/icon_fire.png')
p1 = [('t', '투척', B, BL), ('t', ' — 화염' + N + '오버레이', M, BL), ('t', ' —', M, WH), ('br',),
      ('t', '화염 오버레이가 있는 공간의 오퍼레이터는 즉시', M, WH), ('i', fire), ('t', '를' + N + '입습니다.', M, WH)]
p2 = [('t', '오퍼레이터가 화염 오버레이가 있는 공간에 진입하거나 그곳에서 행동을 끝낼' + N + '때마다', M, WH), ('i', fire), ('t', '를' + N + '입습니다.', M, WH)]
run_card('cp', 'capitao', '전술 석궁 (TAC mk0)', [dict(runs=p1, x_first=970, x_rest=741, cy=422.5), dict(runs=p2, x_first=741, x_rest=741, cy=None, fixed_cy=False)], 745)
# HIBANA (elite, pages 7-8) and HIBANA2 (pages 9-10)
for d, n, ov in (('hb', 'hibana', {'WEAPONS': [597, 122, 723, 149]}), ('hb2', 'hibana2', None)):
    dest = ic(f'{d}/icon_destroy.png')
    p = [('t', '투척', B, BL), ('t', ' — 목표 공간에서 파괴', M, WH), ('i', dest), ('t', '행동을 수행합니다.', M, WH)]
    run_card(d, n, '유탄 발사기 (X-KAIROS)', [dict(runs=p, x_first=1011, x_rest=769, cy=490.5)], 593, label_override=ov)
