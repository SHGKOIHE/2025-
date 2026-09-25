import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; OR = hexc('#ec8a42')
ic = lambda f: Image.open(f).convert('RGBA')
# CAVEIRA
pin = ic('cv/icon_pin.png')
p1 = [('t', 'CAVEIRA가 상대 오퍼레이터를 제거할 때마다, 남아 있는 모든 상대' + N + '오퍼레이터는', M, WH), ('i', pin), ('t', '를' + N + '받습니다.', M, WH)]
p2 = [('t', '자신의 위층 구역에서, 상대의 위층' + N + '구역에 있는 위치가 발각된 오퍼레이터를 대상으로 사격 행동(근거리, 가벼운' + N + '엄폐)을 수행합니다.', M, WH)]
run_card('cv', 'caveira', '심문', [dict(runs=p1, x_first=730, x_rest=730, cy=424.5, limit=606-12),
                                     dict(runs=p2, x_first=902, x_rest=730, cy=677.5)], 865,
         label_override={'ACTION': [743, 658, 834, 691]}, extra_titles=[dict(text='고요한 발걸음', cy=621, color='#df8d43')])
# ECHO
stun, elec = ic('ec/icon_stun.png'), ic('ec/icon_elec.png')
p = [('t', '드론', B, OR), ('t', ' — 스캔이 완료되면, 스캔한 방에 있는 위치가 발각된 모든 상대의 오퍼레이터는', M, WH), ('i', stun), ('t', '를' + N + '받습니다.', M, WH)]
run_card('ec', 'echo', '초음파 드론 (YOKAI)', [dict(runs=p, x_first=960, x_rest=735, cy=467.5)], 643, title_icon=elec)
# FROST
dmg = ic('fr/icon_dmg2.png')
p = [('t', '장애물에 인접한 공간에 진입한' + N + '후, 상대 오퍼레이터는', M, WH), ('i', dmg), ('t', '를 입습니다. 상대 오퍼레이터는 추가 행동을 소비하여 이' + N + '효과를 무시할 수 있습니다.', M, WH)]
run_card('fr', 'frost', '전술 함정 (스털링 MK2 LHT)', [dict(runs=p, x_first=962, x_rest=728, cy=457.5)], 656)
