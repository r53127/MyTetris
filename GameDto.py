'''
游戏数据
'''

class GameDto():
    def __init__(self):
        self.dbRcorder=[]
        self.diskRecorder=[]
        self.gameMap=[[0]*18 for i in range(10)] #方块地图为10*18
        self.gameAct=0  #下落方块
        self.next=0
        self.nowLevel=0
        self.nowPoint=0
        self.newRemoveLine=0



