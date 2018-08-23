import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QCursor, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from GameCfg import GameCfg
import LayerClass

class TetrisWindow(QMainWindow):
    #load game config
    CFG = GameCfg()
    def __init__(self):
        super().__init__()
        #make layer objects
        self.layers=[]
        for layer in TetrisWindow.CFG.layerscfg:
            creator=getattr(LayerClass,layer.classname)# python reflect mechanism
            self.layers.append(creator(layer.x,layer.y,layer.w,layer.h))
        self.initUI()


    def initUI(self):
        self.setWindowTitle('多多大战俄罗斯方块')
        self.setWindowIcon(QIcon('Graphics\windows\windows.png'))
        self.pix = QBitmap("Graphics/Backgroud/mask3.png")
        self.resize(self.pix.size())#Masking panel pic size：1162*654
        self.setMask(self.pix)
        self.setWindowOpacity(1)  # set transparency
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

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
            #draw backgroud
            painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap("Graphics/Backgroud/screen1.jpg"))
            #draw layers
            for layer in self.layers:
                layer.paint(painter)
        except BaseException as e:
            print('Error is :',e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TetrisWindow()
    sys.exit(app.exec_())


