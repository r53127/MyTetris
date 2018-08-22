from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QImage
from Const import CONST


class LayerClass():
    def __init__(self, x, y, w, h):  # Top-left coordinate and size of the layer is （x,y)  and （width,height)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.imgW = QImage(CONST.FrameImg).width()
        self.imgH = QImage(CONST.FrameImg).height()

    def createlayer(self, painter):
        # 左上
        painter.drawImage(QRect(self.x, self.y, CONST.CORNERSIZE, CONST.CORNERSIZE), QImage(CONST.FrameImg),
                          QRect(0, 0, CONST.CORNERSIZE, CONST.CORNERSIZE))
        # 中上
        painter.drawImage(QRect(self.x + CONST.CORNERSIZE, self.y, self.w - 2 * CONST.CORNERSIZE, CONST.CORNERSIZE),
                          QImage(CONST.FrameImg),
                          QRect(CONST.CORNERSIZE, 0, self.imgW - 2 * CONST.CORNERSIZE, CONST.CORNERSIZE))
        # 右上
        painter.drawImage(QRect(self.x + self.w - CONST.CORNERSIZE, self.y, CONST.CORNERSIZE, CONST.CORNERSIZE), QImage(CONST.FrameImg),
                          QRect(self.imgW - CONST.CORNERSIZE, 0, CONST.CORNERSIZE, CONST.CORNERSIZE))
        # 左中
        painter.drawImage(QRect(self.x, self.y + CONST.CORNERSIZE, CONST.CORNERSIZE, self.h - 2 * CONST.CORNERSIZE),
                          QImage(CONST.FrameImg),
                          QRect(0, CONST.CORNERSIZE, CONST.CORNERSIZE, self.imgH - 2 * CONST.CORNERSIZE))
        # 中中
        painter.drawImage(
            QRect(self.x + CONST.CORNERSIZE, self.y + CONST.CORNERSIZE, self.w - 2 * CONST.CORNERSIZE, self.h - 2 * CONST.CORNERSIZE),
            QImage(CONST.FrameImg),
            QRect(CONST.CORNERSIZE, CONST.CORNERSIZE, self.imgW - 2 * CONST.CORNERSIZE, self.imgH - 2 * CONST.CORNERSIZE))
        # 右中
        painter.drawImage(QRect(self.x + self.w - CONST.CORNERSIZE, self.y + CONST.CORNERSIZE, CONST.CORNERSIZE, self.h - 2 * CONST.CORNERSIZE),
                          QImage(CONST.FrameImg),
                          QRect(self.imgW - CONST.CORNERSIZE, CONST.CORNERSIZE, CONST.CORNERSIZE, self.imgH - 2 * CONST.CORNERSIZE))
        # 左下
        painter.drawImage(QRect(self.x, self.y + self.h - CONST.CORNERSIZE, CONST.CORNERSIZE, CONST.CORNERSIZE), QImage(CONST.FrameImg),
                          QRect(0, self.imgH - CONST.CORNERSIZE, CONST.CORNERSIZE, CONST.CORNERSIZE))
        # 中下
        painter.drawImage(QRect(self.x + CONST.CORNERSIZE, self.y + self.h - CONST.CORNERSIZE, self.w - 2 * CONST.CORNERSIZE, CONST.CORNERSIZE),
                          QImage(CONST.FrameImg),
                          QRect(CONST.CORNERSIZE, self.imgH - CONST.CORNERSIZE, self.imgW - 2 * CONST.CORNERSIZE, CONST.CORNERSIZE))
        # 右下
        painter.drawImage(QRect(self.x + self.w - CONST.CORNERSIZE, self.y + self.h - CONST.CORNERSIZE, CONST.CORNERSIZE, CONST.CORNERSIZE),
                          QImage(CONST.FrameImg),
                          QRect(self.imgW - CONST.CORNERSIZE, self.imgH - CONST.CORNERSIZE, CONST.CORNERSIZE, CONST.CORNERSIZE))


class DBLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + CONST.PADDING, self.y + CONST.PADDING), QImage(CONST.DBImg))


class WorldLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + CONST.PADDING, self.y + CONST.PADDING), QImage(CONST.WorldImg))


class GameLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)



class ButtonLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + CONST.PADDING + 20, self.y + CONST.PADDING + 20), QImage(CONST.StartImg))


class NextLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)


class LevelLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + CONST.PADDING, self.y + CONST.PADDING), QImage(CONST.LevelImg))


class PointLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + CONST.PADDING, self.y + CONST.PADDING), QImage(CONST.ScoreImg))


class AboutLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + CONST.PADDING + 10, self.y + CONST.PADDING), QImage(CONST.LogoImg))

