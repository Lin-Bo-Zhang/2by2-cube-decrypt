'''
程式.二階魔術方塊破解器.main 的 Docstring
本程式用於解二階魔術方塊，使用者可輸入打亂公式或手動輸入魔術方塊狀態，程式將輸出解法公式。
'''
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

l = np.array([0,1,2,3,4,5,6,7])                                     #資料
o = np.array([0,0,0,0,0,0,0,0])                                                    
                                                                    

if int(input('使用打亂公式輸入1,手動輸入狀態輸入0:'))==0:
    l=np.array(list(map(int,input('角塊位置').split(','))))              #輸入
    o=np.array(list(map(int,input('角塊朝向').split(','))))             
else:
    a=list(map(str,(input('打亂公式').split(' '))))
    map={'R':R0,"R'":R1,'R2':R2,
        'U':U0,"U'":U1,'U2':U2,
        'F':F0,"F'":F1,'F2':F2,
        }
    a=[map[i] for i in a]

    for i in a:
        i(l,o)










def process_corner(l, o, actions, cid_info):            #第一層邏輯
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
        if cid != cid_info['cid']:                      #找到目標腳塊
            continue

        if pos > 3:                                     #處理在頂層的腳塊
            move = cid_info['move1'](pos, o)            #移動到目標曹上方
            actions.append(move)                        #動作存放
            move(l, o)

            seq = cid_info['seq1'](pos, o)              #放入目標曹
            actions.append(seq)                         #動作存放
            f(l, o, seq)
            break

        if pos < 4:                                     #處理在底層的腳塊            
            move = cid_info['move2'](pos, o)            #移動到頂層並移動到目標曹上方
            actions.append(move)                        #動作存放
            f(l, o, move)

            seq = cid_info['seq2'](pos, o)              #放入目標曹
            actions.append(seq)                         #動作存放
            f(l, o, seq)
            break


cid1 = {                                                                    #腳塊0的邏輯
    'cid': 0,
    'move1': lambda pos, o=None: [N, U1, U2, U0][pos - 4],                  #腳塊在頂層時的移動函式
    'seq1': lambda pos, o: [[R0,U2,R1,U1,R0,U0,R1],                         #放入目標曹的函式
                             [U0,R0,U1,R1],
                             [R0,U0,R1]][o[4]],
    'move2': lambda pos, o=None: [[R0,U1,R1],                               #腳塊在底層時的移動函式 
                                  [L1,U1,L0],
                                  [L0,U2,L1],
                                  [R1,U0,R0,U0]][pos],
    'seq2': lambda pos, o: [[R0,U2,R1,U1,R0,U0,R1],                         #放入目標曹的函式
                             [U0,R0,U1,R1],
                             [R0,U0,R1]][o[4]]
}

cid2 = {                                                                    #腳塊1的邏輯                            
    'cid': 1,                                                               
    'move1': lambda pos, o=None: [U0, N, U1, U2][pos - 4],                  #腳塊在頂層時的移動函式
    'seq1': lambda pos, o: [[L1,U2,L0,U0,L1,U1,L0],                         #放入目標曹的函式        
                             [U1,L1,U0,L0],         
                             [L1,U1,L0]][o[5]],
    'move2': lambda pos, o=None: [N,                                        #腳塊在底層時的移動函式
                                  [L1,U0,L0],
                                  [L0,U2,L1,U0],
                                  [R1,U2,R0]][pos],
    'seq2': lambda pos, o: [[L1,U2,L0,U0,L1,U1,L0],                         #放入目標曹的函式
                             [U1,L1,U0,L0],
                             [L1,U1,L0]][o[5]]
}

cid3 = {                                                                    #腳塊2的邏輯                        
    'cid': 2,
    'move1': lambda pos, o=None: [U2,U0, N, U1][pos - 4],                   #腳塊在頂層時的移動函式
    'seq1': lambda pos, o: [[L0,U2,L1,U1,L0,U0,L1],                         #放入目標曹的函式
                             [U0,L0,U1,L1],
                             [L0,U0,L1]][o[6]],
    'move2': lambda pos, o=None: [N,                                        #腳塊在底層時的移動函式
                                  N,
                                  [L0,U1,L1],
                                  [R1,U1,R0]][pos],
    'seq2': lambda pos, o: [[L0,U2,L1,U1,L0,U0,L1],                          #放入目標曹的函式
                             [U0,L0,U1,L1],
                             [L0,U0,L1]][o[6]]
}

