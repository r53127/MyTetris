'''
游戏界面图层
'''
import random

from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QImage, QPixmap

from Const import CONST

FRMAEIMG = CONST.FrameImg  # 边框图片
SIZE = CONST.CFG.cornersize  # pic cornor width : 7 pixel
PADDING = CONST.CFG.padding  # pic padding : 16 pixel
ACT = CONST.ActImg  # 方块图片
ACT_SIZE = CONST.Act_Size  # 方块边长32像素

NUMWIDTH=QImage(CONST.NumImge).width()/10#数字宽度
NUMHEIGHT=QImage(CONST.NumImge).height()#数字高度


class LayerClass():
    def __init__(self, x, y, w, h):  # Top-left coordinate and size of the layer is （x,y)  and （width,height)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.imgW = QImage(FRMAEIMG).width()
        self.imgH = QImage(FRMAEIMG).height()

    def setGameDto(self, gameDto):
        self.gameDto = gameDto

    def createlayer(self, painter):
        # 左上
        painter.drawImage(QRect(self.x, self.y, SIZE, SIZE), QImage(FRMAEIMG),
                          QRect(0, 0, SIZE, SIZE))
        # 中上
        painter.drawImage(QRect(self.x + SIZE, self.y, self.w - 2 * SIZE, SIZE),
                          QImage(FRMAEIMG),
                          QRect(SIZE, 0, self.imgW - 2 * SIZE, SIZE))
        # 右上
        painter.drawImage(QRect(self.x + self.w - SIZE, self.y, SIZE, SIZE), QImage(FRMAEIMG),
                          QRect(self.imgW - SIZE, 0, SIZE, SIZE))
        # 左中
        painter.drawImage(QRect(self.x, self.y + SIZE, SIZE, self.h - 2 * SIZE),
                          QImage(FRMAEIMG),
                          QRect(0, SIZE, SIZE, self.imgH - 2 * SIZE))
        # 中中
        painter.drawImage(
            QRect(self.x + SIZE, self.y + SIZE, self.w - 2 * SIZE, self.h - 2 * SIZE),
            QImage(FRMAEIMG),
            QRect(SIZE, SIZE, self.imgW - 2 * SIZE, self.imgH - 2 * SIZE))
        # 右中
        painter.drawImage(QRect(self.x + self.w - SIZE, self.y + SIZE, SIZE, self.h - 2 * SIZE),
                          QImage(FRMAEIMG),
                          QRect(self.imgW - SIZE, SIZE, SIZE, self.imgH - 2 * SIZE))
        # 左下
        painter.drawImage(QRect(self.x, self.y + self.h - SIZE, SIZE, SIZE), QImage(FRMAEIMG),
                          QRect(0, self.imgH - SIZE, SIZE, SIZE))
        # 中下
        painter.drawImage(QRect(self.x + SIZE, self.y + self.h - SIZE, self.w - 2 * SIZE, SIZE),
                          QImage(FRMAEIMG),
                          QRect(SIZE, self.imgH - SIZE, self.imgW - 2 * SIZE, SIZE))
        # 右下
        painter.drawImage(QRect(self.x + self.w - SIZE, self.y + self.h - SIZE, SIZE, SIZE),
                          QImage(FRMAEIMG),
                          QRect(self.imgW - SIZE, self.imgH - SIZE, SIZE, SIZE))

    # 画方块
    #mapX,mapY为地图格数
    #rectCode为单个方块在方块图片中的编号
    def drawRect(self, mapX, mapY, painter, rectCode):
        painter.drawImage(
            QRect(self.x + mapX * ACT_SIZE + SIZE, self.y + mapY * ACT_SIZE + SIZE, ACT_SIZE,
                  ACT_SIZE), QImage(ACT),
            QRect(rectCode * 32, 0, ACT_SIZE, ACT_SIZE))

        # 打印图片数字
        # x,y 为框内坐标
        # num 为要打印的数字
        #numberSize为原字体比例
    def drawNumberAlignRight(self, num, x, y, painter,numberSize=1):
        finished = 0  # 已打印字符数
        for i in reversed(list(str(num))):#逆序打印
            finished = finished + 1
            painter.drawImage(QRect(self.x + x - finished * NUMWIDTH, self.y + y, NUMWIDTH*numberSize,NUMHEIGHT*numberSize),
                              QImage(CONST.NumImge),
                              QRect(int(i) * NUMWIDTH, 0, NUMWIDTH, NUMHEIGHT))

