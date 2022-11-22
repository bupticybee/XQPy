import math
import random
from XQlightPy.book import BOOK_DAT


def binarySearch(vlss, vl):
    low = 0
    high = len(vlss) - 1
    while (low <= high):
        mid = (low + high) >> 1
        if (vlss[mid][0] < vl):
            low = mid + 1
        elif (vlss[mid][0] > vl):
            high = mid - 1
        else:
            return mid
    return -1


MATE_VALUE = 10000
BAN_VALUE = MATE_VALUE - 100
WIN_VALUE = MATE_VALUE - 200
NULL_SAFE_MARGIN = 400
NULL_OKAY_MARGIN = 200
DRAW_VALUE = 20
ADVANCED_VALUE = 3

PIECE_KING = 0
PIECE_ADVISOR = 1
PIECE_BISHOP = 2
PIECE_KNIGHT = 3
PIECE_ROOK = 4
PIECE_CANNON = 5
PIECE_PAWN = 6

RANK_TOP = 3
RANK_BOTTOM = 12
FILE_LEFT = 3
FILE_RIGHT = 11

ADD_PIECE = False
DEL_PIECE = True

IN_BOARD_ = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

IN_FORT_ = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

LEGAL_SPAN = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
]

KNIGHT_PIN_ = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -16, 0, -16, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 16, 0, 16, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
]

KING_DELTA = [-16, -1, 1, 16]
ADVISOR_DELTA = [-17, -15, 15, 17]
KNIGHT_DELTA = [[-33, -31], [-18, 14], [-14, 18], [31, 33]]
KNIGHT_CHECK_DELTA = [[-33, -18], [-31, -14], [14, 31], [18, 33]]
MVV_VALUE = [50, 10, 10, 30, 40, 30, 20, 0]

