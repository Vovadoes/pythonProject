import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QFont, QColor
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QApplication

from random import randint

SCREEN_SIZE = [400, 400]
SIDE_LENGTH = 200
SIDES_COUNT = 5


class DrawStar(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()
        self.btn.clicked.connect(self.paint)

    def initUI(self):
        self.setGeometry(150, 150, *SCREEN_SIZE)
        self.setWindowTitle('Рисуем звезду')
        self.btn = QPushButton(self)
        self.btn.move(10, 10)
        self.btn.setText('Кнопка')


    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_squares(qp)
            qp.end()

    def draw_squares(self, qp):
        pen = QPen(Qt.yellow, 2)
        qp.setPen(pen)
        for i in range(5):
            r = randint(10, 100)
            x = randint(r, SCREEN_SIZE[0] - r)
            y = randint(r, SCREEN_SIZE[1] - r)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
