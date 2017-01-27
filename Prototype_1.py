from PySide import QtGui, QtCore

class Ui_Proto(object):
    def setupUi(self, ProtoWindow):
        ProtoWindow.setObjectName("ProtoValley")
        ProtoWindow.setEnabled(True)
        ProtoWindow.resize(525,300)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Proto.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProtoWindow.setWindowIcon(icon)

        self.centralwidget = QtGui.QWidget(ProtoWindow)
        self.centralwidget.setObjectName("centralwidget")
        ProtoWindow.setCentralWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        fontB = QtGui.QFont()
        fontB.setPointSize(11)

        self.new_order =  QtGui.QCheckBox(self.centralwidget)
        self.new_order.setGeometry(20,25,100,21)
        self.new_order.setObjectName("neworder")
        self.new_order.setFont(font)
        self.new_order.setText("New Order")

        self.order_group = QtGui.QGroupBox("New Order Entry",self.centralwidget)
        self.order_group.setGeometry(20,50,200,150)
        self.order_group.setObjectName("newgroupbox")
        self.order_group.setFont(fontB)

        self.reference_number = QtGui.QLabel(self.order_group)
        self.reference_number.setGeometry(10,25,120,21)
        self.reference_number.setObjectName("reference_number")
        self.reference_number.setFont(font)

        self.reference_number_value = QtGui.QLabel(self.order_group)
        self.reference_number_value.setGeometry(125,25,120,21)
        self.reference_number_value.setObjectName("Reference_value")
        self.reference_number_value.setFont(font)

        self.design = QtGui.QCheckBox(self.order_group)
        self.design.setGeometry(50,55,120,21)
        self.design.setObjectName("designcheck")
        self.design.setFont(font)

        self.dlp = QtGui.QCheckBox(self.order_group)
        self.dlp.setGeometry(50,75,150,21)
        self.dlp.setObjectName("dlpcheck")
        self.dlp.setFont(font)

        self.fdm = QtGui.QCheckBox(self.order_group)
        self.fdm.setGeometry(50,100,150,21)
        self.fdm.setObjectName("fdmcheck")
        self.fdm.setFont(font)

        self.casting = QtGui.QCheckBox(self.order_group)
        self.casting.setGeometry(50,125,150,21)
        self.casting.setObjectName("casting")
        self.casting.setFont(font)
        self.statusbox_label = QtGui.QLabel(self.centralwidget)
        self.statusbox_label.setGeometry(250,20,200,21)
        self.statusbox_label.setObjectName("statuslabel")
        self.statusbox_label.setFont(fontB)

        self.statusbox = QtGui.QTreeWidget(self.centralwidget)
        self.statusbox.setGeometry(QtCore.QRect(250, 50, 250, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbox.sizePolicy().hasHeightForWidth())
        self.statusbox.setSizePolicy(sizePolicy)
        self.statusbox.setProperty("cursor", QtCore.Qt.ArrowCursor)
        self.statusbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusbox.setAlternatingRowColors(True)
        self.statusbox.setUniformRowHeights(True)
        self.statusbox.setAllColumnsShowFocus(False)
        self.statusbox.setColumnCount(1)
        self.statusbox.setObjectName("statusbox")

        self.done_btn = QtGui.QPushButton(self.centralwidget)
        self.done_btn.setGeometry(25,220,75,21)
        self.done_btn.setObjectName("donebutton")
        self.done_btn.setFont(font)

        self.add_btn = QtGui.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(340,220,75,21)
        self.add_btn.setObjectName("addbutton")
        self.add_btn.setFont(font)








        self.retranslate_Ui(ProtoWindow)


    def retranslate_Ui(self,ProtoWindow):
        ProtoWindow.setWindowTitle(QtGui.QApplication.translate("ProtoWindow","ProtoValley - Order Tracking",None,QtGui.QApplication.UnicodeUTF8))
        self.reference_number.setText(QtGui.QApplication.translate("ProtoWindow","Reference number:", None,QtGui.QApplication.UnicodeUTF8))
        self.reference_number_value.setText(QtGui.QApplication.translate("ProtoWindow","xxxxxx",None,QtGui.QApplication.UnicodeUTF8))
        self.design.setText(QtGui.QApplication.translate("ProtoWindow","Design",None,QtGui.QApplication.UnicodeUTF8))
        self.dlp.setText(QtGui.QApplication.translate("ProtoWindow","DLP 3D Print",None,QtGui.QApplication.UnicodeUTF8))
        self.fdm.setText(QtGui.QApplication.translate("ProtoWindow","FDM 3D Print", None,QtGui.QApplication.UnicodeUTF8))
        self.casting.setText(QtGui.QApplication.translate("ProtoWindow","Casting",None,QtGui.QApplication.UnicodeUTF8))
        self.statusbox.headerItem().setText(0, QtGui.QApplication.translate("ProtoWindow", "File Location", None,QtGui.QApplication.UnicodeUTF8))
        self.statusbox_label.setText(QtGui.QApplication.translate("ProtoWindow","Files related to the Order:",None,QtGui.QApplication.UnicodeUTF8))
        self.done_btn.setText(QtGui.QApplication.translate("ProtoWindow","Done",None,QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("ProtoWindow","ADD",None,QtGui.QApplication.UnicodeUTF8))
