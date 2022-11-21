from XQlightPy.position import CHR,ASC,FILE_X,RANK_Y,FILE_LEFT,RANK_TOP,SRC,DST

def move2Iccs(mv):
    sqSrc = SRC(mv)
    sqDst = DST(mv)
    return CHR(ASC("A") + FILE_X(sqSrc) - FILE_LEFT) + \
        CHR(ASC("9") - RANK_Y(sqSrc) + RANK_TOP) + "-" + \
        CHR(ASC("A") + FILE_X(sqDst) - FILE_LEFT) + \
        CHR(ASC("9") - RANK_Y(sqDst) + RANK_TOP)

def cord2uint8(cord):
    alphabet = ASC(cord[0]) - ASC("A") + FILE_LEFT
    numeric = ASC("9") - ASC(cord[1]) + RANK_TOP
    return (numeric << 4) + alphabet

def Iccs2move(iccs):
    part1 = cord2uint8(iccs[3:])
    part2 = cord2uint8(iccs[:2])
    return (part1 << 8) + part2