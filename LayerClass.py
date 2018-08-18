from PyQt5.QtCore import QRect
from PyQt5.QtGui import QImage


class CONST():
    SIZE = 7  # 边框切边宽度为7个像素
    PADDING = 16  # 图片显示内边距为16个像素
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
    def __init__(self, x, y, w, h):  # x,y,w,h分别为图层的起始坐标（x,y)和大小（width,height),FrameImg为准备切片的图片名称
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.imgW = QImage(CONST.FrameImg).width()
        self.imgH = QImage(CONST.FrameImg).height()

    def CreateLayer(self, painter):
        # 左上
        painter.drawImage(QRect(self.x, self.y, CONST.SIZE, CONST.SIZE), QImage(CONST.FrameImg),
                          QRect(0, 0, CONST.SIZE, CONST.SIZE))
        # 中上
        painter.drawImage(QRect(self.x + CONST.SIZE, self.y, self.w - 2 * CONST.SIZE, CONST.SIZE), QImage(CONST.FrameImg),
                          QRect(CONST.SIZE, 0, self.imgW - 2 * CONST.SIZE, CONST.SIZE))
        # 右上
        painter.drawImage(QRect(self.x + self.w - CONST.SIZE, self.y, CONST.SIZE, CONST.SIZE), QImage(CONST.FrameImg),
                          QRect(self.imgW - CONST.SIZE, 0, CONST.SIZE, CONST.SIZE))
        # 左中
        painter.drawImage(QRect(self.x, self.y + CONST.SIZE, CONST.SIZE, self.h - 2 * CONST.SIZE), QImage(CONST.FrameImg),
                          QRect(0, CONST.SIZE, CONST.SIZE, self.imgH - 2 * CONST.SIZE))
        # 中中
        painter.drawImage(QRect(self.x + CONST.SIZE, self.y + CONST.SIZE, self.w - 2 * CONST.SIZE, self.h - 2 * CONST.SIZE),
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
                          QImage(CONST.FrameImg), QRect(CONST.SIZE, self.imgH - CONST.SIZE, self.imgW - 2 * CONST.SIZE, CONST.SIZE))
        # 右下
        painter.drawImage(QRect(self.x + self.w - CONST.SIZE, self.y + self.h - CONST.SIZE, CONST.SIZE, CONST.SIZE), QImage(
            CONST.FrameImg),
                          QRect(self.imgW - CONST.SIZE, self.imgH - CONST.SIZE, CONST.SIZE, CONST.SIZE))

class DBLayer(LayerClass):
    def __init__(self):
        pass







