from PyQt5.QtCore import QRect
from PyQt5.QtGui import QImage

class LayerClass():
    def __init__(self,x,y,w,h,ImageFilename,size):#x,y,w,h分别为图层的起始坐标（x,y)和大小（width,height),ImageFilename为准备切片的图片名称，size为图片切角的像素值
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.ImageFilename=ImageFilename
        self.imgW = QImage(ImageFilename).width()
        self.imgH = QImage(ImageFilename).height()
        self.size=size

    def CreateLayer(self,painter):#
        # 左上
        painter.drawImage(QRect(self.x, self.y, self.size, self.size), QImage(self.ImageFilename), QRect(0, 0, self.size, self.size))
        # 中上
        painter.drawImage(QRect(self.x + self.size, self.y, self.w - 2 * self.size, self.size), QImage(self.ImageFilename),
                          QRect(self.size, 0, self.imgW - 2 * self.size, self.size))
        # 右上
        painter.drawImage(QRect(self.x + self.w - self.size, self.y, self.size, self.size), QImage(self.ImageFilename), QRect(self.imgW - self.size, 0, self.size, self.size))
        # 左中
        painter.drawImage(QRect(self.x, self.y + self.size, self.size, self.h - 2 * self.size), QImage(self.ImageFilename),
                          QRect(0, self.size, self.size, self.imgH - 2 * self.size))
        # 中中
        painter.drawImage(QRect(self.x + self.size, self.y + self.size, self.w - 2 * self.size, self.h - 2 * self.size), QImage(self.ImageFilename),
                          QRect(self.size, self.size, self.imgW - 2 * self.size, self.imgH - 2 * self.size))
        # 右中
        painter.drawImage(QRect(self.x + self.w - self.size, self.y + self.size, self.size, self.h - 2 * self.size), QImage(self.ImageFilename),
                          QRect(self.imgW - self.size, self.size, self.size, self.imgH - 2 * self.size))
        # 左下
        painter.drawImage(QRect(self.x, self.y + self.h - self.size, self.size, self.size), QImage(self.ImageFilename), QRect(0, self.imgH - self.size, self.size, self.size))
        # 中下
        painter.drawImage(QRect(self.x + self.size, self.y + self.h - self.size, self.w - 2 * self.size, self.size), QImage(self.ImageFilename),
                          QRect(self.size, self.imgH - self.size, self.imgW - 2 * self.size, self.size))
        # 右下
        painter.drawImage(QRect(self.x + self.w - self.size, self.y + self.h - self.size, self.size, self.size), QImage(self.ImageFilename),
                          QRect(self.imgW - self.size, self.imgH - self.size, self.size, self.size))
