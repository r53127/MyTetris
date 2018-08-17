import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtGui import QPixmap,QPainter,QBitmap , QIcon , QCursor , QImageReader , QPainterPath , QPen , QImage
from PyQt5.QtCore import Qt , QRect ,QPoint
from LayerClass import LayerClass

class TetrisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        img = "Graphics/windows/windows.png"
        self.layers=[
            LayerClass(40, 32, 334, 279, img, 7),
            LayerClass(40, 343, 334, 279, img, 7),
            LayerClass(414, 32, 334, 590, img, 7),  # 游戏窗口，小方块为32*32像素，边框宽度为7，游戏窗口为16：9, 宽=32*10+14，高=18*32+14
            LayerClass(788, 32, 334, 124, img, 7),
            LayerClass(788, 188, 176, 148, img, 7),
            LayerClass(964, 188, 158, 148, img, 7),
            LayerClass(788, 368, 334, 124, img, 7),
            LayerClass(788, 524, 334, 98, img, 7),
         ]
        self.img_position={
            (820, 536):QImage("Graphics/game/logo.png"),
            (60, 52): QImage("Graphics/game/db.png"),
            (60,363):QImage("Graphics/game/world.png"),
            (820,64): QImage("Graphics/game/start.png"),
            (970, 64): QImage("Graphics/game/exit.png"),
            (1000, 208): QImage("Graphics/game/level.png"),
            (808, 378): QImage("Graphics/game/score.png"),
            (808, 418): QImage("Graphics/game/rmline.png")
        }



    def initUI(self):
        self.setWindowTitle('多多大战俄罗斯方块')
        self.setWindowIcon(QIcon('Graphics\windows\windows.png'))
        self.pix = QBitmap("Graphics/Backgroud/mask3.png")
        self.resize(self.pix.size())#蒙板的尺寸为1162*654
        self.setMask(self.pix)
        self.setWindowOpacity(1)  # 设置透明度
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
            # 当左键移动窗体修改偏移值
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
                layer.CreateLayer(painter)
            for img_pos in self.img_position:
                painter.drawImage(QPoint(img_pos[0],img_pos[1]), self.img_position[img_pos])

        except BaseException as e:
            print('错误是:',e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TetrisWindow()
    sys.exit(app.exec_())


