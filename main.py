# 方塊位置  l 
# 腳塊朝向  o
# 排列方法: list中0~3是底層(白)4~7是頂層(黃)
# 朝向狀態表示: 白黃朝向 上或下時為0 前後時為1 左右時為2
# 角塊的固定顏色

corner_colors = [
    ("O", "G", "W"),  # 0
    ("R", "G", "W"),  # 1
    ("R", "B", "W"),  # 2
    ("O", "B", "W"),  # 3
    ("O", "G", "Y"),  # 4
    ("R", "G", "Y"),  # 5
    ("R", "B", "Y"),  # 6
    ("O", "B", "Y"),  # 7
]

from moves import *
import numpy as np
import types

l = np.array([0,1,2,3,4,5,6,7])
o = np.array([0,0,0,0,0,0,0,0])



l=np.array(list(map(int,input('角塊位置').split(','))))
o=np.array(list(map(int,input('角塊朝向').split(','))))










def process_corner(l, o, actions, cid_info):
    """
    l: 角塊位置列表
    o: 朝向列表
    actions: 用來儲存動作的列表
    cid_info: 包含角塊ID及相關移動和序列函數的字典
    這個函數會根據指定的角塊ID，找到該角塊在魔術方塊中的位置，
    並根據其位置和朝向執行相應的移動和序列操作，將所需的動作添加到actions列表中。
    move用來將目標塊移至目標曹上方
    seq用來將目標塊從目標曹上方放到目標曹
    """
    for pos, cid in enumerate(l):
        if cid != cid_info['cid']:
            continue

        if pos > 3:
            move = cid_info['move1'](pos, o)
            actions.append(move)
            move(l, o)

            seq = cid_info['seq1'](pos, o)
            actions.append(seq)
            f(l, o, seq)
            break

        if pos < 4:
            move = cid_info['move2'](pos, o)
            actions.append(move)
            f(l, o, move)

            seq = cid_info['seq2'](pos, o)
            actions.append(seq)
            f(l, o, seq)
            break


cid1 = {
    'cid': 0,
    'move1': lambda pos, o=None: [N, U1, U2, U0][pos - 4],
    'seq1': lambda pos, o: [[R0,U2,R1,U1,R0,U0,R1],
                             [U0,R0,U1,R1],
                             [R0,U0,R1]][o[4]],
    'move2': lambda pos, o=None: [[R0,U1,R1],
                                  [L1,U1,L0],
                                  [L0,U2,L1],
                                  [R1,U0,R0,U0]][pos],
    'seq2': lambda pos, o: [[R0,U2,R1,U1,R0,U0,R1],
                             [U0,R0,U1,R1],
                             [R0,U0,R1]][o[4]]
}

cid2 = {
    'cid': 1,
    'move1': lambda pos, o=None: [U0, N, U1, U2][pos - 4],
    'seq1': lambda pos, o: [[L1,U2,L0,U0,L1,U1,L0],
                             [U1,L1,U0,L0],
                             [L1,U1,L0]][o[5]],
    'move2': lambda pos, o=None: [N,
                                  [L1,U0,L0],
                                  [L0,U2,L1,U0],
                                  [R1,U2,R0]][pos],
    'seq2': lambda pos, o: [[L1,U2,L0,U0,L1,U1,L0],
                             [U1,L1,U0,L0],
                             [L1,U1,L0]][o[5]]
}

cid3 = {
    'cid': 2,
    'move1': lambda pos, o=None: [U2,U0, N, U1][pos - 4],
    'seq1': lambda pos, o: [[L0,U2,L1,U1,L0,U0,L1],
                             [U0,L0,U1,L1],
                             [L0,U0,L1]][o[6]],
    'move2': lambda pos, o=None: [N,
                                  N,
                                  [L0,U1,L1],
                                  [R1,U1,R0]][pos],
    'seq2': lambda pos, o: [[L0,U2,L1,U1,L0,U0,L1],
                             [U0,L0,U1,L1],
                             [L0,U0,L1]][o[6]]
}

cid4 = {
    'cid': 3,
    'move1': lambda pos, o=None: [U1,U2,U0, N][pos - 4],
    'seq1': lambda pos, o: [[R1,U2,R0,U0,R1,U1,R0],
                             [U1,R1,U0,R0],
                             [R1,U1,R0]][o[7]],
    'move2': lambda pos, o=None: [N,
                                  N,
                                  N,
                                  [R1,U0,R0]][pos],
    'seq2': lambda pos, o: [[R1,U2,R0,U0,R1,U1,R0],
                             [U1,R1,U0,R0],
                             [R1,U1,R0]][o[7]]
}



