from PySide import QtGui, QtCore


class Ui_Auto(object):

    def setupUi(self, AutoWindow):
        AutoWindow.setObjectName("Automation")
        AutoWindow.setEnabled(True)
        AutoWindow.resize(350,200)

        self.centralwidget = QtGui.QWidget(AutoWindow)
        self.centralwidget.setObjectName("centralwidget")
        AutoWindow.setCentralWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        fontB = QtGui.QFont()
        fontB.setPointSize(11)

        self.picture = QtGui.QLineEdit(self.centralwidget)
        self.picture.setGeometry(25,25,200,25)
        self.picture.setObjectName('picturelocation')
        self.picture.setFont(font)

        self.browse = QtGui.QPushButton(self.centralwidget)
        self.browse.setGeometry(230,25,75,25)
        self.browse.setObjectName('browselocation')
        self.picture.setFont(font)
        self.browse.setText("Browse")

        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(100,100,75,25)
        self.start.setObjectName('start')
        self.start.setFont(font)
        self.start.setText("Crop")

        self.Automate = QtGui.QPushButton(self.centralwidget)
        self.Automate.setGeometry(200,100,75,25)
        self.Automate.setObjectName("Automate")
        self.Automate.setFont(font)
        self.Automate.setText("Automate")



        AutoWindow.setWindowTitle(QtGui.QApplication.translate("AutoWindow","Lithophane Automation - ProtoValley",None,QtGui.QApplication.UnicodeUTF8))