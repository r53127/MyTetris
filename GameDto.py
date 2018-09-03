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
        self.nowRemoveLine=0
        self.isStarted=0##游戏开始标志 0表述没开始，1表示开始了
        self.isLosed=0##游戏失败标志 0表示没输，1表示输了
        self.isPaused=False ##游戏暂停标志 False表示没暂停，True表示暂停