actions = []
process_corner(l, o, actions, cid1)
process_corner(l, o, actions, cid2)
process_corner(l, o, actions, cid3)
process_corner(l, o, actions, cid4)

oll = {
    (1,1,1,1): 0,
    (1,2,2,1): 1,
    (0,2,2,0): 2,
    (0,1,1,0): 3,
    (0,1,0,2): 4,
    (1,2,0,2): 5,
    (2,1,2,0): 6,
}
oll_actions = {0:[R2,U2,R0,U2,R2],
               1:[F0,R0,U0,R1,U1,R0,U0,R1,U1,F1],
               2:[F0,R0,U0,R1,U1,F1],
               3:[R0,U0,R1,U1,R1,F0,R0,F1],
               4:[F0,R1,F1,U0,R0,U1,R1],
               5:[L1,U2,L0,U0,L1,U0,L0],
               6:[R0,U2,R1,U1,R0,U1,R1]
               }

if o[4] != 0 or o[5] != 0 or o[6] != 0 or o[7] != 0:
    for _ in range(4):
        key = (o[4], o[5], o[6], o[7])

        if key in oll:
            idx = oll[key]
            f(l, o, oll_actions[idx])
            actions.append(oll_actions[idx])
            break

        actions.append(U0)
        U0(l, o)

pll= {
    (7,5,6,4):0,
    (6,4,5,7):1,
    (5,7,4,6):2,
    (4,6,7,5):3,
    (6,5,4,7):4,
    (4,7,6,5):5,
    (5,4,7,6):6,
    (7,6,5,4):7
}
pll_actions={
    0:[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1,U1],
    1:[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1,U2],
    2:[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1,U0],
    3:[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1],
    4:[F0,R0,U1,R1,U1,R0,U0,R1,F1,R1,U0,R1,U1,R1,F0,R0,F1],
    5:[F0,R0,U1,R1,U1,R0,U0,R1,F1,R1,U0,R1,U1,R1,F0,R0,F1,U2],
    6:[F0,R0,U1,R1,U1,R0,U0,R1,F1,R1,U0,R1,U1,R1,F0,R0,F1,U1],
    7:[F0,R0,U1,R1,U1,R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R0,F1,U0]
}
if l[4] != 4 or l[5] != 5 or l[6] != 6 or l[7] != 7:
    for _ in range(4):
        key = (l[4], l[5], l[6], l[7])

        if key in pll:
            idx = pll[key]
            f(l, o, pll_actions[idx])
            actions.append(pll_actions[idx])
            break

        actions.append(U0)
        U0(l, o)











temp=[]                                     #存的函式轉換成轉動代號
map_inverse={R0:'R',R1:"R'",R2:'R2',
    U0:'U',U1:"U'",U2:'U2',
    F0:'F',F1:"F'",F2:'F2',
    L0:'L',L1:"L'",L2:'L2',
    B0:'B',B1:"B'",B2:'B2',
    D0:'D',D1:"D'",D2:'D2',
    N:''}
for i in actions:
    if isinstance(i, types.FunctionType):
        temp.append(map_inverse[i])
    else:
        for j in i:
            temp.append(map_inverse[j])

map_inverse = {
    'R': "R'", "R'": 'R',
    'U': "U'", "U'": 'U',
    'F': "F'", "F'": 'F',
    'L': "L'", "L'": 'L',
    'B': "B'", "B'": 'B',
    'D': "D'", "D'": 'D',
    'R2':'R2', 'U2':'U2', 'F2':'F2',
    'L2':'L2', 'B2':'B2', 'D2':'D2', '':''
}
changed = True
while changed:
    changed = False
    temp2 = []
    b=0
    while b < len(temp):
        if temp[b] == '':
            b += 1
            continue

        if b + 1 < len(temp):
            if temp[b] == temp[b+1]:
                temp2.append(temp[b][0] + '2')
                b += 2
                changed = True
                continue
            elif temp[b] == map_inverse.get(temp[b+1]):
                b += 2
                changed = True
                continue
        temp2.append(temp[b])
        b += 1
    temp = temp2


changed = True
while changed:
    changed = False
    temp2 = []
    b=0

    while b < len(temp):
        if b + 1 < len(temp):
            if temp[b][0] == temp[b+1][0]:
                if len(temp[b])==2 and len(temp[b+1])==2:
                    temp2.append(temp[b][0])
                    b += 2
                    changed = True
                    continue
                else:
                    temp2.append(temp[b][0]+"'")
                    b += 2
                    changed = True
                    continue
        temp2.append(temp[b])
        b += 1
    temp = temp2




result = ' '.join(i for i in temp2 if i != '')
print(result)
