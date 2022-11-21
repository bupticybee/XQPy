from XQlightPy.position import MATE_VALUE, WIN_VALUE, BAN_VALUE, HOME_HALF, DST
import math
import random
import time

SHELL_STEP = [0, 1, 4, 13, 40, 121, 364, 1093]

class HashTableObject:
    def __init__(self,depth,flag,vl,mv,zobristLock):
        self.depth = depth
        self.flag = flag
        self.vl = vl
        self.mv = mv
        self.zobristLock = zobristLock

def shellSort(mvs, vls):
    stepLevel = 1
    while SHELL_STEP[stepLevel] < len(mvs):
        stepLevel += 1
    stepLevel -= 1
    while stepLevel > 0:
        step = SHELL_STEP[stepLevel]
        for i in range(len(mvs)):
            mvBest = mvs[i]
            vlBest = vls[i]
            j = i - step
            while j >= 0 and vlBest > vls[j]:
                mvs[j + step] = mvs[j]
                vls[j + step] = vls[j]
                j -= step
            mvs[j + step] = mvBest
            vls[j + step] = vlBest
        stepLevel -= 1


PHASE_HASH = 0
PHASE_KILLER_1 = 1
PHASE_KILLER_2 = 2
PHASE_GEN_MOVES = 3
PHASE_REST = 4


class MoveSort:
    def __init__(self, mvHash, pos, killerTable, historyTable):
        self.mvs = []
        self.vls = []
        self.mvHash = 0
        self.mvKiller1 = 0
        self.mvKiller2 = 0
        self.pos = pos
        self.historyTable = historyTable
        self.phase = PHASE_HASH
        self.index = 0
        self.singleReply = False

        if pos.inCheck():
            self.phase = PHASE_REST
            mvsAll = pos.generateMoves(None)
            for i in range(len(mvsAll)):
                mv = mvsAll[i]
                if not pos.makeMove(mv):
                    continue
                pos.undoMakeMove()
                self.mvs.append(mv)
                self.vls.append(0x7fffffff if mv == mvHash else historyTable[pos.historyIndex(mv)])
            shellSort(self.mvs, self.vls)
            self.singleReply = (len(self.mvs) == 1)
        else:
            self.mvHash = mvHash
            self.mvKiller1 = killerTable[pos.distance][0]
            self.mvKiller2 = killerTable[pos.distance][1]

    def next(self):
        if self.phase == PHASE_HASH:
            self.phase = PHASE_KILLER_1
            if self.mvHash > 0:
                return self.mvHash
        if self.phase == PHASE_KILLER_1:
            self.phase = PHASE_KILLER_2
            if (self.mvKiller1 != self.mvHash and self.mvKiller1 > 0 and
                    self.pos.legalMove(self.mvKiller1)):
                return self.mvKiller1
        if self.phase == PHASE_KILLER_2:
            self.phase = PHASE_GEN_MOVES
            if (self.mvKiller2 != self.mvHash and self.mvKiller2 > 0 and
                    self.pos.legalMove(self.mvKiller2)):
                return self.mvKiller2
        if self.phase == PHASE_GEN_MOVES:
            self.phase = PHASE_REST
            self.mvs = self.pos.generateMoves(None)
            self.vls = []
            for i in range(len(self.mvs)):
                self.vls.append(self.historyTable[self.pos.historyIndex(self.mvs[i])])
            shellSort(self.mvs, self.vls)
            self.index = 0
        while self.index < len(self.mvs):
            mv = self.mvs[self.index]
            self.index += 1
            if mv != self.mvHash and mv != self.mvKiller1 and mv != self.mvKiller2:
                return mv
        return 0


LIMIT_DEPTH = 64
NULL_DEPTH = 2
RANDOMNESS = 8

HASH_ALPHA = 1
HASH_BETA = 2
HASH_PV = 3


