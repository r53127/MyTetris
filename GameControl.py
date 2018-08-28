'''
接受玩家控制键盘事件
控制画面
控制游戏逻辑
'''
from PyQt5.QtWidgets import QMessageBox


class GameControl():
    def __init__(self,gameWindow,gameService):
        #游戏界面层
        self.gameWindow= gameWindow
        #游戏逻辑层
        self.gameService=gameService

    def gameTest(self):
        self.gameService.gameTest()
        self.gameWindow.update()

    def up(self):
        try:
            QMessageBox.information(self.gameWindow,'提示', '不要按我！')
        except BaseException as e:
            print('Error is :', e)

    def down(self):
        QMessageBox.information(self.gameWindow, '提示', '你再按！')

    def left(self):
        QMessageBox.information(self.gameWindow, '提示', '再按我弄死你！')

    def right(self):
        QMessageBox.information(self.gameWindow, '提示', '你还按！')
