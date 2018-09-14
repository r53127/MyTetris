from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QCursor, QIcon
from PyQt5.QtWidgets import QMainWindow

import LayerClass
from Const import CONST


class TetrisWindow(QMainWindow):
    def __init__(self, gameDto,gameControl):
        super().__init__()
        # 接收传入的游戏数据
        self.gameDto = gameDto
        self.gameControl = gameControl
        self.initLayer()
        self.initUI()

    def initLayer(self):
        self.layers = []
        for layercfg in CONST.CFG.layerscfg:  # load layers size ,make layers object
            creator = getattr(LayerClass, layercfg.classname)  # python reflect mechanism
            layer = creator(layercfg.x, layercfg.y, layercfg.w, layercfg.h, self)  # 生成layer
            layer.setGameDto(self.gameDto)  # 把游戏数据对象传递给layer
            self.layers.append(layer)  # create and init layers

    def initUI(self):
        self.setWindowTitle('多多大战俄罗斯方块')
        self.setWindowIcon(QIcon('Graphics\windows\windows.png'))
        # desktop=QApplication.desktop()
        # self.pix=desktop.availableGeometry()
        # self.setGeometry(self.pix)
        # self.pix = QBitmap("Graphics/Backgroud/mask3.png")
        # self.resize(self.pix.size())  # Masking panel pic size：1162*654
        # self.setMask(self.pix)
        self.resize(1162,654)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowOpacity(1)  # set transparency
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key_Escape:
                self.close()
            elif event.key() == Qt.Key_Up:
                self.gameControl.keyUp()
            elif event.key() == Qt.Key_Down:
                self.gameControl.keyDown()
            elif event.key() == Qt.Key_Left:
                self.gameControl.keyLeft()
            elif event.key() == Qt.Key_Right:
                self.gameControl.keyRight()
            elif event.key() == Qt.Key_Space:
                self.gameControl.keyFastdown()
            elif event.key() == Qt.Key_T:
                self.gameControl.keyTest()
            elif event.key() == Qt.Key_S:
                self.gameControl.keyStart()
            elif event.key() == Qt.Key_P:
                self.gameControl.keyPause()
        except BaseException as e:
            print('错误是:', e)

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
            for layer in self.layers:
                layer.paint(painter)  # 显示layer
        except BaseException as e:
            print('Error is :', e)



