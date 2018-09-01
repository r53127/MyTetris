'''
接受玩家控制键盘事件
控制画面
控制游戏逻辑
'''
import random

from PyQt5.QtCore import QTimer


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

    def keyFastdown(self):
        canFallFlag=self.gameService.keyDown()
        while canFallFlag:
            canFallFlag=self.gameService.keyDown()

    def keyStart(self):
        if self.gameWindow.gameDto.isStart==0:
            self.gameWindow.gameDto.isStart=1
            self.gameWindow.gameDto.gameAct.initRect(random.randint(1,7))
            self.timer = QTimer()
            self.timer.setInterval(500)
            self.timer.timeout.connect(self.keyDown)
            self.timer.start()

    def keyPause(self):
        if self.gameWindow.gameDto.isStart:
            self.timer.timeout.disconnect(self.keyDown)
            self.gameWindow.gameDto.isStart=0
        else:
            self.timer.timeout.connect(self.keyDown)
            self.gameWindow.gameDto.isStart = 1

    def keyTest(self):
        pass

