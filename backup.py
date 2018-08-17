# x,y,w,h=32,32,500,800# 从（32，32）开始长256，宽256的窗体
# imgW=QImage(ImageFilename).width()
# imgH=QImage(ImageFilename).height()
# size=7
# #左上
# painter.drawImage(QRect(x,y,size,size),QImage(ImageFilename),QRect(0,0,size,size))
# #中上
# painter.drawImage(QRect(x+size,y,w-2*size,size),QImage(ImageFilename),QRect(size,0,imgW-2*size,size))
# #右上
# painter.drawImage(QRect(x+w-size, y, size, size), QImage(ImageFilename), QRect(imgW-size, 0, size, size))
# #左中
# painter.drawImage(QRect(x,y+size,size,h-2*size),QImage(ImageFilename),QRect(0,size,size,imgH-2*size))
# #中中
# painter.drawImage(QRect(x+size,y+size,w-2*size,h-2*size),QImage(ImageFilename),QRect(size,size,imgW-2*size,imgH-2*size))
# #右中
# painter.drawImage(QRect(x+w-size, y+size, size, h-2*size), QImage(ImageFilename), QRect(imgW-size, size, size, imgH-2*size))
# #左下
# painter.drawImage(QRect(x, y+h-size, size, size), QImage(ImageFilename), QRect(0, imgH-size, size, size))
# #中下
# painter.drawImage(QRect(x+size, y + h - size, w-2*size, size), QImage(ImageFilename),QRect(size, imgH - size, imgW-2*size, size))
# #右下
# painter.drawImage(QRect(x +w- size, y + h - size, size, size), QImage(ImageFilename),QRect(imgW-size, imgH - size, size, size))