from XQlightPy.search import shellSort,Search
from XQlightPy.position import Position
import numpy as np


def test_shellsort():
    a = [np.random.randint(0, 1000) for i in range(1000)]
    b = [i for i in a]
    shellSort(a, b)
    for i in range(len(b) - 1):
        assert (b[i + 1] <= b[i])
        assert(a[i] == b[i])

def test_search_pos1():
    pos = Position()
    pos.fromFen("9/2Cca4/3k1C3/4P1p2/4N1b2/4R1r2/4c1n2/3p1n3/2rNK4/9 w")
    search = Search(pos, 16)
    mov = search.searchMain(64,1000)
    assert(mov == 26215)

def test_search_pos2():
    pos = Position()
    pos.fromFen("1nbakabnr/r8/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K3R/RNBA1ABN1 w - - 0 1")
    search = Search(pos, 16)
    mov = search.searchMain(64,3000)
    print("test_search_pos2 mov:",mov)
    assert(mov != 0)


if __name__ == "__main__":
    test_search_pos2()