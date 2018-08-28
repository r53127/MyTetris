import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QCursor, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from GameDto import GameDto
import LayerClass
from Const import CONST
from GameControl import GameControl
from GameService import GameService


class TetrisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initLayer()
        self.initUI()
        self.initComponent()

    def initLayer(self):
        self.layers = []
        for layer in CONST.CFG.layerscfg:  # load layers size ,make layers object
            creator = getattr(LayerClass, layer.classname)  # python reflect mechanism
            self.layers.append(creator(layer.x, layer.y, layer.w, layer.h))#create and init layers

    def initUI(self):
        self.setWindowTitle('多多大战俄罗斯方块')
        self.setWindowIcon(QIcon('Graphics\windows\windows.png'))
        self.pix = QBitmap("Graphics/Backgroud/mask3.png")
        self.resize(self.pix.size())  # Masking panel pic size：1162*654
        self.setMask(self.pix)
        self.setWindowOpacity(1)  # set transparency
        self.show()

    def initComponent(self):
        pass

    def setGameControl(self,gameControl):
        self.gameControl=gameControl

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_E:
            self.gameControl.up()
        elif event.key() == Qt.Key_D:
            self.gameControl.down()
        elif event.key() == Qt.Key_S:
            self.gameControl.left()
        elif event.key() == Qt.Key_F:
            self.gameControl.right()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            # when left button moved, modify window offset value
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def paintEvent(self, QPaintEvent):
        try:
            painter = QPainter(self)
            painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap("Graphics/Backgroud/screen1.jpg"))
            for layer in self.layers:
                layer.paint(painter)
        except BaseException as e:
            print('Error is :', e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建游戏数据源
    gameDto=GameDto()
    #创建游戏面板
    gameWin = TetrisWindow()
    #创建游戏逻辑块（连接游戏数据源）
    gameServ=GameService(gameDto)
    #创建游戏控制器（链接游戏面板和游戏逻辑块）
    gameCtrl=GameControl(gameWin,gameServ)
    #安装游戏控制器
    gameWin.setGameControl(gameCtrl)
    sys.exit(app.exec_())
