import sys; sys.path.insert(0, 'lib')
from quick import *
import numpy as np
M, B = 'Medium', 'ExtraBold'; N = ' '; BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# AMARU
p1 = [('t', ': AMARU가 진입로 공간으로 이동할 때, 인질을 호위 중이 아니라면 이동 포인트 1을 소비하여 메인 층의 다른 빈 진입로 공간으로 재배치할 수' + N + '있습니다.', M, WH)]
rep = run_card('am', 'amaru', '가라 훅', [dict(runs=p1, x_first=996, x_rest=735, cy=474.5, limit=693 - 10)], 693, label_override={'ACTION': [743, 454, 834, 488]})
size = rep['p0']['size']
for k, back in ((0, False), (1, True)):
    f = f'am/amaru_{"back" if back else "front"}.png'
    im = Image.open(f); a = np.array(im); alpha = a[..., 3].copy()
    cf = gray if back else (lambda c: c)
    draw_label(im, '유지 단계:', F('Medium', size), cf(WH), right=1099, cy=757)
    draw_label(im, '.', F('Medium', size), cf(WH), left=1222, cy=757)
    b = np.array(im); b[..., 3] = alpha; b[alpha == 0, :3] = 0
    Image.fromarray(b, 'RGBA').save(f, dpi=(300, 300))
# GRIDLOCK
dmg = ic('gl/icon_dmg.png')
p1 = [('t', '투척', B, BL), ('t', ' — 목표 공간에 트랙스 스팅어를 놓습니다.', M, WH)]
p2 = [('t', '트랙스 스팅어가 있거나 트랙스 스팅어에 인접한 공간에 진입하는 상대 오퍼레이터는', M, WH), ('i', dmg), ('t', '를 입고 즉시 자신의 활성화를 끝내야 합니다 (미끼 토큰' + N + '제외).', M, WH)]
run_card('gl', 'gridlock', '트랙스 스팅어', [dict(runs=p1, x_first=966, x_rest=729, cy=417), dict(runs=p2, x_first=730, x_rest=730, cy=None, fixed_cy=False)], 731,
         title_icon=ic('gl/icon_title.png'), label_override={'ACTION': [793, 396, 885, 430]})
# KALI
eye, dest = ic('kl/icon_eye.png'), ic('kl/icon_destroy.png')
p = [('t', '투척,', B, BL), ('t', ' 얇은 벽, 강화된 벽 또는 바리케이드 중 1개까지' + N + '무시', M, BL), ('t', ' — 목표 공간을 포함하는 방의 항상 보이는', M, WH), ('i', eye),
     ('t', '모든 가젯과 모든 바리케이드에 파괴', M, WH), ('i', dest), ('t', '행동을 수행합니다.', M, WH)]
run_card('kl', 'kali', 'LV 폭발형 창', [dict(runs=p, x_first=956, x_rest=730, cy=434.5)], 695,
         label_override={'ACTION': [793, 416, 885, 450], 'WEAPONS': [579, 122, 705, 149]})
gm = np.load('kl/gunmask.npy'); bg0 = np.array(Image.open('kl/bg_0.png').convert('RGB')); bg1 = np.array(Image.open('kl/bg_1.png').convert('RGB'))
for f, bg in (('kl/kali_front.png', bg0), ('kl/kali_back.png', bg1)):
    a = np.array(Image.open(f)); reg = np.zeros_like(gm); reg[100:170, 560:720] = True; m = gm & reg
    a[m, :3] = bg[m]
    Image.fromarray(a, 'RGBA').save(f, dpi=(300, 300))
