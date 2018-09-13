'''
游戏逻辑
'''
import random

from PyQt5.QtMultimedia import QSound

from Const import CONST


class GameService():
    def __init__(self, dto,gameWin):
        self.dto = dto
        self.gameWin=gameWin

    def startGame(self):
        if not self.dto.isStarted:
            self.dto.isLosed = 0
            self.dto.isStarted = 1
            self.dto.nowRemoveLine = 0
            self.dto.nowPoint = 0
            self.dto.nowLevel = 0
            self.dto.speed = CONST.GameSpeed
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
            return True  ##正常下移
        ##移不动刷新地图
        for act in self.dto.gameAct.actPoints:
            self.dto.gameMap[act[0]][act[1]] = 1
        ##消行
        removed_Lines = self.removeLines()
        ##更新分数
        added_Point = self.updatePoint(removed_Lines)
        ##更新等级
        added_Level = self.updateLevel(added_Point)
        ##更新速度
        self.updateSpeed(added_Level)
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
        self.gameWin.savePointDialog.setPointLabel(str(self.dto.nowPoint))
        self.gameWin.savePointDialog.show()

    def checkLosed(self):
        for point in self.dto.gameAct.actPoints:
            if self.dto.gameMap[point[0]][point[1]]:
                return True

    def removeLines(self):
        removed_Lines = 0
        for mapY in range(self.dto.gameHeight):  # 逐行扫描方块地图
            if self.iscanRemove(mapY):
                self.removeLine(mapY)
                QSound.play(r"music\remove02.wav")
                removed_Lines += 1
        self.dto.nowRemoveLine += removed_Lines
        return removed_Lines

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

    def updatePoint(self, removedLines):
        if removedLines:
            addedPoint = removedLines ** 2 * 10
            self.dto.nowPoint += addedPoint
            return addedPoint

    def updateLevel(self, added_Point):
        if added_Point:
            added_Level = int(self.dto.nowPoint / 200) - self.dto.nowLevel
            self.dto.nowLevel = int(self.dto.nowPoint / 200)
            return added_Level

    def updateSpeed(self, added_Level):
        if self.dto.speed <= 50:
            self.dto.speed = 50
            return
        if added_Level:
            self.dto.speed = self.dto.speed - added_Level * 50
