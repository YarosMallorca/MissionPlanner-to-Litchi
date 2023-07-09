import sys

from PySide6.QtCore import Qt, QEvent, QPointF, QPoint
from PySide6.QtGui import QColor, QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsColorizeEffect, QWidget

from gui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowMaximizeButtonHint
            | Qt.WindowMinimizeButtonHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.prevGeo = self.geometry()
        self.installEventFilters()
        self.setup_buttons()
    def color_toggle(self, obj, active):
        color = QColor('#535352') if active else QColor('#efeff1')
        effect = QGraphicsColorizeEffect(obj)
        effect.setColor(color)
        obj.setGraphicsEffect(effect)

    def setup_buttons(self):
        color = QColor('#efeff1')
        for btn in self.ui.buttonGroup_header.buttons():
            self.color_toggle(btn, False)

    def installEventFilters(self):
        for w in self.findChildren(QWidget) + [self]:
            w.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj is self:
            return QMainWindow.eventFilter(self, obj, event)
        print(obj.objectName())
        # print(event)
        match obj.objectName():
            case 'layoutWidget':
                match event.type():
                    case QEvent.MouseButtonDblClick:
                        self.setWindowState(self.windowState() ^ Qt.WindowFullScreen)
                        return True
                    case QEvent.MouseButtonRelease:
                        if event.globalPosition().y() < 10 and self.moved:
                            self.prevGeo = self.geometry()
                            self.showMaximized()
                            return True
                    case QEvent.MouseButtonPress:
                        self.prevMousePos = event.scenePosition()
                        self.moved = False
                    case QEvent.MouseMove:
                        if self.windowState() == Qt.WindowFullScreen \
                                or self.windowState() == Qt.WindowMaximized:
                            self.showNormal()
                            self.prevMousePos = QPointF(self.prevGeo.width() / 2.0, 50)
                        gr = self.geometry()
                        screenPos = event.globalPosition()
                        pos = screenPos - self.prevMousePos
                        x = max(pos.x(), 0)
                        y = max(pos.y(), 0)
                        screen = QGuiApplication.screenAt(QPoint(x, y)).size()
                        x = min(x, screen.width() - gr.width())
                        y = min(y, screen.height() - gr.height())
                        self.move(x, y)
                        self.moved = True
            case 'pushButton_home':
                match event.type():
                    case QEvent.MouseButtonRelease:
                        self.color_toggle(obj, False)
                    case QEvent.MouseButtonPress:
                        self.color_toggle(obj, True)
            case 'pushButton_list':
                match event.type():
                    case QEvent.MouseButtonRelease:
                        self.color_toggle(obj, False)
                    case QEvent.MouseButtonPress:
                        self.color_toggle(obj, True)
            case 'pushButton_settings':
                match event.type():
                    case QEvent.MouseButtonRelease:
                        self.color_toggle(obj, False)
                    case QEvent.MouseButtonPress:
                        self.color_toggle(obj, True)
            case 'pushButton_minimize':
                match event.type():
                    case QEvent.MouseButtonRelease:
                        self.color_toggle(obj, False)
                        self.showMinimized()
                    case QEvent.MouseButtonPress:
                        self.color_toggle(obj, True)
            case 'pushButton_close':
                match event.type():
                    case QEvent.MouseButtonRelease:
                        self.color_toggle(obj, False)
                        sys.exit(0)
                    case QEvent.MouseButtonPress:
                        self.color_toggle(obj, True)

        return QMainWindow.eventFilter(self, obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
