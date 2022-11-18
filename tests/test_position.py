from XQlightPy.position import Position,RC4
import numpy as np

def test_genmove():
    pos = Position()
    pos.clearBoard()
    pos.fromFen("9/2Cca4/3k1C3/4P1p2/4N1b2/4R1r2/4c1n2/3p1n3/2rNK4/9 w")
    res_correct = np.asarray(
        [13637, 17477, 17221, 18245, 21829, 25925, 30021, 34117, 38213, 42309, 18520, 14424, 22360, 22872, 23128, 23384,
         26712, 30808, 34904, 39000, 22375, 26215, 26727, 25975, 34167, 26999, 35191, 34439, 34183, 33927, 33671, 34951,
         35207, 38791, 42935, 47287, 51127]
    )
    moves_res = pos.generateMoves()
    assert(len(moves_res) == 37)
    assert(np.all(res_correct == np.asarray(moves_res)))
    assert(pos.checked() == False)
    assert(pos.bookMove() == 0)

def test_rc4():
    rc4 = RC4([0])
    correct_res = np.asarray([0, 35, 3, 43, 9, 11, 65, 229, 32, 36, 134, 98, 59, 34, 173, 153, 214, 200, 64, 161, 191, 62, 6, 25, 56, 234, 49, 246, 69, 133, 203, 194, 10, 42, 228, 198, 195, 245, 236, 91, 206, 23, 235, 27, 138, 18, 143, 250, 244, 76, 123, 217, 132, 249, 72, 127, 94, 151, 33, 60, 248, 85, 177, 210, 142, 83, 110, 140, 41, 135, 196, 238, 156, 242, 141, 67, 5, 185, 131, 63, 137, 37, 172, 121, 70, 144, 237, 130, 17, 44, 253, 166, 78, 201, 12, 119, 215, 7, 126, 114])
    assert(np.all(rc4.state[:len(correct_res)] == correct_res))
    assert(rc4.nextByte() == 222)
    assert(rc4.nextByte() == 24)
    assert(rc4.nextLong() == 933446025)
    assert(rc4.nextLong() == 109722205)

    rc4 = RC4([0])
    assert(rc4.nextLong() == 1099503838)
    assert(rc4.nextLong() == 979187619)
    assert(rc4.nextLong() == 1730021002)
    assert(rc4.nextLong() == 1838313047)
    assert(rc4.nextLong() == -1551951161)
    assert(rc4.nextLong() == -1746154256)


def test_pos_book():
    pos = Position()
    pos.clearBoard()
    pos.fromFen("rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1")
    res_correct = np.asarray(
        [33683, 34197, 34711, 35225, 35739, 38052, 33956, 29860, 25764, 13476, 41892, 42404, 42660, 42916, 43172, 43428,
         46244, 39594, 35498, 31402, 27306, 15018, 43434, 43178, 42922, 42666, 42410, 43946, 47786, 46019, 41923, 41924,
         42436, 41925, 42949, 47046, 47047, 47048, 42953, 43977, 43466, 43978, 48075, 43979]
    )
    for i in range(100):
        assert(pos.bookMove() != 0)
    pos_actions = pos.generateMoves(None)
    assert(len(pos_actions) == 44)
    assert(np.all(res_correct == np.asarray(pos_actions)))
    assert(pos.zobristKey == -421837250)
    assert(pos.zobristLock == 86398677)

    pos = Position()
    pos.fromFen("9/2Cca4/3k1C3/4P1p2/4N1b2/4R1r2/4c1n2/3p1n3/2rNK4/9 w")
    assert(pos.zobristKey == -1362866936)
    assert(pos.zobristLock == -554356577)

def test_a_few_step():
    pos = Position()
    pos.fromFen("rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1")

    mov = pos.generateMoves()[0]
    assert(mov == 33683)
    assert(pos.makeMove(mov))

    mov = pos.generateMoves()[0]
    assert(mov == 17203)
    assert(pos.makeMove(mov))

    mov = pos.generateMoves()[0]
    assert(mov == 29571)
    assert(pos.makeMove(mov))

    assert(pos.zobristKey == -513434690)
    assert(pos.zobristLock == -1428449623)
    assert(pos.checked() == False)

    mov = pos.generateMoves()[0]
    assert(pos.legalMove(mov) == True)
    assert(pos.legalMove(mov + 20) == False)

