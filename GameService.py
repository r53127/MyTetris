'''
游戏逻辑
'''
import random

from PyQt5.QtMultimedia import QSound


class GameService():
    def __init__(self, dto):
        self.dto = dto

    def startGame(self):
        if not self.dto.isStarted:
            self.dto.isLosed = 0
            self.dto.isStarted = 1
            self.dto.nowRemoveLine = 0
            self.dto.nowPoint = 0
            self.dto.nowLevel = 0
            self.dto.gameMap = [[0] * self.dto.gameHeight for i in range(self.dto.gameWidth)]
            self.dto.gameAct.initRect(random.randint(1, 7))

    def keyUp(self):
        if self.dto.isPaused or (not self.dto.isStarted) or self.dto.isLosed:  ##暂停或未开始或输了
            return
        self.dto.gameAct.rotate(self.dto.gameMap, self.dto.gameAct.rectCode)
        QSound.play("music\move.wav")

    def keyLeft(self):
        if self.dto.isPaused or (not self.dto.isStarted) or self.dto.isLosed:  ##暂停或未开始或输了
            return
        self.dto.gameAct.move(-1, 0, self.dto.gameMap)

    def keyRight(self):
        if self.dto.isPaused or (not self.dto.isStarted) or self.dto.isLosed:  ##暂停或未开始或输了
            return
        self.dto.gameAct.move(1, 0, self.dto.gameMap)

    def keyDown(self):
        if self.dto.isPaused or (not self.dto.isStarted) or self.dto.isLosed:  ##暂停或未开始或输了
            return False  ##不能下移
        if self.dto.gameAct.move(0, 1, self.dto.gameMap):
            QSound.play("music\move.wav")
            return True  ##正常下移
        ##移不动刷新地图
        for act in self.dto.gameAct.actPoints:
            self.dto.gameMap[act[0]][act[1]] = 1
        ##消行加分
        removedLines = self.plusPoint()
        if removedLines:
            ##算分
            self.dto.nowRemoveLine += removedLines
            self.dto.nowPoint += removedLines ** 2 * 10
            ##升级
            self.dto.nowLevel = int(self.dto.nowPoint / 200)
        ##刷新一个新的方块
        self.dto.gameAct.initRect(self.dto.next)
        self.dto.next = random.randint(1, 7)
        ##判断游戏是否结束
        if self.checkLosed():
            self.afterLosed()  # 输了以后的操作
            return False  ##不能再下移

    def afterLosed(self):
        self.dto.isStarted = 0
        self.dto.isLosed = 1
        QSound.play(r"music\lose.wav")

    def checkLosed(self):
        for point in self.dto.gameAct.actPoints:
            if self.dto.gameMap[point[0]][point[1]]:
                return True

    def plusPoint(self):
        removedLines = 0
        for mapY in range(self.dto.gameHeight):  # 逐行扫描方块地图
            if self.iscanRemove(mapY):
                self.removeLine(mapY)
                QSound.play(r"music\remove02.wav")
                removedLines += 1
        return removedLines

    def iscanRemove(self, mapY):
        for mapX in range(self.dto.gameWidth):  # 行内逐个判断是否有方块
            if self.dto.gameMap[mapX][mapY] != 1:
                return False
        return True

    def removeLine(self, rowNumber):  # 删除该行
        y = rowNumber  # 给定行号
        while y > 0:
            for x in range(self.dto.gameWidth):
                self.dto.gameMap[x][y] = self.dto.gameMap[x][y - 1]  # 把上一行的方块移动到该行
            y = y - 1  # 行往上移
        else:
            for x in range(self.dto.gameWidth):
                self.dto.gameMap[x][0] = 0
