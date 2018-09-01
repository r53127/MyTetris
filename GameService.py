'''
游戏逻辑
'''
import random

from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QMessageBox, QWidget


class GameService():
    def __init__(self, dto):
        self.dto = dto

    def keyUp(self):
        if self.dto.gameAct.rotate(self.dto.gameMap, self.dto.gameAct.rectCode):
            QSound.play("music\move.wav")

    def keyLeft(self):
         self.dto.gameAct.move(-1, 0, self.dto.gameMap)

    def keyRight(self):
        self.dto.gameAct.move(1, 0, self.dto.gameMap)

    def keyDown(self):
        if (self.dto.isStart==0) or (self.dto.isLose==1):
            return False ##不能下移
        if self.dto.gameAct.move(0, 1, self.dto.gameMap):
            QSound.play("music\move.wav")
            return True  ##下移则返回False
        ##移不动刷新地图
        for act in self.dto.gameAct.actPoints:
            self.dto.gameMap[act[0]][act[1]] = 1
        ##消行加分
        self.plusPoint()
        ##算分
        self.plusExp()
        ##升级
        self.upgradeLevel()
        ##刷新一个新的方块
        self.dto.gameAct.initRect(self.dto.next)
        self.dto.next = random.randint(1, 7)
        for point in self.dto.gameAct.actPoints:
            if self.dto.gameMap[point[0]][point[1]]:
                self.dto.isStart=0
                self.dto.isLose=1
                QMessageBox.information(None, '失败！', '游戏已结束！')
        return False ##不能再下移

    def plusExp(self):
        pass

    def upgradeLevel(self):
        pass

    def plusPoint(self):
        for mapY in range(self.dto.gameHeight):  # 逐行扫描方块地图
            if self.iscanRemove(mapY):
                self.removeLine(mapY)
                QSound.play(r"music\remove02.wav")

    def iscanRemove(self, mapY):
        for mapX in range(self.dto.gameWidth):  # 行内逐个判断是否有方块
            if self.dto.gameMap[mapX][mapY] != 1:
                return False
        return True

    def removeLine(self, rowNumber):
        y = rowNumber  # 给定行号
        while y > 0:
            for x in range(self.dto.gameWidth):
                self.dto.gameMap[x][y] = self.dto.gameMap[x][y - 1]  # 把上一行的方块移动该行
            y = y - 1  # 行往上移
        else:
            for x in range(self.dto.gameWidth):
                self.dto.gameMap[x][0] = 0
