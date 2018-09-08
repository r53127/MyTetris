'''
接受玩家控制键盘事件
控制画面
控制游戏逻辑
'''

from PyQt5.QtCore import QTimer


class GameControl():
    def __init__(self, gameWindow, gameService):
        # 游戏界面层
        self.gameWindow = gameWindow
        # 游戏逻辑层
        self.gameService = gameService

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
        if self.gameWindow.gameDto.isPaused:
            return
        # iscanFastfall=self.gameService.keyDown()
        # while iscanFastfall:
        #     iscanFastfall=self.gameService.keyDown()
        ##循环代码优化
        while (1):
            if not self.gameService.keyDown():
                break
        self.gameWindow.update()

    def keyStart(self):
        if self.gameWindow.gameDto.isStarted or self.gameWindow.gameDto.isPaused:
            return
        self.gameService.startGame()
        self.timer = QTimer()
        self.timer.setInterval(self.gameWindow.gameDto.speed)
        self.timer.timeout.connect(self.keyDown)
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start()
        self.gameWindow.update()

    def updateTimer(self):
        self.timer.setInterval(self.gameWindow.gameDto.speed)
        if self.gameWindow.gameDto.isLosed:
            self.timer.timeout.disconnect(self.keyDown)
            self.timer.stop()

    def keyPause(self):
        if not self.gameWindow.gameDto.isStarted:
            return
        # if not self.gameWindow.gameDto.isPaused:
        #     self.timer.stop()
        #     self.gameWindow.gameDto.isPaused = 1
        # else:
        #     self.timer.start()
        #     self.gameWindow.gameDto.isPaused = 0
        ##典型开关型代码优化
        if self.gameWindow.gameDto.isPaused:
            self.timer.start()
        else:
            self.timer.stop()
        self.gameWindow.gameDto.isPaused = not self.gameWindow.gameDto.isPaused

    def keyTest(self):
        self.gameWindow.gameDto.nowRemoveLine += 1
        self.gameService.updateSpeed(self.gameService.updateLevel(self.gameService.updatePoint(1)))
        self.gameWindow.update()

    def keySetup(self):
        pass
