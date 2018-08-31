import random

from PyQt5.QtMultimedia import QSound

MIN_X = 0
MAX_X = 9  # 宽最多10格
MIN_Y = 0
MAX_Y = 17  # 长最多18格

'''
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7
'''
class GameAct():
    #方块坐标表
    rectTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((1, 0), (0, 0), (1, 1), (2, 1)),
        ((1, 1), (0, 1), (1, 0), (2, 0)),
        ((1, 0), (0, 0), (2, 0), (3, 0)),
        ((1, 0), (0, 0), (2, 0), (1, 1)),
        ((1, 0), (0, 0), (0, 1), (1, 1)),
        ((0, 1), (0, 0), (0, 2), (1, 2)),
        ((1, 1), (1, 0), (1, 2), (0, 2))
    )

    def __init__(self):
        self.initRect(random.randint(1,7))

    def initRect(self,rectCode):
        self.rectCode=rectCode  ##界面层需要方块编号选择不同颜色
        self.actPoints = []
        for point in GameAct.rectTable[rectCode]:
            self.actPoints.append([point[0]+3,point[1]])#中间出方块

    def isOverZone(self, newX, newY,gameMap):
        if newX < MIN_X or newX > MAX_X or newY < MIN_Y or newY > MAX_Y or gameMap[newX][newY]:
            return False

    def move(self, moveX, moveY,gameMap):  # moveX,moveY分别是x,y轴移动偏移量
        for i in range(len(self.actPoints)):
            newX = self.actPoints[i][0] + moveX
            newY = self.actPoints[i][1] + moveY
            if self.isOverZone(newX, newY,gameMap) == False:
                return False
        QSound.play("music\move.wav")
        for i in range(len(self.actPoints)):
            self.actPoints[i][0] += moveX
            self.actPoints[i][1] += moveY
        return True

    def rotate(self,gameMap):
        for i in range(1, len(self.actPoints)):
            newX = self.actPoints[0][0] + self.actPoints[0][1] - self.actPoints[i][1]
            newY = self.actPoints[0][1] - self.actPoints[0][0] + self.actPoints[i][0]
            if self.isOverZone(newX, newY,gameMap) == False:
                return
        QSound.play("music\move.wav")
        for i in range(1, len(self.actPoints)):
            newX = self.actPoints[0][0] + self.actPoints[0][1] - self.actPoints[i][1]
            newY = self.actPoints[0][1] - self.actPoints[0][0] + self.actPoints[i][0]
            self.actPoints[i][0] = newX
            self.actPoints[i][1] = newY
