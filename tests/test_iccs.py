from XQlightPy.cchess import move2Iccs,Iccs2move

def test_iccs():
    assert(move2Iccs(43466) == "H0-G2")
    assert(Iccs2move("H0-G2") == 43466)

def test_moves():
    moves  = """
    g3-g4
    g6-g5
    b0-c2
    h7-h0
    e3-e4
    d9-e8
    e1-e2
    c6-c5
    """.upper()
    for one_move in moves.split("\n"):
        one_move = one_move.strip()
        if not one_move:
            continue
        assert(move2Iccs(Iccs2move(one_move)) == one_move)
