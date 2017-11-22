# coding=utf-8
import time

from PyQt4 import QtGui, QtCore

import date_api
import news_api
import weather_api
from layouts import mirror_nice
from news_api import newsFeed


class LoadingWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        super(LoadingWidget, self).__init__(parent)
        self.parent = parent
        self.setFixedSize(450, 1000)
        self.setStyleSheet("background-color:transparent")
        movie = QtGui.QMovie("loading.gif")
        self.setMovie(movie)
        movie.start()

        self.widthSize = self.parent.width() - self.width()
        self.setGeometry(self.widthSize / 2, (0), 0, 0)

    def resizeEvent(self, event):
        self.widthSize = self.parent.width() - self.width()
        self.setGeometry(self.widthSize / 2, (0), 0, 0)


class MainWidget(QtGui.QWidget, mirror_nice.Ui_Form):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setFixedSize(QtCore.QSize(700, 800))
        self.news = news_api.newsFeed()

        self.updateMirror()
        self.updateNews()

        self.setLayout(self.globalGrid)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateMirror)
        timer.start(2000)

    def updateNews(self):
        # TODO: break layout into two widget
        belfold = [self.news[u"belfold"]["title"], self.news[u"belfold"]["summary"]]
        kulfold = [self.news[u"kulfold"]["title"], self.news[u"kulfold"]["summary"]]
        tech = [self.news[u"tech"]["title"], self.news[u"tech"]["summary"]]
        self.newsBrowser.setText(belfold[0]+"\n"+belfold[1]+"\n\n"+kulfold[0]+"\n"+kulfold[1]+"\n\n"+tech[0]+"\n"+tech[1])


    def updateMirror(self):
        time = QtCore.QTime.currentTime()
        time = time.toString('hh:mm')
        time = time[:2] + ':' + time[3:]

        weather = weather_api.weather()
        date = date_api.date()

        self.dateBrowser.setText(date["day"] + "\n" + date["month"])
        self.timeLabel.setText(time)
        self.dayLabel.setText(date["weekday"])

        temperature = weather["temp"]
        iconName = weather["icon"]
        details = weather["status"]

        self.text = self.tempLabel.setText(str(temperature) + u"°")

        pixmap = QtGui.QPixmap("icons/%s" % (iconName))

        pixmap = pixmap.scaled(QtCore.QSize(150, 150), QtCore.Qt.KeepAspectRatio,
                               transformMode=QtCore.Qt.SmoothTransformation)
        self.imgLabel.setPixmap(pixmap)
        self.descBrowser.setText(details)


class NewsThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        feed = newsFeed()
        time.sleep(0.8)
        self.emit(QtCore.SIGNAL('done'), feed)


class MirrorMain(QtGui.QMainWindow):
    def __init__(self):
        super(MirrorMain, self).__init__()
        self.threadPool = []
        self.threadPool.append(NewsThread())
        self.connect(self.threadPool[len(self.threadPool) - 1], QtCore.SIGNAL("done"), self.done)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:black")
        self.showMaximized()
        self.loadingWidget = LoadingWidget(self)
        self.setCentralWidget(self.loadingWidget)

        self.threadPool[len(self.threadPool) - 1].start()

    def done(self, news):
        self.news = news
        self.mainWidget = MainWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.loadingWidget.deleteLater()


if __name__ == "__main__":
    app = QtGui.QApplication([])
    main = MirrorMain()
    app.exec_()
