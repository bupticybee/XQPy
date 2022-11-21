from XQlightPy.position import Position
from XQlightPy.search import Search
from XQlightPy.cchess import move2Iccs,Iccs2move
import numpy as np

uni_pieces = {4+8:'车', 3+8:'马', 2+8:'相', 1+8:'仕', 0+8:'帅', 6+8:'兵', 5+8:'炮',
                  4+16:'俥', 3+16:'傌', 2+16:'象', 1+16:'士', 0+16:'将', 6+16:'卒', 5+16:'砲', 0:'．'}

def print_board(pos):
    print()
    for i, row in enumerate(np.asarray(pos.squares).reshape(16,16)[3:3+10,3:3+9]):
        print(' ', 9 - i, ''.join(uni_pieces.get(p, p) for p in row))
    print('    ａｂｃｄｅｆｇｈｉ\n\n')


search_time_ms = 5000
pos = Position()
pos.fromFen("rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1")
search = Search(pos, 16)

choice = input("你想要： \n\t1. 执红先行\n\t2. 执黑后行\n\t 请选择:\n")
assert(choice in ["1","2"])
mov = None
if choice == "2":
    mov = search.searchMain(64, search_time_ms) # 搜索3秒钟
    pos.makeMove(mov)

while True:
    print_board(pos)

    # 人来下棋
    if mov:
        print("电脑的上一步：",move2Iccs(mov).replace("-","").lower())
    hintmov = search.searchMain(64, 10) # 搜索10毫秒，给出例子
    while True:
        user_step = input("请输入你的行棋步子，比如 " + move2Iccs(hintmov).replace("-","").lower() + " \n" + \
                          "悔棋请输入 shameonme :\n").upper()
        if user_step == "shameonme".upper():
            mov = None
            pos.undoMakeMove()
            pos.undoMakeMove()
            break
        if len(user_step) == 4:
            user_step = user_step[:2] + "-" + user_step[2:]
        try:
            user_move = Iccs2move(user_step)
            assert(pos.legalMove(user_move))
        except:
            print("你的行棋不合法，请重新输入")
            continue
        pos.makeMove(user_move)
        break

    if user_step != "shameonme".upper():
        # 电脑下棋
        mov = search.searchMain(64, search_time_ms) # 搜索3秒钟
        pos.makeMove(mov)