class Search:
    def __init__(self, pos, hashLevel):
        self.hashMask = (1 << hashLevel) - 1
        self.pos = pos

    def getHashItem(self):
        return self.hashTable[self.pos.zobristKey & self.hashMask]

    def probeHash(self, vlAlpha, vlBeta, depth, mv):
        hash = self.getHashItem()
        if hash.zobristLock != self.pos.zobristLock:
            mv[0] = 0
            return -MATE_VALUE
        mv[0] = hash.mv

        mate = False
        if hash.vl > WIN_VALUE:
            if hash.vl <= BAN_VALUE:
                return -MATE_VALUE
            hash.vl -= self.pos.distance
            mate = True
        elif hash.vl < -WIN_VALUE:
            if hash.vl >= -BAN_VALUE:
                return -MATE_VALUE
            hash.vl += self.pos.distance
            mate = True
        elif hash.vl == self.pos.drawValue():
            return -MATE_VALUE
        if hash.depth < depth and not mate:
            return -MATE_VALUE
        if hash.flag == HASH_BETA:
            return hash.vl if hash.vl >= vlBeta else -MATE_VALUE
        if hash.flag == HASH_ALPHA:
            return hash.vl if hash.vl <= vlAlpha else -MATE_VALUE
        return hash.vl

    def recordHash(self, flag, vl, depth, mv):
        hash = self.getHashItem()
        if hash.depth > depth:
            return
        hash.flag = flag
        hash.depth = depth
        if vl > WIN_VALUE:
            if mv == 0 and vl <= BAN_VALUE:
                return
            hash.vl = vl + self.pos.distance
        elif vl < -WIN_VALUE:
            if mv == 0 and vl >= -BAN_VALUE:
                return
            hash.vl = vl - self.pos.distance
        elif vl == self.pos.drawValue() and mv == 0:
            return
        else:
            hash.vl = vl
        hash.mv = mv
        hash.zobristLock = self.pos.zobristLock

    def setBestMove(self, mv, depth):
        self.historyTable[self.pos.historyIndex(mv)] += depth * depth
        mvsKiller = self.killerTable[self.pos.distance]
        if mvsKiller[0] != mv:
            mvsKiller[1] = mvsKiller[0]
            mvsKiller[0] = mv

    def searchQuiesc(self, vlAlpha_, vlBeta):
        vlAlpha = vlAlpha_
        self.allNodes += 1

        vl = self.pos.mateValue()
        if vl >= vlBeta:
            return vl
        vlRep = self.pos.repStatus(1)
        if vlRep > 0:
            return self.pos.repValue(vlRep)
        if self.pos.distance == LIMIT_DEPTH:
            return self.pos.evaluate()
        vlBest = -MATE_VALUE
        mvs = []
        vls = []
        if self.pos.inCheck():
            mvs = self.pos.generateMoves(None)
            for i in range(len(mvs)):
                vls.append(self.historyTable[self.pos.historyIndex(mvs[i])])
            shellSort(mvs, vls)
        else:
            vl = self.pos.evaluate()
            if vl > vlBest:
                if vl >= vlBeta:
                    return vl
                vlBest = vl
                vlAlpha = max(vl, vlAlpha)
            mvs = self.pos.generateMoves(vls)
            shellSort(mvs, vls)
            for i in range(len(mvs)):
                if vls[i] < 10 or (vls[i] < 20 and HOME_HALF(DST(mvs[i]), self.pos.sdPlayer)):
                    mvs = mvs[:i]
                    break
        for i in range(len(mvs)):
            if not self.pos.makeMove(mvs[i]):
                continue
            vl = -self.searchQuiesc(-vlBeta, -vlAlpha)
            self.pos.undoMakeMove()
            if vl > vlBest:
                if vl >= vlBeta:
                    return vl
                vlBest = vl
                vlAlpha = max(vl, vlAlpha)
        return self.pos.mateValue() if vlBest == -MATE_VALUE else vlBest

    def searchFull(self, vlAlpha_, vlBeta, depth, noNull):
        vlAlpha = vlAlpha_
        if depth <= 0:
            return self.searchQuiesc(vlAlpha, vlBeta)
        self.allNodes += 1
        vl = self.pos.mateValue()
        if vl >= vlBeta:
            return vl

        vlRep = self.pos.repStatus(1)
        if vlRep > 0:
            return self.pos.repValue(vlRep)

        mvHash = [0]
        vl = self.probeHash(vlAlpha, vlBeta, depth, mvHash)
        if vl > -MATE_VALUE:
            return vl
        if self.pos.distance == LIMIT_DEPTH:
            return self.pos.evaluate()
        if not noNull and not self.pos.inCheck() and self.pos.nullOkay():
            self.pos.nullMove()
            vl = -self.searchFull(-vlBeta, 1 - vlBeta, depth - NULL_DEPTH - 1, True)
            self.pos.undoNullMove()
            if (vl >= vlBeta and (self.pos.nullSafe() or
                                  self.searchFull(vlAlpha, vlBeta, depth - NULL_DEPTH, True) >= vlBeta)):
                return vl
        hashFlag = HASH_ALPHA
        vlBest = -MATE_VALUE
        mvBest = 0
        sort = MoveSort(mvHash[0], self.pos, self.killerTable, self.historyTable)

        while True:
            mv = sort.next()
            if mv <= 0:
                break
            if not self.pos.makeMove(mv):
                continue
            newDepth = depth if (self.pos.inCheck() or sort.singleReply) else depth - 1
            if vlBest == -MATE_VALUE:
                vl = -self.searchFull(-vlBeta, -vlAlpha, newDepth, False)
            else:
                vl = -self.searchFull(-vlAlpha - 1, -vlAlpha, newDepth, False)
                if vlAlpha < vl < vlBeta:
                    vl = -self.searchFull(-vlBeta, -vlAlpha, newDepth, False)
            self.pos.undoMakeMove()
            if vl > vlBest:
                vlBest = vl
                if vl >= vlBeta:
                    hashFlag = HASH_BETA
                    mvBest = mv
                    break
                if vl > vlAlpha:
                    vlAlpha = vl
                    hashFlag = HASH_PV
                    mvBest = mv
        if vlBest == -MATE_VALUE:
            return self.pos.mateValue()
        self.recordHash(hashFlag, vlBest, depth, mvBest)
        if mvBest > 0:
            self.setBestMove(mvBest, depth)
        return vlBest

    def searchRoot(self,depth):
        vlBest = -MATE_VALUE
        sort = MoveSort(self.mvResult, self.pos, self.killerTable, self.historyTable)
        while True:
            mv = sort.next()
            if mv <= 0:
                break
            if not self.pos.makeMove(mv):
                continue
            newDepth = depth if self.pos.inCheck() else (depth - 1)
            if vlBest == -MATE_VALUE:
                vl = -self.searchFull(-MATE_VALUE, MATE_VALUE, newDepth, True)
            else:
                vl = -self.searchFull(-vlBest - 1, -vlBest, newDepth, False)
                if vl > vlBest:
                    vl = -self.searchFull(-MATE_VALUE, -vlBest, newDepth, True)
            self.pos.undoMakeMove()
            if vl > vlBest:
                vlBest = vl
                self.mvResult = mv
                if -WIN_VALUE < vlBest < WIN_VALUE:
                    vlBest += math.floor(random.random() * RANDOMNESS) - \
                        math.floor(random.random() * RANDOMNESS)
                    vlBest = ((vlBest - 1) if vlBest == self.pos.drawValue() else vlBest)
        self.setBestMove(self.mvResult, depth)
        return vlBest

    def searchUnique(self,vlBeta, depth):
        sort = MoveSort(self.mvResult, self.pos, self.killerTable, self.historyTable)
        sort.next()
        while True:
            mv = sort.next()
            if mv <= 0:
                break
            if not self.pos.makeMove(mv):
                continue
            vl = -self.searchFull(-vlBeta, 1 - vlBeta, depth if self.pos.inCheck() else (depth - 1), False)
            self.pos.undoMakeMove()
            if vl >= vlBeta:
                return False
        return True

    def searchMain(self,depth, millis):
        self.mvResult = self.pos.bookMove()
        if self.mvResult > 0:
            self.pos.makeMove(self.mvResult)
            if self.pos.repStatus(3) == 0:
                self.pos.undoMakeMove()
                return self.mvResult
            self.pos.undoMakeMove()
        self.hashTable = []
        for i in range(self.hashMask + 1):
            self.hashTable.append(HashTableObject(depth= 0, flag= 0, vl= 0, mv= 0, zobristLock= 0))
        self.killerTable =[]
        for i in range(LIMIT_DEPTH):
            self.killerTable.append([0, 0])
        self.historyTable =[]
        for i in range(4096):
            self.historyTable.append(0)
        self.mvResult = 0
        self.allNodes = 0
        self.pos.distance = 0
        t = time.time()
        for i in range(1,depth + 1):
            vl = self.searchRoot(i)
            self.allMillis = (time.time() - t) * 1000
            if self.allMillis > millis:
                break
            if vl > WIN_VALUE or vl < -WIN_VALUE:
                break
            if self.searchUnique(1 - WIN_VALUE, i):
                break
        return self.mvResult

