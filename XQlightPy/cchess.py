from XQlightPy.position import CHR,ASC,FILE_X,RANK_Y,FILE_LEFT,RANK_TOP,SRC,DST

def move2Iccs(mv):
    sqSrc = SRC(mv)
    sqDst = DST(mv)
    return CHR(ASC("A") + FILE_X(sqSrc) - FILE_LEFT) + \
        CHR(ASC("9") - RANK_Y(sqSrc) + RANK_TOP) + "-" + \
        CHR(ASC("A") + FILE_X(sqDst) - FILE_LEFT) + \
        CHR(ASC("9") - RANK_Y(sqDst) + RANK_TOP)