PIECE_VALUE = [
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 9, 9, 9, 11, 13, 11, 9, 9, 9, 0, 0, 0, 0,
        0, 0, 0, 19, 24, 34, 42, 44, 42, 34, 24, 19, 0, 0, 0, 0,
        0, 0, 0, 19, 24, 32, 37, 37, 37, 32, 24, 19, 0, 0, 0, 0,
        0, 0, 0, 19, 23, 27, 29, 30, 29, 27, 23, 19, 0, 0, 0, 0,
        0, 0, 0, 14, 18, 20, 27, 29, 27, 20, 18, 14, 0, 0, 0, 0,
        0, 0, 0, 7, 0, 13, 0, 16, 0, 13, 0, 7, 0, 0, 0, 0,
        0, 0, 0, 7, 0, 7, 0, 15, 0, 7, 0, 7, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 11, 15, 11, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 20, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 18, 0, 0, 20, 23, 20, 0, 0, 18, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 20, 20, 0, 20, 20, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 20, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 18, 0, 0, 20, 23, 20, 0, 0, 18, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 20, 20, 0, 20, 20, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 90, 90, 90, 96, 90, 96, 90, 90, 90, 0, 0, 0, 0,
        0, 0, 0, 90, 96, 103, 97, 94, 97, 103, 96, 90, 0, 0, 0, 0,
        0, 0, 0, 92, 98, 99, 103, 99, 103, 99, 98, 92, 0, 0, 0, 0,
        0, 0, 0, 93, 108, 100, 107, 100, 107, 100, 108, 93, 0, 0, 0, 0,
        0, 0, 0, 90, 100, 99, 103, 104, 103, 99, 100, 90, 0, 0, 0, 0,
        0, 0, 0, 90, 98, 101, 102, 103, 102, 101, 98, 90, 0, 0, 0, 0,
        0, 0, 0, 92, 94, 98, 95, 98, 95, 98, 94, 92, 0, 0, 0, 0,
        0, 0, 0, 93, 92, 94, 95, 92, 95, 94, 92, 93, 0, 0, 0, 0,
        0, 0, 0, 85, 90, 92, 93, 78, 93, 92, 90, 85, 0, 0, 0, 0,
        0, 0, 0, 88, 85, 90, 88, 90, 88, 90, 85, 88, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 206, 208, 207, 213, 214, 213, 207, 208, 206, 0, 0, 0, 0,
        0, 0, 0, 206, 212, 209, 216, 233, 216, 209, 212, 206, 0, 0, 0, 0,
        0, 0, 0, 206, 208, 207, 214, 216, 214, 207, 208, 206, 0, 0, 0, 0,
        0, 0, 0, 206, 213, 213, 216, 216, 216, 213, 213, 206, 0, 0, 0, 0,
        0, 0, 0, 208, 211, 211, 214, 215, 214, 211, 211, 208, 0, 0, 0, 0,
        0, 0, 0, 208, 212, 212, 214, 215, 214, 212, 212, 208, 0, 0, 0, 0,
        0, 0, 0, 204, 209, 204, 212, 214, 212, 204, 209, 204, 0, 0, 0, 0,
        0, 0, 0, 198, 208, 204, 212, 212, 212, 204, 208, 198, 0, 0, 0, 0,
        0, 0, 0, 200, 208, 206, 212, 200, 212, 206, 208, 200, 0, 0, 0, 0,
        0, 0, 0, 194, 206, 204, 212, 200, 212, 204, 206, 194, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 100, 100, 96, 91, 90, 91, 96, 100, 100, 0, 0, 0, 0,
        0, 0, 0, 98, 98, 96, 92, 89, 92, 96, 98, 98, 0, 0, 0, 0,
        0, 0, 0, 97, 97, 96, 91, 92, 91, 96, 97, 97, 0, 0, 0, 0,
        0, 0, 0, 96, 99, 99, 98, 100, 98, 99, 99, 96, 0, 0, 0, 0,
        0, 0, 0, 96, 96, 96, 96, 100, 96, 96, 96, 96, 0, 0, 0, 0,
        0, 0, 0, 95, 96, 99, 96, 100, 96, 99, 96, 95, 0, 0, 0, 0,
        0, 0, 0, 96, 96, 96, 96, 96, 96, 96, 96, 96, 0, 0, 0, 0,
        0, 0, 0, 97, 96, 100, 99, 101, 99, 100, 96, 97, 0, 0, 0, 0,
        0, 0, 0, 96, 97, 98, 98, 98, 98, 98, 97, 96, 0, 0, 0, 0,
        0, 0, 0, 96, 96, 97, 99, 99, 99, 97, 96, 96, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 9, 9, 9, 11, 13, 11, 9, 9, 9, 0, 0, 0, 0,
        0, 0, 0, 19, 24, 34, 42, 44, 42, 34, 24, 19, 0, 0, 0, 0,
        0, 0, 0, 19, 24, 32, 37, 37, 37, 32, 24, 19, 0, 0, 0, 0,
        0, 0, 0, 19, 23, 27, 29, 30, 29, 27, 23, 19, 0, 0, 0, 0,
        0, 0, 0, 14, 18, 20, 27, 29, 27, 20, 18, 14, 0, 0, 0, 0,
        0, 0, 0, 7, 0, 13, 0, 16, 0, 13, 0, 7, 0, 0, 0, 0,
        0, 0, 0, 7, 0, 7, 0, 15, 0, 7, 0, 7, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 11, 15, 11, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ],
]


def IN_BOARD(sq):
    return IN_BOARD_[sq] != 0


def IN_FORT(sq):
    return IN_FORT_[sq] != 0


def RANK_Y(sq):
    return sq >> 4


def FILE_X(sq):
    return sq & 15


def COORD_XY(x, y):
    return x + (y << 4)


def SQUARE_FLIP(sq):
    return 254 - sq


def FILE_FLIP(x):
    return 14 - x


def RANK_FLIP(y):
    return 15 - y


def MIRROR_SQUARE(sq):
    return COORD_XY(FILE_FLIP(FILE_X(sq)), RANK_Y(sq))


