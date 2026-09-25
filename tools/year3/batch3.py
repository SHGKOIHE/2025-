import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; BL = hexc('#7899ce'); OR = hexc('#ec8a42')
ic = lambda f: Image.open(f).convert('RGBA')
# CLASH
stun, die = ic('cl/icon_stun.png'), ic('cl/icon_die.png')
p1 = [('t', 'CLASH에게 2개 이상의 보호가 있는 경우, CLASH를 대상으로 한 사격에서 일반적인 타격 3개 대신 4개까지' + N + '취소합니다.', M, WH)]
p2 = [('t', '배치', B, OR), ('t', ' — 목표 공간이 있는 방에서 오퍼레이터 하나를 선택합니다. 해당 오퍼레이터는', M, WH), ('i', stun), ('t', '를' + N + '받고 ', M, WH), ('i', die), ('t', '를' + N + '입습니다.', M, WH)]
run_card('cl', 'clash', '전기 방패 (CCE)', [dict(runs=p1, x_first=730, x_rest=730, cy=377.5, limit=569 - 12),
         dict(runs=p2, x_first=971, x_rest=727, cy=590.5)], 755, label_override={'ACTION': [799, 569, 891, 603]})
# KAID
stun, dmg = ic('kd/icon_stun.png'), ic('kd/icon_dmg.png')
p1 = [('t', '준비', B, OR), ('t', ' — 빈 진입로 공간 2곳에 전기집게발을 2개까지 놓습니다.', M, WH)]
p2 = [('t', '상대 오퍼레이터가 전기집게발이 있는 공간에 진입하거나, ', M, WH), ('t', '배치', B, BL), ('t', ' 가젯으로 해당 공간을 목표로 지정할 때마다,', M, WH), ('i', stun), ('t', '를' + N + '받고 ', M, WH), ('i', dmg), ('t', '를' + N + '입습니다.', M, WH)]
p3 = [('t', '상대 ', M, WH), ('t', '드론', B, BL), ('t', '은 전기집게발이 있는 공간에 배치되거나 진입할 수' + N + '없습니다.', M, WH)]
run_card('kd', 'kaid', '전기집게발 (RTILA)', [dict(runs=p1, x_first=724, x_rest=724, cy=426.5), dict(runs=p2, x_first=725, x_rest=725, cy=None, fixed_cy=False),
         dict(runs=p3, x_first=725, x_rest=725, cy=None, fixed_cy=False)], 880, title_icon=ic('kd/icon_title.png'))
# MAESTRO (maestro = p15 normal, maestro_second = p17 elite)
for d, name, p1a, l2x, p2a in (('ms', 'maestro', (815, 456), 905, (908, 564.5)), ('ms2', 'maestro_second', (798, 467), 896, (818, 589.5))):
    pin, die = ic(f'{d}/icon_pin.png'), ic(f'{d}/icon_die.png')
    p1 = [('t', '준비', B, OR), ('t', ' — 악의 눈 카메라를 2개까지', M, WH), ('br',), ('t', '강화된 벽 섹션 2곳에 놓습니다.', M, WH)]
    p2 = [('t', '상대 오퍼레이터가 악의 눈 카메라가 있는 방의 공간에 진입하거나 그곳에서 행동을 끝낼 때마다,', M, WH), ('i', pin), ('t', '를' + N + '받고 ', M, WH), ('i', die), ('t', '피해를' + N + '입습니다.', M, WH)]
    run_card(d, name, '악의 눈 카메라', [dict(runs=p1, x_first=p1a[0], x_rest=l2x, cy=p1a[1]), dict(runs=p2, x_first=p2a[0], x_rest=p2a[0], cy=p2a[1])], 812,
             title_icon=ic(f'{d}/icon_title.png'))
