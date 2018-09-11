'''
游戏界面图层
'''
import os
from abc import abstractmethod, ABCMeta

from PyQt5.QtCore import QRect, QPoint, Qt
from PyQt5.QtGui import QPixmap, QCursor, QFont
from PyQt5.QtWidgets import QPushButton

from Const import CONST

FRMAEIMG = CONST.FrameImg  # 边框图片
SIZE = CONST.CFG.cornersize  # pic cornor width : 7 pixel
PADDING = CONST.CFG.padding  # pic padding : 16 pixel
ACT = CONST.ActImg  # 方块图片
ACT_SIZE = CONST.Act_Size  # 方块边长32像素

NUMWIDTH = CONST.NumImge.width() / 10  # 数字宽度
NUMHEIGHT = CONST.NumImge.height()  # 数字高度


class LayerClass():
    def __init__(self, x, y, w, h,
                 parent=None):  # Top-left coordinate and size of the layer is （x,y)  and （width,height)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.parent = parent
        self.imgW = FRMAEIMG.width()
        self.imgH = FRMAEIMG.height()

    def setGameDto(self, gameDto):
        self.gameDto = gameDto

    def createlayer(self, painter):
        # 左上
        painter.drawImage(QRect(self.x, self.y, SIZE, SIZE), FRMAEIMG,
                          QRect(0, 0, SIZE, SIZE))
        # 中上
        painter.drawImage(QRect(self.x + SIZE, self.y, self.w - 2 * SIZE, SIZE),
                          FRMAEIMG,
                          QRect(SIZE, 0, self.imgW - 2 * SIZE, SIZE))
        # 右上
        painter.drawImage(QRect(self.x + self.w - SIZE, self.y, SIZE, SIZE), FRMAEIMG,
                          QRect(self.imgW - SIZE, 0, SIZE, SIZE))
        # 左中
        painter.drawImage(QRect(self.x, self.y + SIZE, SIZE, self.h - 2 * SIZE),
                          FRMAEIMG,
                          QRect(0, SIZE, SIZE, self.imgH - 2 * SIZE))
        # 中中
        painter.drawImage(
            QRect(self.x + SIZE, self.y + SIZE, self.w - 2 * SIZE, self.h - 2 * SIZE),
            FRMAEIMG,
            QRect(SIZE, SIZE, self.imgW - 2 * SIZE, self.imgH - 2 * SIZE))
        # 右中
        painter.drawImage(QRect(self.x + self.w - SIZE, self.y + SIZE, SIZE, self.h - 2 * SIZE),
                          FRMAEIMG,
                          QRect(self.imgW - SIZE, SIZE, SIZE, self.imgH - 2 * SIZE))
        # 左下
        painter.drawImage(QRect(self.x, self.y + self.h - SIZE, SIZE, SIZE), FRMAEIMG,
                          QRect(0, self.imgH - SIZE, SIZE, SIZE))
        # 中下
        painter.drawImage(QRect(self.x + SIZE, self.y + self.h - SIZE, self.w - 2 * SIZE, SIZE),
                          FRMAEIMG,
                          QRect(SIZE, self.imgH - SIZE, self.imgW - 2 * SIZE, SIZE))
        # 右下
        painter.drawImage(QRect(self.x + self.w - SIZE, self.y + self.h - SIZE, SIZE, SIZE),
                          FRMAEIMG,
                          QRect(self.imgW - SIZE, self.imgH - SIZE, SIZE, SIZE))

    # 画方块
    # mapX,mapY为地图格数
    # rectCode为单个方块在方块图片中的编号
    def drawRect(self, mapX, mapY, painter, rectCode):
        if self.gameDto.isLosed:
            rectCode = 8  # 使用8号方块作为失败方块
        painter.drawImage(
            QRect(self.x + mapX * ACT_SIZE + SIZE, self.y + mapY * ACT_SIZE + SIZE, ACT_SIZE,
                  ACT_SIZE), ACT,
            QRect(rectCode * 32, 0, ACT_SIZE, ACT_SIZE))

    # 打印图片数字
    # x,y 为框内坐标
    # num 为要打印的数字
    # numberSize为原字体比例
    def drawNumberAlignRight(self, num, x, y, painter, numberSize=1):
        finished = 0  # 已打印字符数
        for i in reversed(list(str(num))):  # 逆序打印
            finished = finished + 1
            painter.drawImage(
                QRect(self.x + x - finished * NUMWIDTH, self.y + y, NUMWIDTH * numberSize, NUMHEIGHT * numberSize),
                CONST.NumImge,
                QRect(int(i) * NUMWIDTH, 0, NUMWIDTH, NUMHEIGHT))

    # 画值槽进度条
    # x,y 为框内要调整的像素
    # num ,showString为要显示的数字长度和要显示的字符
    #percent=recorderPoint/nowPoint
    def drawProcess(self, painter, percent, x, y, **showplayer_or_showstring):
        levelupW = CONST.ProcessImg.width()
        levelupH = CONST.ProcessImg.height()
        painter.setBrush(Qt.black)
        painter.drawRect(self.x + x, self.y + y + 2, self.w - 2 * PADDING, levelupH + 4)
        painter.setBrush(Qt.white)
        painter.drawRect(self.x + x + 2, self.y + y + 4, self.w - 2 * PADDING - 4, levelupH)
        painter.setBrush(Qt.black)
        painter.drawRect(self.x + x + 4, self.y + y + 6, self.w - 2 * PADDING - 8, levelupH - 4)
        painter.drawImage(
            QRect(self.x + x + 4, self.y + y + 7, percent* (self.w - 2 * PADDING - 8) , levelupH - 5),
            CONST.ProcessImg,
            QRect(percent*levelupW-1, 0, 1, levelupH))
        painter.setPen(Qt.white)
        painter.setFont(QFont('Mine', 10, QFont.Bold))
        #使用命名关键字参数,因为要传递的参数不确定，如果没有玩家纪录则打印字符串，如有存在记录则打印玩家信息
        if 'showstring' in showplayer_or_showstring:
            painter.drawText(self.x + x + 6, self.y + y + levelupH - 4, showplayer_or_showstring['showstring'])
        if 'showplayer' in showplayer_or_showstring:
            painter.drawText(self.x + x + 6, self.y + y + levelupH - 4, showplayer_or_showstring['showplayer'].name)
            painter.drawText(self.x + x + 6+(self.w - 2 * PADDING - 8)/2, self.y + y + levelupH - 4, str(showplayer_or_showstring['showplayer'].point).rjust(14))


