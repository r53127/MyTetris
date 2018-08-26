'''
接受玩家控制键盘事件
控制画面
控制游戏逻辑
'''

class GameControl():
    def __init__(self,gameWindow,gameService):
        self.panelgame= gameWindow
        self.gameService=gameService
