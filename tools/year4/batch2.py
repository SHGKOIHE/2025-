import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; OR = hexc('#ec8a42')
ic = lambda f: Image.open(f).convert('RGBA')
# NØKK (nokk_first = p7, nokk_second = p9 elite)
for d, name in (('nk', 'nokk_first'), ('nk2', 'nokk_second')):
    p = [('t', 'NØKK은 절대', M, WH), ('i', ic(f'{d}/icon_pin.png')), ('t', '를 받지 않습니다.', M, WH)]
    run_card(d, name, 'HEL 존재감 감소기', [dict(runs=p, x_first=827, x_rest=827, cy=556)], 745)
# GOYO
fire = ic('gy/icon_fire.png')
p1 = [('t', '준비 — 화염 오버레이', B, OR), ('t', ' — 빈 공간 2곳에 이동식 방패를 2개까지 놓습니다.', M, WH)]
p2 = [('t', '상대 오퍼레이터가 이동식 방패에 인접한 공간에 진입하거나 그러한 방패가 파괴될 때마다, 해당 방패를 상자에 되돌려 놓고 그 공간을 덮도록 화염 오버레이를 배치합니다. 화염 오버레이가 차지한 공간의 오퍼레이터는 즉시', M, WH), ('i', fire), ('t', '를' + N + '입습니다.', M, WH)]
p3 = [('t', '오퍼레이터가 화염 오버레이가 있는 공간에 진입하거나 그곳에서 행동을 끝낼 때마다', M, WH), ('i', fire), ('t', '를' + N + '입습니다.', M, WH)]
run_card('gy', 'goyo', '볼칸 방패', [dict(runs=p1, x_first=730, x_rest=730, cy=384.5, limit=476 - 8),
         dict(runs=p2, x_first=996, x_rest=728, cy=498.5, limit=826 - 14), dict(runs=p3, x_first=729, x_rest=729, cy=836)], 972,
         title_icon=ic('gy/icon_title.png'), label_override={'REACTION': [827, 476, 949, 513]})
