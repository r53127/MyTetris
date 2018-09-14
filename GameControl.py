'''
接受玩家控制键盘事件
控制画面
控制游戏逻辑
'''
import random
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication

from Const import CONST
from Db import Database, DataDisk
from GameDto import GameDto
from GameService import GameService
from Player import GamePlayer
from SavePointDialog import SavePointDialog
from TetrisWindow import TetrisWindow


class GameControl():
    def __init__(self):
        # 创建游戏数据源
        self.dto = GameDto()
        #鏈接數據庫
        self.db_data = Database()
        #讀取本地數據
        self.disk_data = DataDisk()
        #加載數據
        self.reloadData()
        # 创建游戏面板(连接游戏数据源、 安装游戏控制器）
        self.gameWindow = TetrisWindow(self.dto, self)
        # 创建游戏逻辑块（连接游戏数据源）
        self.gameService = GameService(self.dto)
        # 传送对象的方法：1、构造函数初始化 2、Set方法 3、传递参数
        # 初始化玩家輸入姓名窗口
        self.savePointDialog=SavePointDialog(self)

    # 加載玩家數據
    def reloadData(self):
        self.dto.dbRcorder = self.db_data.loadUserData('score', 5)
        self.dto.diskRecorder = self.disk_data.loadUserData()

    # 保存玩家數據
    def saveData(self, playername):
        try:
            if self.dto.nowPoint == 0:
                return
            player = GamePlayer(playername.strip(), self.dto.nowPoint)
            self.db_data.saveUserData(player)
            self.disk_data.saveUserData(player)
            self.reloadData()
        except BaseException as e:
            print('Error is :', e)

    def startGame(self):
        if not self.dto.isStarted:
            self.dto.isLosed = 0
            self.dto.isStarted = 1
            self.dto.nowRemoveLine = 0
            self.dto.nowPoint = 0
            self.dto.nowLevel = 0
            self.dto.speed = CONST.GameSpeed
            self.dto.gameMap = [[0] * self.dto.gameHeight for i in range(self.dto.gameWidth)]
            self.dto.gameAct.initRect(random.randint(1, 7))

    def keyUp(self):
        self.gameService.keyUp()
        self.gameWindow.update()

    def keyDown(self):
        if self.gameService.keyDown():
            QSound.play("music\move.wav")
        ##判断游戏是否结束
        if self.checkLosed():
            self.afterLosed()  # 输了以后的操作
        self.gameWindow.update()

    def afterLosed(self):
        self.dto.isStarted = 0
        self.dto.isLosed = 1
        QSound.play(r"music\lose.wav")
        self.savePointDialog.setPointLabel(str(self.dto.nowPoint))
        self.savePointDialog.show()

    def checkLosed(self):
        for point in self.dto.gameAct.actPoints:
            if self.dto.gameMap[point[0]][point[1]]:
                return True

    def keyLeft(self):
        self.gameService.keyLeft()
        self.gameWindow.update()

    def keyRight(self):
        self.gameService.keyRight()
        self.gameWindow.update()

    def keyFastdown(self):
        if not self.gameWindow.gameDto.isStarted or self.gameWindow.gameDto.isPaused:
            return
        # iscanFastfall=self.gameService.keyDown()
        # while iscanFastfall:
        #     iscanFastfall=self.gameService.keyDown()
        ##循环代码优化
        while (1):
            if not self.gameService.keyDown():
                QSound.play(r"music\remove01.wav")
                break
        self.gameWindow.update()

    def keyStart(self):
        if self.gameWindow.gameDto.isStarted or self.gameWindow.gameDto.isPaused:
            return
        self.startGame()
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
        # if not self.gameWindow.dto.isPaused:
        #     self.timer.stop()
        #     self.gameWindow.dto.isPaused = 1
        # else:
        #     self.timer.start()
        #     self.gameWindow.dto.isPaused = 0
        ##典型开关型代码优化
        if self.gameWindow.gameDto.isPaused:
            self.timer.start()
        else:
            self.timer.stop()
        self.gameWindow.gameDto.isPaused = not self.gameWindow.gameDto.isPaused

    def keyTest(self):
        self.gameWindow.gameDto.nowRemoveLine += 2
        self.gameService.updateSpeed(self.gameService.updateLevel(self.gameService.updatePoint(2)))
        self.gameWindow.update()

    def keySetup(self):
        ##TODO 设置按钮功能
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 播放背景音乐
    backmusic = QSound(r"music\backmusic01.wav")
    backmusic.setLoops(-1)
    backmusic.play()
    # 创建游戏控制器
    GameControl()
    sys.exit(app.exec_())