def SQUARE_FORWARD(sq, sd):
    return sq - 16 + (sd << 5)


def KING_SPAN(sqSrc, sqDst):
    return LEGAL_SPAN[sqDst - sqSrc + 256] == 1


def ADVISOR_SPAN(sqSrc, sqDst):
    return LEGAL_SPAN[sqDst - sqSrc + 256] == 2


def BISHOP_SPAN(sqSrc, sqDst):
    return LEGAL_SPAN[sqDst - sqSrc + 256] == 3


def BISHOP_PIN(sqSrc, sqDst):
    return (sqSrc + sqDst) >> 1


def KNIGHT_PIN(sqSrc, sqDst):
    return sqSrc + KNIGHT_PIN_[sqDst - sqSrc + 256]


def HOME_HALF(sq, sd):
    return (sq & 0x80) != (sd << 7)


def AWAY_HALF(sq, sd):
    return (sq & 0x80) == (sd << 7)


def SAME_HALF(sqSrc, sqDst):
    return ((sqSrc ^ sqDst) & 0x80) == 0


def SAME_RANK(sqSrc, sqDst):
    return ((sqSrc ^ sqDst) & 0xf0) == 0


def SAME_FILE(sqSrc, sqDst):
    return ((sqSrc ^ sqDst) & 0x0f) == 0


def SIDE_TAG(sd):
    return 8 + (sd << 3)


def OPP_SIDE_TAG(sd):
    return 16 - (sd << 3)


def SRC(mv):
    return mv & 255


def DST(mv):
    return mv >> 8


def MOVE(sqSrc, sqDst):
    return sqSrc + (sqDst << 8)


def MIRROR_MOVE(mv):
    return MOVE(MIRROR_SQUARE(SRC(mv)), MIRROR_SQUARE(DST(mv)))


def MVV_LVA(pc, lva):
    return MVV_VALUE[pc & 7] - lva


def CHR(n):
    return chr(n)


def ASC(c):
    return ord(c)


FEN_PIECE = "        KABNRCP kabnrcp "


def CHAR_TO_PIECE(c):
    if c == "K":
        return PIECE_KING
    elif c == "A":
        return PIECE_ADVISOR
    elif c == "B":
        return PIECE_BISHOP
    elif c == "E":
        return PIECE_BISHOP
    elif c == "H":
        return PIECE_KNIGHT
    elif c == "N":
        return PIECE_KNIGHT
    elif c == "R":
        return PIECE_ROOK
    elif c == "C":
        return PIECE_CANNON
    elif c == "P":
        return PIECE_PAWN
    else:
        return -1


def unsinged_right_shift(x, y):
    x = x & 0xffffffff
    signed = False
    if x < 0:
        signed = True
    x = x.to_bytes(4, byteorder='big', signed=signed)  # 有符号
    x = int.from_bytes(x, byteorder='big', signed=False)  # 无符号
    return x >> (y & 0xf)


class RC4:
    def __init__(self, key):
        self.x = self.y = 0
        self.state = []
        for i in range(256):
            self.state.append(i)
        j = 0
        for i in range(256):
            j = (j + self.state[i] + key[i % len(key)]) & 0xff
            self.swap(i, j)

    def swap(self, i, j):
        t = self.state[i]
        self.state[i] = self.state[j]
        self.state[j] = t

    def nextByte(self):
        self.x = (self.x + 1) & 0xff
        self.y = (self.y + self.state[self.x]) & 0xff
        self.swap(self.x, self.y)
        t = (self.state[self.x] + self.state[self.y]) & 0xff
        return self.state[t]

    def nextLong(self):
        n0 = self.nextByte()
        n1 = self.nextByte()
        n2 = self.nextByte()
        n3 = self.nextByte()
        return ((n0 + (n1 << 8) + (n2 << 16) + ((n3 << 24) & 0xffffffff)) + 2147483648) % 4294967296 - 2147483648


