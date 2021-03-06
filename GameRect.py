import random

from Const import CONST

MIN_X = 0
MAX_X = CONST.GameWidth# 宽最多10格
MIN_Y = 0
MAX_Y = CONST.GameHeight  # 长最多18格

class GameRect():

    def __init__(self):
        pass

    def initRect(self,rectCode):
        self.rectCode=rectCode  ##界面层需要方块编号选择不同颜色
        self.actPoints = []
        xOffset=random.randint(0,6)#随机位置出方块
        for point in CONST.rectTable[rectCode]:#初始化坐标
            self.actPoints.append([point[0]+xOffset,point[1]])

    def isOverZone(self, newX, newY,gameMap):
        if newX < MIN_X or newX > MAX_X or newY < MIN_Y or newY > MAX_Y or gameMap[newX][newY]:
            return True ##超出范围

    def move(self, moveX, moveY,gameMap):  # moveX,moveY分别是x,y轴移动偏移量
        for i in range(len(self.actPoints)):
            newX = self.actPoints[i][0] + moveX
            newY = self.actPoints[i][1] + moveY
            if self.isOverZone(newX, newY,gameMap):
                return False #不能移动
        for i in range(len(self.actPoints)):
            self.actPoints[i][0] += moveX
            self.actPoints[i][1] += moveY
        return True #可以移动

    def rotate(self,gameMap,rectCode):
        if rectCode==5:
            return False  ##旋转失败
        for i in range(1, len(self.actPoints)):
            newX = self.actPoints[0][0] + self.actPoints[0][1] - self.actPoints[i][1]
            newY = self.actPoints[0][1] - self.actPoints[0][0] + self.actPoints[i][0]
            if self.isOverZone(newX, newY,gameMap):
                return False ##旋转失败
        for i in range(1, len(self.actPoints)):
            newX = self.actPoints[0][0] + self.actPoints[0][1] - self.actPoints[i][1]
            newY = self.actPoints[0][1] - self.actPoints[0][0] + self.actPoints[i][0]
            self.actPoints[i][0] = newX
            self.actPoints[i][1] = newY
        return True##旋转成功

