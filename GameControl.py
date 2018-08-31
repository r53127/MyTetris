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

    def keyUp(self):
        self.gameService.keyUp()
        self.gameWindow.update()

    def keyDown(self):
        self.gameService.keyDown()
        self.gameWindow.update()

    def keyLeft(self):
        self.gameService.keyLeft()
        self.gameWindow.update()

    def keyRight(self):
        self.gameService.keyRight()
        self.gameWindow.update()

    def keySteal(self):
        self.gameService.keyspaceDown()
        self.gameWindow.update()
