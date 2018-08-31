'''
游戏逻辑
'''
import random


class GameService():
    def __init__(self, dto):
        self.dto = dto

    def keyUp(self):
        self.dto.gameAct.rotate(self.dto.gameMap,self.dto.gameAct.rectCode)

    def keyDown(self):
        if self.dto.gameAct.move(0, 1, self.dto.gameMap):
            return  ##成功下移则直接返回
        ##移不动刷新地图
        for act in self.dto.gameAct.actPoints:
            self.dto.gameMap[act[0]][act[1]] = 1
        ##消行加分
        self.plusPoint()
        ##算分
        ##升级
        ##刷新一个新的方块
        self.dto.gameAct.initRect(self.dto.next)
        self.dto.next=random.randint(1, 7)

    def keyspaceDown(self):
        if self.dto.gameAct.move(0, 1, self.dto.gameMap):
            return  ##成功下移则直接返回
        ##移不动刷新地图
        for act in self.dto.gameAct.actPoints:
            self.dto.gameMap[act[0]][act[1]] = 1
        ##消行加分
        self.plusPoint()
        ##算分
        ##升级
        ##刷新一个新的方块
        self.dto.gameAct.initRect(3)

    def plusPoint(self):
        for mapY in range(self.dto.gameHeight):#逐行扫描方块地图
            if self.iscanRemove(mapY):
                self.removeLine(mapY)

    def iscanRemove(self, mapY):
        for mapX in range(self.dto.gameWidth): #行内逐个判断是否有方块
            if self.dto.gameMap[mapX][mapY] != 1:
                return False
        return True

    def removeLine(self, rowNumber):
        y = rowNumber  #给定行号
        while y > 0:
            for x in range(self.dto.gameWidth):
                self.dto.gameMap[x][y] = self.dto.gameMap[x][y - 1]#把上一行的方块移动该行
            y = y - 1  #行往上移
        else:
            for x in range(self.dto.gameWidth):
                self.dto.gameMap[x][0] = 0

    def keyLeft(self):
        self.dto.gameAct.move(-1, 0, self.dto.gameMap)

    def keyRight(self):
        self.dto.gameAct.move(1, 0, self.dto.gameMap)
