# Берем заготовку для квадрат-объектив и учимся рисовать разные фигуры по нажатию на кнопку "показать"
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
import random
from PyQt5 import uic

SCREEN_SIZE = [400, 450]
FIGURES = ['circle']
COLORS = ['yellow']


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('4.ui', self)
        self.pushButton.clicked.connect(self.draw)

        # рисование фигур
    def draw(self):
        self.figure = random.choice(FIGURES)
        print(self.figure)
        self.size = random.randint(10, 100)
        self.color = random.choice(COLORS)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(self.color))
            qp.setBrush(QColor(self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            if self.figure == 'square':
                qp.drawRect(self.x, self.y, self.size, self.size)
            elif self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            elif self.figure == 'triangle':
                self.drawTriangle(qp)
            qp.end()

    def drawTriangle(self, qp):
        a = self.x - self.size // 2, self.y + self.size // 2
        b = self.x + self.size // 2, self.y + self.size // 2
        c = self.x, self.y - self.size // 2
        points = [QPoint(a[0], a[1]), QPoint(b[0], b[1]), QPoint(c[0], c[1])]
        qp.drawPolygon(QPolygon(points))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec_())