class GameLayer(LayerClass):
    def __init__(self, x, y, w, h):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h)

    def paint(self, painter):
        OVERWIDTH = QImage(CONST.OverImg).width()
        OVERHEIGHT = QImage(CONST.OverImg).height()
        self.createlayer(painter)
        # 打印下落方块
        if self.gameDto.isStarted==1 and self.gameDto.isLosed==0:
            for point in self.gameDto.gameAct.actPoints:
                self.drawRect(point[0], point[1], painter, self.gameDto.gameAct.rectCode)
        elif self.gameDto.isLosed==1:
            for point in self.gameDto.gameAct.actPoints:
                self.drawRect(point[0], point[1], painter, 8)# 使用8号方块作为失败方块
        # 打印地图
        gameMap = self.gameDto.gameMap
        for mapX in range(len(gameMap)):
            for mapY in range(len(gameMap[mapX])):
                if gameMap[mapX][mapY]:
                    if self.gameDto.isLosed==0:
                        self.drawRect(mapX, mapY, painter, 1)  # 使用1号方块作为固定方块
                    elif self.gameDto.isLosed==1:
                        self.drawRect(mapX, mapY, painter, 8)  # 使用8号方块作为失败方块
                        painter.drawImage(QPoint(self.x + (self.w-OVERWIDTH)/2+PADDING, self.y+(self.h-OVERHEIGHT)/2 + PADDING), QImage(CONST.OverImg))


class DBLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + PADDING, self.y + PADDING), QImage(CONST.DBImg))


class WorldLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + PADDING, self.y + PADDING), QImage(CONST.WorldImg))


class ButtonLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + PADDING + 20, self.y + PADDING + 20), QImage(CONST.StartImg))
        painter.drawImage(QPoint(self.x + PADDING + 60+QImage(CONST.StartImg).width(), self.y + PADDING + 20), QImage(CONST.SetupImg))


class NextLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        # 打印下一个方块
        if self.gameDto.isStarted==1 and self.gameDto.isLosed==0:
            nextPoints = []
            for point in CONST.rectTable[self.gameDto.next]:
                nextPoints.append([point[0], point[1]])
            for point in nextPoints:
                painter.drawImage(
                    QRect(self.x + point[0] * ACT_SIZE + SIZE + 30, self.y + point[1] * ACT_SIZE + SIZE + 30, ACT_SIZE,
                          ACT_SIZE), QImage(ACT),
                    QRect(self.gameDto.next * 32, 0, ACT_SIZE, ACT_SIZE))


class LevelLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        levelImgWidth = QImage(CONST.LevelImg).width()
        levelImgHeight = QImage(CONST.LevelImg).height()
        centerx=(self.w-levelImgWidth)/2
        painter.drawImage(QPoint(self.x + centerx, self.y + PADDING), QImage(CONST.LevelImg))
        self.drawNumberAlignRight(self.gameDto.nowLevel,self.w*3/4,(self.h-levelImgHeight)/2,painter)



class PointLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        scoreImgHeight = QImage(CONST.ScoreImg).height()
        painter.drawImage(QPoint(self.x+SIZE , self.y+SIZE), QImage(CONST.ScoreImg))
        painter.drawImage(QPoint(self.x+SIZE, self.y+scoreImgHeight+SIZE), QImage(CONST.RmlineImg))
        self.drawNumberAlignRight(self.gameDto.nowPoint,self.w,0,painter,0.7)
        self.drawNumberAlignRight(self.gameDto.nowRemoveLine, self.w, scoreImgHeight, painter, 0.7)


class AboutLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + PADDING + 10, self.y + PADDING), QImage(CONST.LogoImg))

class BackLayer(LayerClass):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.BackImg="Graphics/Backgroud/00"+str(random.randint(1,9))+".jpg"

    def paint(self, painter):
        painter.drawPixmap(self.x, self.y, self.w, self.h, QPixmap(self.BackImg))
