import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# VIGIL
pin = ic('vg/icon_pin.png')
p1 = [('t', 'VIGIL은 절대', M, WH), ('i', pin), ('t', '를 받지 않습니다.', M, WH)]
p2 = [('t', 'VIGIL이 사격의 대상이 되면, 사격자는 타격 주사위를 굴리기 전에 원하는 주사위 1개를 제거해야' + N + '합니다.', M, WH)]
run_card('vg', 'vigil', '전자 은폐 장치 (ERC-7)', [dict(runs=p1, x_first=730, x_rest=730, cy=525), dict(runs=p2, x_first=730, x_rest=730, cy=None, fixed_cy=False)], 812)
# FINKA
d3, dmg, stun = ic('fk/icon_dmg3.png'), ic('fk/icon_dmg.png'), ic('fk/icon_stun.png')
p1 = [('t', '수직', B, BL), ('t', ' — 목표', M, WH), ('br',), ('t', '오퍼레이터에게서', M, WH), ('i', d3), ('t', '까지 제거합니다.', M, WH)]
p2 = [('t', '투과', B, BL), ('t', ' — 다른 오퍼레이터가 제거되면, FINKA는 (숨은 상태라면 자신을 공개하고) 그 미니어처가 상자에 돌아가기 전에 즉시 해당 오퍼레이터를 소생시킬 수 있습니다. 오퍼레이터가 더 이상 제거 상태가 아닐 때까지', M, WH),
      ('i', dmg), ('t', '를 제거합니다. 소생한' + N + '오퍼레이터는', M, WH), ('i', stun), ('t', '를' + N + '받습니다.', M, WH)]
run_card('fk', 'finka', '아드레날린 분출', [dict(runs=p1, x_first=981, x_rest=719, cy=444.5, limit=560 - 12),
         dict(runs=p2, x_first=959, x_rest=773, cy=592.5)], 955, label_override={'ACTION': [776, 428, 867, 462], 'REACTION': [792, 560, 915, 609]})
# LION
pin = ic('ln/icon_pin.png')
p1 = [('t', '드론', B, BL), ('t', ' — EE-ONE-D는 이동력 포인트를 10개까지 소비할 수 있습니다. 스캔을 완료하면 드론이 이동을 완료한 공간에 EE-ONE-D' + N + '토큰을 놓습니다.', M, WH)]
p2 = [('t', 'EE-ONE-D 토큰이 있는 방의 공간에 진입하거나, 그곳에서 행동을 끝낸 상대' + N + '오퍼레이터는', M, WH), ('i', pin), ('t', '를' + N + '받습니다.', M, WH)]
run_card('ln', 'lion', '드론 (EE-ONE-D)', [dict(runs=p1, x_first=996, x_rest=716, cy=440.5), dict(runs=p2, x_first=762, x_rest=762, cy=None, fixed_cy=False)], 812,
         title_icon=ic('ln/icon_title.png'), label_override={'ACTION': [811, 420, 903, 454]})