class GameLayer(LayerClass):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)

    def paint(self, painter):
        OVERWIDTH = CONST.OverImg.width()
        OVERHEIGHT = CONST.OverImg.height()
        self.createlayer(painter)
        # 绘制下落方块
        if self.gameDto.isStarted:
            for point in self.gameDto.gameAct.actPoints:
                self.drawRect(point[0], point[1], painter, self.gameDto.gameAct.rectCode)
            self.drawShadow(painter)

        # 绘制地图
        gameMap = self.gameDto.gameMap
        for mapX in range(len(gameMap)):
            for mapY in range(len(gameMap[mapX])):
                if gameMap[mapX][mapY]:#如果该坐标为1，则绘制一个方块
                    self.drawRect(mapX, mapY, painter, self.gameDto.nowLevel % 8)  # 使用余数号方块作为固定方块
        if self.gameDto.isLosed:
            painter.drawImage(
                QPoint(self.x + (self.w - OVERWIDTH) / 2 + PADDING, self.y + (self.h - OVERHEIGHT) / 2 + PADDING),
                CONST.OverImg)

    def drawShadow(self,painter):
        if self.gameDto.isShowShadow:
            shadowLeft=self.gameDto.gameAct.actPoints[0][0]
            shadowRight=self.gameDto.gameAct.actPoints[0][0]
            shadowHeight=CONST.GameHeight
            #根据下落方块的旋转情况获取阴影的最大左右边界
            for point in self.gameDto.gameAct.actPoints:
                if shadowLeft>point[0]:
                     shadowLeft=point[0]
                if shadowRight<point[0]:
                    shadowRight=point[0]
            painter.drawImage(
                QRect(self.x+shadowLeft*ACT_SIZE+SIZE, self.y+SIZE,(shadowRight-shadowLeft+1)*ACT_SIZE, (shadowHeight+1)*ACT_SIZE),
                CONST.ShadowImg,
                QRect(0, 0, 1, 1))


class DataLayer(LayerClass, metaclass=ABCMeta):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)

    @abstractmethod
    def paint(self, painter):
        pass

    ##绘制5个玩家纪录
    def drawData(self,painter,players_recorder):
        painter.drawImage(QPoint(self.x + PADDING, self.y + PADDING), CONST.DBImg)
        i = 0
        while i<5:
            #判断要绘制的纪录是否超界
            if i<len(players_recorder):
                player=players_recorder[i]
                percent = self.gameDto.nowPoint / player.point
                if percent >= 1:
                    percent = 1
                self.drawProcess(painter, percent, 15, CONST.DBImg.height() + 20 + 40 * i, showplayer=player)
            else:
                #纪录不存在
                self.drawProcess(painter, percent, 15, CONST.DBImg.height() + 20 + 40 * i, showstring='NO DATA')
            i=i+1


class DBLayer(DataLayer):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)

    def paint(self, painter):
        self.createlayer(painter)
        self.drawData(painter,self.gameDto.dbRcorder)


