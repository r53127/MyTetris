from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QImage


class CONST():
    SIZE = 7  # pic cornor width : 7 pixel
    PADDING = 16  # pic padding : 16 pixel
    FrameImg = "Graphics/windows/windows.png"
    LogoImg = "Graphics/game/logo.png"
    DBImg = "Graphics/game/db.png"
    WorldImg = "Graphics/game/world.png"
    StartImg = "Graphics/game/start.png"
    ExitImg = "Graphics/game/exit.png"
    LevelImg = "Graphics/game/level.png"
    ScoreImg = "Graphics/game/score.png"
    RmlineImg = "Graphics/game/rmline.png"


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
        painter.drawImage(QRect(self.x, self.y, CONST.SIZE, CONST.SIZE), QImage(CONST.FrameImg),
                          QRect(0, 0, CONST.SIZE, CONST.SIZE))
        # 中上
        painter.drawImage(QRect(self.x + CONST.SIZE, self.y, self.w - 2 * CONST.SIZE, CONST.SIZE),
                          QImage(CONST.FrameImg),
                          QRect(CONST.SIZE, 0, self.imgW - 2 * CONST.SIZE, CONST.SIZE))
        # 右上
        painter.drawImage(QRect(self.x + self.w - CONST.SIZE, self.y, CONST.SIZE, CONST.SIZE), QImage(CONST.FrameImg),
                          QRect(self.imgW - CONST.SIZE, 0, CONST.SIZE, CONST.SIZE))
        # 左中
        painter.drawImage(QRect(self.x, self.y + CONST.SIZE, CONST.SIZE, self.h - 2 * CONST.SIZE),
                          QImage(CONST.FrameImg),
                          QRect(0, CONST.SIZE, CONST.SIZE, self.imgH - 2 * CONST.SIZE))
        # 中中
        painter.drawImage(
            QRect(self.x + CONST.SIZE, self.y + CONST.SIZE, self.w - 2 * CONST.SIZE, self.h - 2 * CONST.SIZE),
            QImage(CONST.FrameImg),
            QRect(CONST.SIZE, CONST.SIZE, self.imgW - 2 * CONST.SIZE, self.imgH - 2 * CONST.SIZE))
        # 右中
        painter.drawImage(QRect(self.x + self.w - CONST.SIZE, self.y + CONST.SIZE, CONST.SIZE, self.h - 2 * CONST.SIZE),
                          QImage(CONST.FrameImg),
                          QRect(self.imgW - CONST.SIZE, CONST.SIZE, CONST.SIZE, self.imgH - 2 * CONST.SIZE))
        # 左下
        painter.drawImage(QRect(self.x, self.y + self.h - CONST.SIZE, CONST.SIZE, CONST.SIZE), QImage(CONST.FrameImg),
                          QRect(0, self.imgH - CONST.SIZE, CONST.SIZE, CONST.SIZE))
        # 中下
        painter.drawImage(QRect(self.x + CONST.SIZE, self.y + self.h - CONST.SIZE, self.w - 2 * CONST.SIZE, CONST.SIZE),
                          QImage(CONST.FrameImg),
                          QRect(CONST.SIZE, self.imgH - CONST.SIZE, self.imgW - 2 * CONST.SIZE, CONST.SIZE))
        # 右下
        painter.drawImage(QRect(self.x + self.w - CONST.SIZE, self.y + self.h - CONST.SIZE, CONST.SIZE, CONST.SIZE),
                          QImage(CONST.FrameImg),
                          QRect(self.imgW - CONST.SIZE, self.imgH - CONST.SIZE, CONST.SIZE, CONST.SIZE))


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

