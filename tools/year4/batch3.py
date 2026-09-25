import sys; sys.path.insert(0, 'lib')
from quick import *
M, B = 'Medium', 'ExtraBold'; N = ' '; OR = hexc('#ec8a42'); BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# MOZZIE
p1 = [('t', '준비', B, OR), ('t', ' — 공격자의 전술 인벤토리 내 드론 슬롯에서 충전 큐브 1개를 가져와 이 프로필의 비어 있는 충전 큐브 슬롯에 놓습니다. 이 프로필에 놓이는 충전 큐브는 이것뿐입니다.', M, WH)]
p2 = [('t', '공격자가 ', M, WH), ('t', '드론', B, BL), ('t', '을', M, BL), ('t', ' 배치할 때마다, 소비한 충전 큐브를 상자에 되돌려 놓는 대신 MOZZIE의 프로필에 있는 비어 있는 충전' + N + '큐브' + N + '슬롯에' + N + '놓습니다.', M, WH)]
p3 = [('t', '드론', B, OR), ('t', '.', M, WH)]
run_card('mz', 'mozzie', '해충 발사기', [dict(runs=p1, x_first=730, x_rest=730, cy=398), dict(runs=p2, x_first=730, x_rest=730, cy=None, fixed_cy=False, limit=812 - 10),
         dict(runs=p3, x_first=959, x_rest=959, cy=833)], 950, title_icon=ic('mz/icon_title.png'), label_override={'ACTION': [801, 812, 893, 850]})
# WAMAI
p1 = [('t', '준비', B, OR), ('t', ' — 단단한 벽 섹션 2곳에 MAG-NET을 2개까지 배치합니다.', M, WH)]
p2 = [('t', '상대 오퍼레이터는 MAG-NET이 있는 방' + N + '안으로 ', M, WH), ('t', '투척', B, BL), ('t', ' 가젯을 투척할 수 없습니다.', M, WH)]
run_card('wm', 'wamai', 'MAG-NET 시스템', [dict(runs=p1, x_first=730, x_rest=730, cy=492.5), dict(runs=p2, x_first=731, x_rest=731, cy=None, fixed_cy=False)], 803,
         title_icon=ic('wm/icon_title.png'))
# WARDEN
p1 = [('t', 'WARDEN은 절대', M, WH), ('i', ic('wd/icon_stun.png')), ('t', '를 받지 않습니다.', M, WH)]
p2 = [('t', 'WARDEN의 ', M, WH), ('t', '조준선', B, WH), ('t', '은 연막 오버레이와 가스 오버레이를 통과합니다.', M, WH)]
run_card('wd', 'warden', '응시 스마트 안경', [dict(runs=p1, x_first=731, x_rest=731, cy=528), dict(runs=p2, x_first=731, x_rest=731, cy=None, fixed_cy=False)], 744)
