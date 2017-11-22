# coding=utf-8
import datetime
import pyowm
from PyQt4 import QtGui, QtCore

import mirror_layout as mirror

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


class MainWidget(QtGui.QWidget, mirror.Ui_Form):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.setLayout(self.globalGrid)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateMirror)
        timer.start(10000)

        self.setFixedSize(QtCore.QSize(400, 345))

        self.updateMirror()

    def updateMirror(self):
        time = QtCore.QTime.currentTime()
        time = time.toString('hh:mm')
        time = time[:2] + ':' + time[3:]
        date = datetime.datetime.now()

        print date.weekday()
        self.timeLabel.setText(time)
        self.dayLabel.setText(days[date.weekday()])
        # self.dateLabel.setText(months[date.month - 1] + " " + str(date.day))

        owm = pyowm.OWM('00d400860e6a288e5682427bfd178b29')  # You MUST provide a valid API key

        day = owm.daily_forecast("Budapest,hu")
        self.forecast = day.get_forecast()
        forecast = self.forecast.get(0)

        iconName = forecast.get_weather_icon_name()
        temperature = forecast.get_temperature("celsius")
        temperature = int(temperature["day"])
        details = forecast.get_detailed_status()
        self.text = self.tempLabel.setText(str(temperature) + u"°C")
        print iconName
        if iconName == "01d" or iconName == "01n":
            pixmap = QtGui.QPixmap("icons/sunny")
        elif iconName == "02d" or iconName == "02n":
            pixmap = QtGui.QPixmap("icons/few_clouds")
        elif iconName == "03d" or iconName == "0n":
            pixmap = QtGui.QPixmap("icons/scattered_clouds")
        elif iconName == "04d" or iconName == "04n":
            pixmap = QtGui.QPixmap("icons/broken_clouds")
        elif iconName == "09d" or iconName == "09n":
            pixmap = QtGui.QPixmap("icons/shower_rain")
        elif iconName == "010d" or iconName == "10n":
            pixmap = QtGui.QPixmap("icons/rain")
        elif iconName == "11d" or iconName == "11n":
            pixmap = QtGui.QPixmap("icons/thunderstorm")
        elif iconName == "13d" or iconName == "13n":
            pixmap = QtGui.QPixmap("icons/snow")
        else:
            pixmap = QtGui.QPixmap("icons/mist")

        pixmap = pixmap.scaled(QtCore.QSize(100, 150), QtCore.Qt.KeepAspectRatio,
                               transformMode=QtCore.Qt.SmoothTransformation)
        self.imgLabel.setPixmap(pixmap)
        self.descBrowser.setText(details)


class MirrorMain(QtGui.QMainWindow):
    def __init__(self):
        super(MirrorMain, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:darkgrey")
        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)


if __name__ == "__main__":
    app = QtGui.QApplication([])
    main = MirrorMain()
    main.showMaximized()
    app.exec_()
