from PySide import QtGui,QtCore
from Quotation_ui import Ui_Proto
import sys
import openpyxl
from win32com import client
class ProtoApp(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Proto()
        self.ui.setupUi(self)
        self.ui.upload.clicked.connect(self.upload)
        self.ui.cost.textChanged.connect(self.calculate)
        self.ui.excel_buttton.clicked.connect(self.excel)



    def excel(self):

        self.sample = openpyxl.load_workbook("Sample.xlsx")
        self.invoice = self.sample.get_sheet_by_name("Invoice")
        self.invoice["A16"] = str(1)
        self.invoice["B16"] = self.ui.file.text()
        self.invoice["D16"] = self.ui.total.text()
        self.invoice["F16"] = self.ui.total.text()
        self.invoice["G39"] = self.ui.total.text()
        self.invoice["G4"] = self.ui.invoice.text()
        file = self.ui.invoice.text()
        self.sample.save("{0}.xlsx".format(file))

        xlApp = client.Dispatch("Excel.Application")
        books = xlApp.Workbooks.Open('C:\Users\ADMIN\PycharmProjects\ProtoValley\{0}.xlsx'.format(file))
        ws = books.Worksheets[0]
        ws.Visible = 1
        ws.ExportAsFixedFormat(0,"C:\Users\ADMIN\PycharmProjects\ProtoValley\{0}.pdf".format(file))



    def upload(self):

        self.ui.upload.setStyleSheet("background-color: red")
        self.ui.upload.setText("Upload")
        self.ui.status_value.setText("File Not Found")


        browse_path = "C:"
        file_path = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(),
                                                      'Select File', browse_path)
        self.file_name = file_path[0]
        if len(self.file_name)>1:
            self.ui.line1.setText(self.file_name)
            self.ui.upload.setStyleSheet("background-color: green")
            self.ui.status_value.setText("File Uploaded")
            self.ui.upload.setText("Uploaded")
            self.calculate()
        else:
            self.ui.time.setText("-----")
            self.ui.cost.setText("5")
            self.ui.total.setText("")
            self.ui.line1.setText("")

    def calculate(self):
        if len(self.file_name)>1:
            file = open(self.file_name,"r")
            for lines in file:
                if "TIME:" in lines:
                    lines = lines[6:]
                    self.ui.time.setText("{0}".format((int(lines)/60)+1))
                    self.ui.total.setText("{0}".format(int(self.ui.time.text())*int(self.ui.cost.text())))
                    break



    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(QtGui.QMessageBox(), 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.exit = True
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    quotation_app = QtGui.QApplication(sys.argv)
    quotation = ProtoApp()
    quotation.show()
    status = quotation_app.exec_()