cid4 = {                                                                    #腳塊3的邏輯
    'cid': 3,
    'move1': lambda pos, o=None: [U1,U2,U0, N][pos - 4],                    #腳塊在頂層時的移動函式
    'seq1': lambda pos, o: [[R1,U2,R0,U0,R1,U1,R0],                         #放入目標曹的函式
                             [U1,R1,U0,R0],
                             [R1,U1,R0]][o[7]],
    'move2': lambda pos, o=None: [N,                                        #腳塊在底層時的移動函式
                                  N,
                                  N,
                                  [R1,U0,R0]][pos],
    'seq2': lambda pos, o: [[R1,U2,R0,U0,R1,U1,R0],                         #放入目標曹的函式
                             [U1,R1,U0,R0],
                             [R1,U1,R0]][o[7]]
}



actions = []
process_corner(l, o, actions, cid1)                                         #執行腳塊處理函式
process_corner(l, o, actions, cid2)
process_corner(l, o, actions, cid3)
process_corner(l, o, actions, cid4)

oll = {                                                                     #OLL辨識表
    (1,1,1,1): [R2,U2,R0,U2,R2],
    (1,2,2,1): [F0,R0,U0,R1,U1,R0,U0,R1,U1,F1],
    (0,2,2,0): [F0,R0,U0,R1,U1,F1],
    (0,1,1,0): [R0,U0,R1,U1,R1,F0,R0,F1],
    (0,1,0,2): [F0,R1,F1,U0,R0,U1,R1],
    (1,2,0,2): [L1,U2,L0,U0,L1,U0,L0],
    (2,1,2,0): [R0,U2,R1,U1,R0,U1,R1],
}


if o[4] != 0 or o[5] != 0 or o[6] != 0 or o[7] != 0:                        #OLL(頂面顏色翻正公式)辨識與處理
    for _ in range(4):
        key = tuple(o[4:8])

        if key in oll:
            f(l, o, oll[key])
            actions.append(oll[key])                                        #動作存放
            break

        actions.append(U0)                                                 #動作存放
        U0(l, o)

pll= {                                                                      #PLL(頂層腳塊位置公式)辨識表                                  
    (7,5,6,4):[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1,U1],
    (6,4,5,7):[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1,U2],
    (5,7,4,6):[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1,U0],
    (4,6,7,5):[R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R2,U1,R1],
    (6,5,4,7):[F0,R0,U1,R1,U1,R0,U0,R1,F1,R1,U0,R1,U1,R1,F0,R0,F1],
    (4,7,6,5):[F0,R0,U1,R1,U1,R0,U0,R1,F1,R1,U0,R1,U1,R1,F0,R0,F1,U2],
    (5,4,7,6):[F0,R0,U1,R1,U1,R0,U0,R1,F1,R1,U0,R1,U1,R1,F0,R0,F1,U1],
    (7,6,5,4):[F0,R0,U1,R1,U1,R0,U0,R1,F1,R0,U0,R1,U1,R1,F0,R0,F1,U0]
}

if l[4] != 4 or l[5] != 5 or l[6] != 6 or l[7] != 7:                    #PLL(頂層腳塊位置公式)辨識與處理
    for _ in range(4):
        key = tuple(l[4:8])

        if key in pll:
            f(l, o, pll[key])
            actions.append(pll[key])                            #動作存放
            break

        actions.append(U0)                                              #動作存放
        U0(l, o)











temp=[]                                     #存的動作轉換成轉動代號
map_inverse={R0:'R',R1:"R'",R2:'R2',
    U0:'U',U1:"U'",U2:'U2',
    F0:'F',F1:"F'",F2:'F2',
    L0:'L',L1:"L'",L2:'L2',
    B0:'B',B1:"B'",B2:'B2',
    D0:'D',D1:"D'",D2:'D2',
    N:''}
for i in actions:                           #將動作轉換成轉動代號
    if isinstance(i, types.FunctionType):   #檢查是否為單一動作
        temp.append(map_inverse[i])
    else:                                   #取出清單裡的動作
        for j in i:
            temp.append(map_inverse[j])

map_inverse = {                             #用於簡化公式的對應表
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
while changed:                          #簡化公式(連續相同動作合併或刪除)
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
while changed:                      #簡化公式(處理合併後出現的動作x2+動作or動作')
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




result = ' '.join(i for i in temp2 if i != '')          #動作轉換為字串並輸出
print(result)
