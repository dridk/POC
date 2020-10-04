from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class SnakeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.pos = QPoint()

    def paintEvent(self, event):

        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(10)
        painter.setPen(pen)
        painter.drawPoint(self.pos)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Left:
            self.pos += QPoint(10, 0)

        if event.key() == Qt.Key_Right:
            self.pos += QPoint(-10, 0)

        if event.key() == Qt.Key_Up:
            self.pos += QPoint(0, -10)

        if event.key() == Qt.Key_Down:
            self.pos += QPoint(0, 10)

        self.update()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    c = SnakeWidget()

    c.show()

    app.exec_()
