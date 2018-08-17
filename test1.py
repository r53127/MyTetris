from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bézier curve')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        # path = QPainterPath()
        # path.moveTo(30, 30)
        # path.cubicTo(30, 30, 200, 350, 350, 30)
        path = QPainterPath();
        path.addRect(150, 150, 100, 100)
        path.moveTo(100, 100)
        path.cubicTo(300, 100, 200, 200, 600, 600)
        path.cubicTo(100, 300, 200, 200, 100, 100)
        qp.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())