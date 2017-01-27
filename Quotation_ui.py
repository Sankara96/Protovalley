from PySide import QtGui, QtCore

class Ui_Proto(object):
    def setupUi(self, ProtoWindow):
        ProtoWindow.setObjectName("ProtoValley")
        ProtoWindow.setEnabled(True)
        ProtoWindow.resize(450,300)

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
        fontB.setUnderline(True)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(10,10,200,21)
        self.label.setFont(fontB)
        self.label.setObjectName("Label")

        self.line1 = QtGui.QLineEdit(self.centralwidget)
        self.line1.setGeometry(15,45,250,21)
        self.line1.setObjectName("Line1")
        self.line1.setFont(font)
        self.line1.setReadOnly(True)

        self.upload = QtGui.QPushButton(self.centralwidget)
        self.upload.setGeometry(270,45,75,21)
        self.upload.setObjectName("Upload")
        self.upload.setFont(font)
        self.upload.setStyleSheet("background-color: red")

        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setGeometry(15,75,75,21)
        self.status.setObjectName("status")
        self.status.setFont(font)

        self.status_value = QtGui.QLabel(self.centralwidget)
        self.status_value.setGeometry(100, 75, 100, 21)
        self.status_value.setObjectName("status_value")
        self.status_value.setFont(font)

        self.groupbox1 = QtGui.QGroupBox("Calculations",self.centralwidget)
        self.groupbox1.setGeometry(15,100,300,180)
        self.groupbox1.setObjectName("Groupbox1")
        self.groupbox1.setFont(font)

        self.time_label = QtGui.QLabel(self.groupbox1)
        self.time_label.setGeometry(10,20,75,21)
        self.time_label.setObjectName("time_label")
        self.time_label.setFont(font)

        self.time = QtGui.QLabel(self.groupbox1)
        self.time.setGeometry(150,20,75,21)
        self.time.setObjectName("time")
        self.time.setFont(font)

        self.cost_label = QtGui.QLabel(self.groupbox1)
        self.cost_label.setGeometry(10,45,120,21)
        self.cost_label.setObjectName("cost_label")
        self.cost_label.setFont(font)

        self.cost = QtGui.QLineEdit(self.groupbox1)
        self.cost.setGeometry(150,45,75,21)
        self.cost.setObjectName("Cost")
        self.cost.setFont(font)

        self.total_label = QtGui.QLabel(self.groupbox1)
        self.total_label.setGeometry(10,70,150,21)
        self.total_label.setObjectName("total_label")
        self.total_label.setFont(font)

        self.total = QtGui.QLineEdit(self.groupbox1)
        self.total.setGeometry(150,70,75,21)
        self.total.setObjectName("total")
        self.total.setFont(font)


        self.file_name = QtGui.QLabel(self.groupbox1)
        self.file_name.setGeometry(10,100,75,21)
        self.file_name.setObjectName("file_name")
        self.file_name.setFont(font)

        self.file = QtGui.QLineEdit(self.groupbox1)
        self.file.setGeometry(150,100,75,21)
        self.file.setObjectName("file")
        self.file.setFont(font)

        self.invoice_label = QtGui.QLabel(self.groupbox1)
        self.invoice_label.setGeometry(10,130,100,21)
        self.invoice_label.setObjectName("invoice_label")
        self.invoice_label.setFont(font)

        self.invoice = QtGui.QLineEdit(self.groupbox1)
        self.invoice.setGeometry(150,130,75,21)
        self.invoice.setObjectName("invoice")
        self.invoice.setFont(font)

        self.excel_buttton = QtGui.QPushButton(self.groupbox1)
        self.excel_buttton.setGeometry(15,160,75,21)
        self.excel_buttton.setObjectName("excel_button")
        self.excel_buttton.setFont(font)




        self.retranslateUI(ProtoWindow)



    def retranslateUI(self,protowindow):
        protowindow.setWindowTitle(QtGui.QApplication.translate("ProtoWindow","Protovalley - Quotation Generation",None,QtGui.QApplication.UnicodeUTF8))
        self.upload.setText(QtGui.QApplication.translate("ProtoWindow","Upload",None,QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProtoWindow","Upload FDM G-Code:",None,QtGui.QApplication.UnicodeUTF8))
        self.status.setText(QtGui.QApplication.translate("ProtoWindow","File Status: ",None,QtGui.QApplication.UnicodeUTF8))
        self.status_value.setText(QtGui.QApplication.translate("ProtoWindow","No File found",None,QtGui.QApplication.UnicodeUTF8))
        self.time_label.setText(QtGui.QApplication.translate("ProtoWindow","Running time:",None,QtGui.QApplication.UnicodeUTF8))
        self.time.setText(QtGui.QApplication.translate("ProtoWindow","----",None,QtGui.QApplication.UnicodeUTF8))
        self.cost_label.setText(QtGui.QApplication.translate("ProtoWindow","Cost per Minute:",None,QtGui.QApplication.UnicodeUTF8))
        self.cost.setText(QtGui.QApplication.translate("ProtoWindow","5",None,QtGui.QApplication.UnicodeUTF8))
        self.total_label.setText(QtGui.QApplication.translate("ProtoWindow","Total Cost in Rs:",None,QtGui.QApplication.UnicodeUTF8))
        self.total.setText(QtGui.QApplication.translate("ProtoWindow","",None,QtGui.QApplication.UnicodeUTF8))
        self.file_name.setText(QtGui.QApplication.translate("ProtoWindow","Details:",None,QtGui.QApplication.UnicodeUTF8))
        self.invoice_label.setText(QtGui.QApplication.translate("ProtoWindow","Invoice Number:",None,QtGui.QApplication.UnicodeUTF8))
        self.excel_buttton.setText(QtGui.QApplication.translate("ProtoWindow","Excel",None,QtGui.QApplication.UnicodeUTF8))