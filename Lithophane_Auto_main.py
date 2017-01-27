from PySide import QtCore,QtGui
import sys
from Lithopane_Auto import Ui_Auto
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
from time import sleep


class Autoapp(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Auto()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.upload)
        self.ui.start.clicked.connect(self.start)
        self.ui.Automate.clicked.connect(self.automate)

    def automate(self):
        """self.driver = webdriver.Firefox()
        self.driver.get("file:///E:/Lithophane_Automation/Lithophane/MakerBot%20Customizer.htm")
        choose = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/input[2]')
        choose.click()"""
        os.startfile('E:\Lithophane_Automation\Lithophane\MakerBot Customizer.htm')
        sleep(3)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.press('enter')
        pyautogui.press('enter')
        temp = ''
        temp1 = ""
        line = 1
        for letters in self.file_name[::-1]:
            if letters == '\\' or letters == "/" and line == 1:
                if line == 1:
                    line = 2
            elif line == 1:
                temp = ''.join((temp, letters))
            elif line == 2:
                temp1 = ''.join((temp1, letters))
        sleep(1)
        pyautogui.typewrite('{0}'.format(temp[::-1]))
        pyautogui.press('tab')
        pyautogui.press('tab')

        pyautogui.press('tab')

        pyautogui.press('tab')
        pyautogui.press('enter')

        pyautogui.typewrite("{0}".format(temp1[::-1]))
        sleep(3)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('enter')
        print " Done"
        sleep(0.5)
        #os.startfile("E:\Lithophane_Automation\Lithophane\image-surface.dat")
        #self.value = self.driver.find_element_by_id('foo_dat')
        #value = self.value.get_attribute('value')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
        sleep(0.5)
        os.startfile(r'E:\Lithophane_Automation\Lithophane\image-surface.dat')
        sleep(3)
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.press('v')
        pyautogui.press('s')
        pyautogui.keyUp('ctrl')


        #with open(r'E:\Lithophane_Automation\Lithophane\image-surface.dat','w') as file:
         #   file.write(value)
        sleep(2)
        os.startfile("E:\Lithophane_Automation\Lithophane\litho.scad")
        sleep(3)
        pyautogui.press('f5')
        sleep(0.5)
        pyautogui.press('f6')
        sleep(70)
        pyautogui.keyDown('alt')
        pyautogui.press('f')
        pyautogui.keyUp('alt')
        pyautogui.press('x')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(3)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('left')
        sleep(0.5)
        pyautogui.press('enter')





    def start(self):

        os.startfile(self.file_name)


    def upload(self):
        browse_path = ""
        file_path = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(),
                                                      'Select File', browse_path)
        self.file_name = file_path[0]
        print self.file_name
        self.ui.picture.setText(self.file_name)

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
    Automation_app = QtGui.QApplication(sys.argv)
    Automation = Autoapp()
    Automation.show()
    status = Automation_app.exec_()