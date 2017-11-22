import sys
import time

from PyQt4 import QtCore, QtGui

from news_api import newsFeed


class MyApp(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 280, 600)
        self.setWindowTitle('threads')

        self.layout = QtGui.QVBoxLayout(self)

        self.testButton = QtGui.QPushButton("test")
        self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)
        self.listwidget = QtGui.QListWidget(self)

        self.layout.addWidget(self.testButton)
        self.layout.addWidget(self.listwidget)
        self.threadPool = []

    def add(self, text):
        """ Add item to list widget """
        self.listwidget.addItem(text.decode("utf-8"))
        self.listwidget.sortItems()

    def done(self):
        self.status_txt.deleteLater()

    def test(self):
        self.listwidget.clear()
        self.threadPool.append(NewsThread())
        self.connect(self.threadPool[len(self.threadPool) - 1], QtCore.SIGNAL("update"), self.add)
        self.connect(self.threadPool[len(self.threadPool) - 1], QtCore.SIGNAL("done"), self.done)

        self.status_txt = QtGui.QLabel("Loading...")
        movie = QtGui.QMovie("loading_boobs.gif")
        self.status_txt.setMovie(movie)
        movie.start()
        self.layout.addWidget(self.status_txt)

        self.threadPool[len(self.threadPool) - 1].start()


class NewsThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        feed = newsFeed()
        feed = feed["belfold"]
        for i in feed:
            time.sleep(0.3)  # artificial time delay
            self.emit(QtCore.SIGNAL('update'), unicode(i[u"summary"]).encode("utf-8"))
        self.emit(QtCore.SIGNAL('done'))


# run
app = QtGui.QApplication(sys.argv)
test = MyApp()
test.show()
app.exec_()
