class GameDto():
    def __init__(self):
        self.dbRcorder=[]
        self.diskRecorder=[]
        self.gameMap=[[0]*10 for i in range(18)]
        self.gameAct=[]
        self.next=0
        self.nowLevel=0
        self.nowPoint=0
        self.newRemoveLine=0



