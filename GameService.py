'''
游戏逻辑
'''
import random

from GameAct import GameAct


class GameService():
    def __init__(self, dto):
        self.dto = dto
        self.dto.gameAct = GameAct()

    def keyUp(self):
        self.dto.gameAct.rotate(self.dto.gameMap)

    def keyDown(self):
        if self.dto.gameAct.move(0, 1,self.dto.gameMap) :
            return ##成功下移则直接返回
        ##移不动刷新地图
        for act in self.dto.gameAct.actPoints:
            self.dto.gameMap[act[0]][act[1]] = 1
        ##消行加分
        self.plusPoint()
        ##算分
        ##升级
        ##刷新一个新的方块
        self.dto.gameAct.initRect(random.randint(1,7))

    def plusPoint(self):
        for mapY in range(18):
            if self.iscanRemove(mapY):
                self.removeLine(mapY)
    def iscanRemove(self, mapY):
        for mapX in range(10):
            if self.dto.gameMap[mapX][mapY]!=1:
                return False
        return True

    def removeLine(self,rowNumber):
        pass



    def keyLeft(self):
        self.dto.gameAct.move(-1, 0,self.dto.gameMap)

    def keyRight(self):
        self.dto.gameAct.move(1, 0,self.dto.gameMap)