class WorldLayer(DataLayer):

    def paint(self, painter):
        self.createlayer(painter)
        self.drawData(painter,self.gameDto.diskRecorder)


class ButtonLayer(LayerClass):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)
        self.btn1 = QPushButton(self.parent)
        self.btn2 = QPushButton(self.parent)
        self.btn1.setObjectName('startbtn')
        self.btn2.setObjectName('setupbtn')
        self.btn1.setGeometry(self.x + PADDING + 20, self.y + PADDING + 20, QPixmap(CONST.StartImg).width(),
                              QPixmap(CONST.StartImg).height())
        self.btn2.setGeometry(self.x + PADDING + 60 + CONST.StartImg.width(), self.y + PADDING + 20,
                              QPixmap(CONST.StartImg).width(), QPixmap(CONST.StartImg).height())
        style = '''
                            #startbtn{
                                border-radius: 30px;
                                background-image: url('./Graphics/game/start.png');
                                }
                            #setupbtn{
                                border-radius: 30px;
                                background-image: url('./Graphics/game/setup.png');
                                }
                        '''
        self.btn1.setStyleSheet(style)
        self.btn2.setStyleSheet(style)
        self.btn1.setFocusPolicy(0)
        self.btn2.setFocusPolicy(0)
        self.btn1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn2.setCursor(QCursor(Qt.PointingHandCursor))

    def paint(self, painter):
        self.createlayer(painter)
        self.btn1.pressed.connect(self.parent.gameControl.keyStart)
        self.btn2.pressed.connect(self.parent.gameControl.keySetup)
        # if self.gameDto.isStarted:
        #     self.btn1.setDisabled(1)
        # else:
        #     self.btn1.setEnabled(1)


class NextLayer(LayerClass):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度`
        super().__init__(x, y, w, h, parent)

    def paint(self, painter):
        self.createlayer(painter)
        # 打印下一个方块
        if self.gameDto.isStarted and not self.gameDto.isLosed:
            nextPoints = []
            for point in CONST.rectTable[self.gameDto.next]:
                nextPoints.append([point[0], point[1]])
            for point in nextPoints:
                painter.drawImage(
                    QRect(self.x + point[0] * ACT_SIZE + SIZE + 30, self.y + point[1] * ACT_SIZE + SIZE + 30, ACT_SIZE,
                          ACT_SIZE), ACT,
                    QRect(self.gameDto.next * 32, 0, ACT_SIZE, ACT_SIZE))


class LevelLayer(LayerClass):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)

    def paint(self, painter):
        self.createlayer(painter)
        levelImgWidth = CONST.LevelImg.width()
        levelImgHeight = CONST.LevelImg.height()
        centerx = (self.w - levelImgWidth) / 2
        painter.drawImage(QPoint(self.x + centerx, self.y + PADDING), CONST.LevelImg)
        self.drawNumberAlignRight(self.gameDto.nowLevel, self.w * 3 / 4, (self.h - levelImgHeight) / 2, painter)


class PointLayer(LayerClass):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)

    def paint(self, painter):
        SCORE_IMG_HEIGHT = CONST.ScoreImg.height()
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + SIZE, self.y + SIZE), CONST.ScoreImg)
        painter.drawImage(QPoint(self.x + SIZE, self.y + SCORE_IMG_HEIGHT + SIZE), CONST.RmlineImg)
        self.drawNumberAlignRight(self.gameDto.nowPoint, self.w, 0, painter, 0.7)
        self.drawNumberAlignRight(self.gameDto.nowRemoveLine, self.w, SCORE_IMG_HEIGHT, painter, 0.7)
        self.drawProcess(painter, (self.gameDto.nowPoint%200)/200, PADDING, 2 * SCORE_IMG_HEIGHT + SIZE, showstring='下一级')


class AboutLayer(LayerClass):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)

    def paint(self, painter):
        self.createlayer(painter)
        painter.drawImage(QPoint(self.x + PADDING + 10, self.y + PADDING), CONST.LogoImg)


class BackLayer(LayerClass):
    def __init__(self, x, y, w, h, parent=None):
        # 初始化层的x/y坐标和长度/宽度
        super().__init__(x, y, w, h, parent)
        self.backgrd_files=[]
        self.initbackgrd()

    def initbackgrd(self):
        backgrd_path="Graphics\Backgroud"
        if not os.path.exists(backgrd_path) or not os.path.isdir(backgrd_path):
            return
        dirs=os.listdir(backgrd_path)
        for file in dirs:
            if os.path.isfile(os.path.join(backgrd_path,file)):
                self.backgrd_files.append(os.path.join(backgrd_path,file))

    def paint(self, painter):
        if self.backgrd_files:
            idx=self.gameDto.nowLevel%len(self.backgrd_files)
            painter.drawPixmap(self.x, self.y, self.w, self.h, QPixmap(self.backgrd_files[idx]))


