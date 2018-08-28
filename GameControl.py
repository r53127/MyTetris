'''
接受玩家控制键盘事件
控制画面
控制游戏逻辑
'''

class GameControl():
    def __init__(self,gameWindow,gameService):
        #游戏界面层
        self.gameWindow= gameWindow
        #游戏逻辑层
        self.gameService=gameService

    def up(self):
        print('pressed e')

    def down(self):
        print('pressed d')

    def left(self):
        print('pressed s')

    def right(self):
        print('pressed f')
