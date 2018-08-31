'''
游戏数据
'''
import random

from GameRect import GameRect


class GameDto():
    def __init__(self):
        self.gameHeight=18
        self.gameWidth=10
        self.dbRcorder=[]
        self.diskRecorder=[]
        self.gameMap=[[0] * self.gameHeight for i in range(self.gameWidth)] #方块地图为10*18
        self.gameAct=GameRect() #下落方块初始化
        self.next=random.randint(1,7)
        self.nowLevel=0
        self.nowPoint=0
        self.newRemoveLine=0



