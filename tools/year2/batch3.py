import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; OR = hexc('#ec8a42')
ic = lambda f: Image.open(f).convert('RGBA')
# LESION (lesion_first = PDF p11, lesion_second = PDF p13 elite)
for d, name, l1, react, frame, ov in (('ls', 'lesion_first', (966, 415, 454), [796, 415, 919, 448], 649, None),
                                      ('ls2', 'lesion_second', (966, 426, 465), [796, 426, 919, 459], 652, {'WEAPONS': [579, 122, 705, 149]})):
    pin, dmg = ic(f'{d}/icon_pin.png'), ic(f'{d}/icon_dmg.png')
    p = [('t', '회색 진입로 칸에 진입하는 상대' + N + '오퍼레이터는', M, WH), ('i', pin), ('t', '를 받고', M, WH), ('i', dmg),
         ('t', '피해를 입습니다. 상대' + N + '오퍼레이터는 추가 행동 1회를 소비하여 이' + N + '효과를 무시할 수 있습니다.', M, WH)]
    o = dict(REACTION=react)
    if ov: o.update(ov)
    run_card(d, name, '고독 지뢰 (GU)', [dict(runs=p, x_first=l1[0], x_rest=725, cy=(l1[1] + l1[2]) / 2)], frame, label_override=o)
# MIRA (3rd line of setup indented like original to clear the raised finger)
p1 = [('t', '준비', B, OR), ('t', ' — 얇은 벽이나 강화된 벽 섹션 1곳까지', M, WH), ('br',), ('t', '크기가 일치하는 구멍 난 벽 토큰으로', M, WH)]
p1b = [('t', '덮습니다.', M, WH)]
p2 = [('t', 'MIRA가 얇은 벽이나 강화된 벽 섹션이 있는 공간에 있다면, 그 벽을 크기가 일치하는 구멍 난 벽 토큰으로 덮은' + N + '후, 구멍 난 벽을 통해 사격 행동을 수행합니다.', M, WH)]
run_card('mr', 'mira', '검은 거울', [dict(runs=p1, x_first=777, x_rest=777, cy=404, limit=547 - 12),
                                    dict(runs=p1b, x_first=812, x_rest=812, cy=404 + 2 * 46),
                                    dict(runs=p2, x_first=1114, x_rest=881, cy=589)], 812, label_override={'ACTION': [961, 569, 1053, 603]})
