import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# ACE: ace_first = p1 (ac), ace_second = p3 (ac2)
cfg = {'ac': dict(name='ace_first', p1=(990, 410, 804), p2=(999, 530, 776), p3=(782, 655.5), a1=[818, 390, 910, 424], a2=[846, 512, 937, 547], frame=777),
       'ac2': dict(name='ace_second', p1=(990, 415, 733), p2=(978, 534, 739), p3=(739, 651.5), a1=[818, 396, 910, 430], a2=[819, 518, 910, 553], frame=744)}
for d, c in cfg.items():
    dest = ic(f'{d}/icon_dest.png')
    p1 = [('t', '투척', B, BL), ('t', ' — 목표 공간에서 파괴', M, WH), ('i', dest), ('t', '행동을 수행합니다.', M, WH)]
    p2 = [('t', '투척', B, BL), ('t', ' — 목표 진입로 공간에 잔해 스탠디를 놓습니다.', M, WH)]
    p3 = [('t', '잔해는 장애물입니다. 잔해가 차지한 공간은 더 이상 진입로 공간이' + N + '아닙니다.', M, WH)]
    run_card(d, c['name'], 'S.E.L.M.A. 아쿠아 브리처', [dict(runs=p1, x_first=c['p1'][0], x_rest=c['p1'][2], cy=c['p1'][1], limit=c['a2'][1] - 6),
             dict(runs=p2, x_first=c['p2'][0], x_rest=c['p2'][2], cy=c['p2'][1], limit=c['p3'][1] - 30), dict(runs=p3, x_first=c['p3'][0], x_rest=c['p3'][0], cy=c['p3'][1])],
             c['frame'], title_icon=ic(f'{d}/icon_title.png'), label_override={'ACTION': c['a1'], 'ACTION2': c['a2']})
# IANA
p1 = [('t', 'IANA가', M, WH), ('i', ic('ia/icon_pin.png')), ('t', '를 받지 않습니다.', M, WH)]
p2 = [('t', 'IANA는 추가 행동이 필요한 가젯의 특수 효과를 무시합니다.', M, WH)]
p3 = [('t', 'IANA를 사격하는 상대 오퍼레이터는 타격 주사위를 굴리기 전에 주사위 1개를 제거해야 합니다. 추가 행동을 소비하여 이 효과를 무시할 수' + N + '있습니다.', M, WH)]
run_card('ia', 'iana', '제미니 복제기', [dict(runs=p1, x_first=965, x_rest=965, cy=432), dict(runs=p2, x_first=965, x_rest=791, cy=510, limit=619 - 8),
         dict(runs=p3, x_first=965, x_rest=791, cy=648)], 860,
         label_override={'REACTION': [796, 409, 919, 445], 'REACTION2': [796, 487, 919, 523], 'REACTION3': [793, 628, 916, 664]}, force_size=40)