PreGen_zobristKeyPlayer = None
PreGen_zobristLockPlayer = None
PreGen_zobristKeyTable = []
PreGen_zobristLockTable = []

rc4 = RC4([0])

PreGen_zobristKeyPlayer = rc4.nextLong()
rc4.nextLong()
PreGen_zobristLockPlayer = rc4.nextLong()

for i in range(14):
    keys = []
    locks = []
    for j in range(256):
        keys.append(rc4.nextLong())
        rc4.nextLong()
        locks.append(rc4.nextLong())
    PreGen_zobristKeyTable.append(keys)
    PreGen_zobristLockTable.append(locks)


class Position():
    def __init__(self):
        pass

    def clearBoard(self):
        self.sdPlayer = 0
        self.squares = []
        for j in range(256):
            self.squares.append(0)
        self.zobristKey = self.zobristLock = 0
        self.vlWhite = self.vlBlack = 0

    def setIrrev(self):
        self.mvList = [0]
        self.pcList = [0]
        self.keyList = [0]
        self.chkList = [self.checked()]
        self.distance = 0

    def addPiece(self, sq, pc, bDel=None):
        self.squares[sq] = (0 if bDel else pc)
        if (pc < 16):
            pcAdjust = pc - 8
            self.vlWhite += (-PIECE_VALUE[pcAdjust][sq] if bDel else PIECE_VALUE[pcAdjust][sq])
        else:
            pcAdjust = pc - 16
            self.vlBlack += (
                -PIECE_VALUE[pcAdjust][SQUARE_FLIP(sq)] if bDel else PIECE_VALUE[pcAdjust][SQUARE_FLIP(sq)])
            pcAdjust += 7
        #print(PreGen_zobristKeyTable[pcAdjust])
        self.zobristKey ^= PreGen_zobristKeyTable[pcAdjust][sq]
        self.zobristLock ^= PreGen_zobristLockTable[pcAdjust][sq]

    def movePiece(self, mv):
        sqSrc = SRC(mv)
        sqDst = DST(mv)
        pc = self.squares[sqDst]
        self.pcList.append(pc)
        if (pc > 0):
            self.addPiece(sqDst, pc, DEL_PIECE)
        pc = self.squares[sqSrc]
        self.addPiece(sqSrc, pc, DEL_PIECE)
        self.addPiece(sqDst, pc, ADD_PIECE)
        self.mvList.append(mv)

    def undoMovePiece(self):
        mv = self.mvList.pop()
        sqSrc = SRC(mv)
        sqDst = DST(mv)
        pc = self.squares[sqDst]
        self.addPiece(sqDst, pc, DEL_PIECE)
        self.addPiece(sqSrc, pc, ADD_PIECE)
        pc = self.pcList.pop()
        if (pc > 0):
            self.addPiece(sqDst, pc, ADD_PIECE)

    def changeSide(self):
        self.sdPlayer = 1 - self.sdPlayer
        self.zobristKey ^= PreGen_zobristKeyPlayer
        self.zobristLock ^= PreGen_zobristLockPlayer

    def makeMove(self, mv):
        zobristKey = self.zobristKey
        self.movePiece(mv)
        if (self.checked()):
            self.undoMovePiece()
            return False
        self.keyList.append(zobristKey)
        self.changeSide()
        self.chkList.append(self.checked())
        self.distance += 1
        return True

    def undoMakeMove(self):
        self.distance -= 1
        self.chkList.pop()
        self.changeSide()
        self.keyList.pop()
        self.undoMovePiece()

    def nullMove(self):
        self.mvList.append(0)
        self.pcList.append(0)
        self.keyList.append(self.zobristKey)
        self.changeSide()
        self.chkList.append(False)
        self.distance += 1

    def undoNullMove(self):
        self.distance -= 1
        self.chkList.pop()
        self.changeSide()
        self.keyList.pop()
        self.pcList.pop()
        self.mvList.pop()

    def fromFen(self, fen):
        self.clearBoard()
        y = RANK_TOP
        x = FILE_LEFT
        index = 0
        if (index == len(fen)):
            self.setIrrev()
            return

        c = fen[index]
        while (c != " "):
            if (c == "/"):
                x = FILE_LEFT
                y += 1
                if (y > RANK_BOTTOM):
                    break
            elif (c >= "1" and c <= "9"):
                x += (ASC(c) - ASC("0"))
            elif (c >= "A" and c <= "Z"):
                if (x <= FILE_RIGHT):
                    pt = CHAR_TO_PIECE(c)
                    if (pt >= 0):
                        self.addPiece(COORD_XY(x, y), pt + 8)
                    x += 1

            elif (c >= "a" and c <= "z"):
                if (x <= FILE_RIGHT):
                    pt = CHAR_TO_PIECE(CHR(ASC(c) + ASC("A") - ASC("a")))
                    if (pt >= 0):
                        self.addPiece(COORD_XY(x, y), pt + 16)
                    x += 1

            index += 1
            if index == len(fen):
                self.setIrrev()
                return
            c = fen[index]
        index += 1
        if index == len(fen):
            self.setIrrev()
            return
        if (self.sdPlayer == (
                0 if fen[index] == "b" else 1
        )):
            self.changeSide()
        self.setIrrev()

    def toFen(self):
        fen = ""
        for y in range(RANK_TOP, RANK_BOTTOM + 1):
            k = 0
            for x in range(FILE_LEFT, FILE_RIGHT + 1):
                pc = self.squares[COORD_XY(x, y)]
                if (pc > 0):
                    if (k > 0):
                        fen += CHR(ASC("0") + k)
                        k = 0
                    fen += FEN_PIECE[pc]
                else:
                    k += 1
            if (k > 0):
                fen += CHR(ASC("0") + k)
            fen += "/"
        return fen[0: len(fen) - 1] + (" w" if self.sdPlayer == 0 else " b")

    def generateMoves(self, vls=None):
        mvs = []
        pcSelfSide = SIDE_TAG(self.sdPlayer)
        pcOppSide = OPP_SIDE_TAG(self.sdPlayer)
        for sqSrc in range(256):
            pcSrc = self.squares[sqSrc]
            if (pcSrc & pcSelfSide) == 0:
                continue
            switchcase = pcSrc - pcSelfSide
            if switchcase == PIECE_KING:
                for i in range(4):
                    sqDst = sqSrc + KING_DELTA[i]
                    if not IN_FORT(sqDst):
                        continue
                    pcDst = self.squares[sqDst]
                    if vls is None:
                        if (pcDst & pcSelfSide) == 0:
                            mvs.append(MOVE(sqSrc, sqDst))
                    elif (pcDst & pcOppSide) != 0:
                        mvs.append(MOVE(sqSrc, sqDst))
                        vls.append(MVV_LVA(pcDst, 5))
            elif switchcase == PIECE_ADVISOR:
                for i in range(4):
                    sqDst = sqSrc + ADVISOR_DELTA[i]
                    if not IN_FORT(sqDst):
                        continue
                    pcDst = self.squares[sqDst]
                    if vls is None:
                        if (pcDst & pcSelfSide) == 0:
                            mvs.append(MOVE(sqSrc, sqDst))
                    elif (pcDst & pcOppSide) != 0:
                        mvs.append(MOVE(sqSrc, sqDst))
                        vls.append(MVV_LVA(pcDst, 1))
            elif switchcase == PIECE_BISHOP:
                for i in range(4):
                    sqDst = sqSrc + ADVISOR_DELTA[i]
                    if (not (IN_BOARD(sqDst) and HOME_HALF(sqDst, self.sdPlayer) and
                             self.squares[sqDst] == 0)):
                        continue
                    sqDst += ADVISOR_DELTA[i]
                    pcDst = self.squares[sqDst]
                    if vls is None:
                        if (pcDst & pcSelfSide) == 0:
                            mvs.append(MOVE(sqSrc, sqDst))
                    elif (pcDst & pcOppSide) != 0:
                        mvs.append(MOVE(sqSrc, sqDst))
                        vls.append(MVV_LVA(pcDst, 1))
            elif switchcase == PIECE_KNIGHT:
                for i in range(4):
                    sqDst = sqSrc + KING_DELTA[i]
                    if self.squares[sqDst] > 0:
                        continue
                    for j in range(2):
                        sqDst = sqSrc + KNIGHT_DELTA[i][j]
                        if not IN_BOARD(sqDst):
                            continue
                        pcDst = self.squares[sqDst]
                        if vls is None:
                            if (pcDst & pcSelfSide) == 0:
                                mvs.append(MOVE(sqSrc, sqDst))
                        elif (pcDst & pcOppSide) != 0:
                            mvs.append(MOVE(sqSrc, sqDst))
                            vls.append(MVV_LVA(pcDst, 1))
            elif switchcase == PIECE_ROOK:
                for i in range(4):
                    delta = KING_DELTA[i]
                    sqDst = sqSrc + delta
                    while IN_BOARD(sqDst):
                        pcDst = self.squares[sqDst]
                        if pcDst == 0:
                            if vls is None:
                                mvs.append(MOVE(sqSrc, sqDst))
                        else:
                            if (pcDst & pcOppSide) != 0:
                                mvs.append(MOVE(sqSrc, sqDst))
                                if vls is not None:
                                    vls.append(MVV_LVA(pcDst, 4))
                            break
                        sqDst += delta
            elif switchcase == PIECE_CANNON:
                for i in range(4):
                    delta = KING_DELTA[i]
                    sqDst = sqSrc + delta
                    while IN_BOARD(sqDst):
                        pcDst = self.squares[sqDst]
                        if pcDst == 0:
                            if vls is None:
                                mvs.append(MOVE(sqSrc, sqDst))
                        else:
                            break
                        sqDst += delta
                    sqDst += delta
                    while IN_BOARD(sqDst):
                        pcDst = self.squares[sqDst]
                        if pcDst > 0:
                            if (pcDst & pcOppSide) != 0:
                                mvs.append(MOVE(sqSrc, sqDst))
                                if vls is not None:
                                    vls.append(MVV_LVA(pcDst, 4))
                            break
                        sqDst += delta
            elif switchcase == PIECE_PAWN:
                sqDst = SQUARE_FORWARD(sqSrc, self.sdPlayer)
                if IN_BOARD(sqDst):
                    pcDst = self.squares[sqDst]
                    if vls is None:
                        if (pcDst & pcSelfSide) == 0:
                            mvs.append(MOVE(sqSrc, sqDst))
                    elif (pcDst & pcOppSide) != 0:
                        mvs.append(MOVE(sqSrc, sqDst))
                        vls.append(MVV_LVA(pcDst, 2))
                if AWAY_HALF(sqSrc, self.sdPlayer):
                    for delta in range(-1, 1 + 1, 2):
                        sqDst = sqSrc + delta
                        if (IN_BOARD(sqDst)):
                            pcDst = self.squares[sqDst]
                            if (vls is None):
                                if (pcDst & pcSelfSide) == 0:
                                    mvs.append(MOVE(sqSrc, sqDst))
                            elif (pcDst & pcOppSide) != 0:
                                mvs.append(MOVE(sqSrc, sqDst))
                                vls.append(MVV_LVA(pcDst, 2))
        return mvs

    def legalMove(self, mv):
        sqSrc = SRC(mv)
        pcSrc = self.squares[sqSrc]

        pcSelfSide = SIDE_TAG(self.sdPlayer)
        if (pcSrc & pcSelfSide) == 0:
            return False
        sqDst = DST(mv)

        pcDst = self.squares[sqDst]
        if (pcDst & pcSelfSide) != 0:
            return False

        switchcase = pcSrc - pcSelfSide
        if switchcase == PIECE_KING:
            return IN_FORT(sqDst) and KING_SPAN(sqSrc, sqDst)
        elif switchcase == PIECE_ADVISOR:
            return IN_FORT(sqDst) and ADVISOR_SPAN(sqSrc, sqDst)
        elif switchcase == PIECE_BISHOP:
            return SAME_HALF(sqSrc, sqDst) and BISHOP_SPAN(sqSrc, sqDst) and \
                   self.squares[BISHOP_PIN(sqSrc, sqDst)] == 0
        elif switchcase == PIECE_KNIGHT:
            sqPin = KNIGHT_PIN(sqSrc, sqDst)
            return sqPin != sqSrc and self.squares[sqPin] == 0
        elif switchcase == PIECE_ROOK or switchcase == PIECE_CANNON:
            if SAME_RANK(sqSrc, sqDst):
                delta = (-1 if sqDst < sqSrc else 1)
            elif SAME_FILE(sqSrc, sqDst):
                delta = (-16 if sqDst < sqSrc else 16)
            else:
                return False

            sqPin = sqSrc + delta
            while sqPin != sqDst and self.squares[sqPin] == 0:
                sqPin += delta
            if sqPin == sqDst:
                return pcDst == 0 or pcSrc - pcSelfSide == PIECE_ROOK
            if pcDst == 0 or pcSrc - pcSelfSide != PIECE_CANNON:
                return False
            sqPin += delta
            while sqPin != sqDst and self.squares[sqPin] == 0:
                sqPin += delta
            return sqPin == sqDst
        elif switchcase == PIECE_PAWN:
            if AWAY_HALF(sqDst, self.sdPlayer) and (sqDst == sqSrc - 1 or sqDst == sqSrc + 1):
                return True
            return sqDst == SQUARE_FORWARD(sqSrc, self.sdPlayer)
        else:
            return False

    def checked(self):
        pcSelfSide = SIDE_TAG(self.sdPlayer)
        pcOppSide = OPP_SIDE_TAG(self.sdPlayer)
        for sqSrc in range(0, 256):
            if self.squares[sqSrc] != pcSelfSide + PIECE_KING:
                continue
            if self.squares[SQUARE_FORWARD(sqSrc, self.sdPlayer)] == pcOppSide + PIECE_PAWN:
                return True
            for delta in range(-1, 1 + 1, 2):
                if self.squares[sqSrc + delta] == pcOppSide + PIECE_PAWN:
                    return True
            for i in range(4):
                if self.squares[sqSrc + ADVISOR_DELTA[i]] != 0:
                    continue
                for j in range(2):
                    pcDst = self.squares[sqSrc + KNIGHT_CHECK_DELTA[i][j]]
                    if pcDst == pcOppSide + PIECE_KNIGHT:
                        return True
            for i in range(4):
                delta = KING_DELTA[i]
                sqDst = sqSrc + delta
                while IN_BOARD(sqDst):
                    pcDst = self.squares[sqDst]
                    if pcDst > 0:
                        if pcDst == pcOppSide + PIECE_ROOK or pcDst == pcOppSide + PIECE_KING:
                            return True
                        break
                    sqDst += delta
                sqDst += delta
                while IN_BOARD(sqDst):
                    pcDst = self.squares[sqDst]
                    if pcDst > 0:
                        if pcDst == pcOppSide + PIECE_CANNON:
                            return True
                        break
                    sqDst += delta
            return False
        return False

    def isMate(self):
        mvs = self.generateMoves(None)
        for i in range(len(mvs)):
            if self.makeMove(mvs[i]):
                self.undoMakeMove()
                return False
        return True

    def mateValue(self):
        return self.distance - MATE_VALUE

    def banValue(self):
        return self.distance - BAN_VALUE

    def drawValue(self):
        return -DRAW_VALUE if (self.distance & 1) == 0 else DRAW_VALUE

    def evaluate(self):
        vl = (self.vlWhite - self.vlBlack if self.sdPlayer == 0 else self.vlBlack - self.vlWhite) + ADVANCED_VALUE
        return (vl - 1) if vl == self.drawValue() else vl

    def nullOkay(self):
        return (self.vlWhite if self.sdPlayer == 0 else self.vlBlack) > NULL_OKAY_MARGIN

    def nullSafe(self):
        return (self.vlWhite if self.sdPlayer == 0 else self.vlBlack) > NULL_SAFE_MARGIN

    def inCheck(self):
        return self.chkList[len(self.chkList) - 1]

    def captured(self):
        return self.pcList[len(self.pcList) - 1] > 0

    def repValue(self, vlRep):
        vlReturn = (0 if (vlRep & 2) == 0 else self.banValue()) + \
                   (0 if (vlRep & 4) == 0 else -self.banValue())

        return self.drawValue() if vlReturn == 0 else vlReturn

    def repStatus(self, recur_):
        recur = recur_
        selfSide = False
        perpCheck = True
        oppPerpCheck = True
        index = len(self.mvList) - 1
        while self.mvList[index] > 0 and self.pcList[index] == 0:
            if selfSide:
                perpCheck = perpCheck and self.chkList[index]
                if self.keyList[index] == self.zobristKey:
                    recur -= 1
                    if recur == 0:
                        return 1 + (2 if perpCheck else 0) + (4 if oppPerpCheck else 0)
            else:
                oppPerpCheck = oppPerpCheck and self.chkList[index]
            selfSide = not selfSide
            index -= 1
        return 0

    def mirror(self):
        pos = Position()
        pos.clearBoard()
        for sq in range(256):
            pc = self.squares[sq]
            if pc > 0:
                pos.addPiece(MIRROR_SQUARE(sq), pc)
        if self.sdPlayer == 1:
            pos.changeSide()
        return pos

    def bookMove(self):
        if BOOK_DAT is None or len(BOOK_DAT) == 0:
            return 0
        mirror = False
        lock = unsinged_right_shift(self.zobristLock, 1)  # Convert into Unsigned
        index = binarySearch(BOOK_DAT, lock)
        if index < 0:
            mirror = True
            lock = unsinged_right_shift(self.mirror().zobristLock, 1)  # Convert into Unsigned
            index = binarySearch(BOOK_DAT, lock)
        if index < 0:
            return 0
        index -= 1
        while index >= 0 and BOOK_DAT[index][0] == lock:
            index -= 1
        mvs = []
        vls = []
        value = 0
        index += 1
        while index < len(BOOK_DAT) and BOOK_DAT[index][0] == lock:
            mv = BOOK_DAT[index][1]
            mv = (MIRROR_MOVE(mv) if mirror else mv)
            if self.legalMove(mv):
                mvs.append(mv)
                vl = BOOK_DAT[index][2]
                vls.append(vl)
                value += vl
            index += 1
        if value == 0:
            return 0
        value = math.floor(random.random() * value)
        for index in range(len(mvs)):
            value -= vls[index]
            if value < 0:
                break
        return mvs[index]

    def historyIndex(self,mv):
        return ((self.squares[SRC(mv)] - 8) << 8) + DST(mv)


    def winner(self):
        if self.isMate():
            return 1 - self.sdPlayer
        pc = SIDE_TAG(self.sdPlayer) + PIECE_KING
        sqMate = 0
        for sq in range(256):
            if self.squares[sq] == pc:
                sqMate = sq
                break
        if sqMate == 0:
            return 1 - self.sdPlayer

        vlRep = self.repStatus(3)
        if (vlRep > 0):
            vlRep = self.repValue(vlRep)
            if -WIN_VALUE < vlRep < WIN_VALUE:
                #双方不变作和
                return 2
            else:
                #长打作负
                return self.sdPlayer

        hasMaterial = False
        for sq in range(256):
            if IN_BOARD(sq) and (self.squares[sq] & 7) > 2:
                hasMaterial = True
                break;
        if (not hasMaterial) :
            # 无进攻子力做和
            return 2
        return
