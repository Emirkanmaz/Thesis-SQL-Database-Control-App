import PyQt5
import pypyodbc
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
import sys
from ThesisAppWindow import Ui_MainWindow

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-OGS2E6J;'
    'Database=SE 307 Project - Emirkan Kanmaz Öykü Alim;'
    'Trusted_Connection=True;'
)

# #*************************************************************GUI APP*****************************************

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.displayData()
        self.displayUniData()
        self.displayInstData()
        self.displayLangData()
        self.displayAuthorData()
        self.displaySuperData()
        # self.ui.pushButton_Exit.clicked.connect(self.exitButtonFuction)
        self.ui.pushButton_ResetData.clicked.connect(self.resetButtonFunction)
        self.ui.pushButton_EnterData.clicked.connect(self.addTable)
        self.ui.pushButton_RefreshTable.clicked.connect(self.displayData)
        self.ui.pushButton_UpdateData.clicked.connect(self.updateButton)
        self.ui.pushButton_DeleteData.clicked.connect(self.deleteButton)
        self.ui.pushButton_SearchData.clicked.connect(self.searchButton)

        self.ui.pushButton_UniversityAdd.clicked.connect(self.addUniTable)
        self.ui.pushButton_UniversityUpdate.clicked.connect(self.updateUniButton)
        self.ui.pushButton_UniversityDelete.clicked.connect(self.deleteUniButton)
        self.ui.pushButton_UniversitySearch.clicked.connect(self.searchUniButton)
        self.ui.pushButton_UniversityReset.clicked.connect(self.resetUniButtonFunction)
        self.ui.pushButton_UniversityRefreshTable.clicked.connect(self.displayUniData)

        self.ui.pushButton_InstituteAdd.clicked.connect(self.addInstTable)
        self.ui.pushButton_InstituteUpdate.clicked.connect(self.updateInstButton)
        self.ui.pushButton_InstituteDelete.clicked.connect(self.deleteInstButton)
        self.ui.pushButton_InstituteSearch.clicked.connect(self.searchInstButton)
        self.ui.pushButton_InstituteReset.clicked.connect(self.resetInstButtonFunction)
        self.ui.pushButton_InstituteRefreshTable.clicked.connect(self.displayInstData)

        # self.ui.pushButton_LanguageAdd.clicked.connect(self.addLangTable)
        # self.ui.pushButton_LanguageUpdate.clicked.connect(self.updateLangButton)
        # self.ui.pushButton_LanguageDelete.clicked.connect(self.deleteLangButton)
        # self.ui.pushButton_LanguageSearch.clicked.connect(self.searchLangButton)
        # self.ui.pushButton_LanguageReset.clicked.connect(self.resetLangButtonFunction)
        # self.ui.pushButton_LanguageRefreshTable.clicked.connect(self.displayLangData)

        self.ui.pushButton_AuthorAdd.clicked.connect(self.addAuthorTable)
        self.ui.pushButton_AuthorUpdate.clicked.connect(self.updateAuthorButton)
        self.ui.pushButton_AuthorDelete.clicked.connect(self.deleteAuthorButton)
        self.ui.pushButton_AuthorSearch.clicked.connect(self.searchAuthorButton)
        self.ui.pushButton_AuthorReset.clicked.connect(self.resetAuthorButtonFunction)
        self.ui.pushButton_AuthorRefreshTable.clicked.connect(self.displayAuthorData)

        self.ui.pushButton_SupervisorAdd.clicked.connect(self.addSuperTable)
        self.ui.pushButton_SupervisorUpdate.clicked.connect(self.updateSuperButton)
        self.ui.pushButton_SupervisorDelete.clicked.connect(self.deleteSuperButton)
        self.ui.pushButton_SupervisorSearch.clicked.connect(self.searchSuperButton)
        self.ui.pushButton_SupervisorReset.clicked.connect(self.resetSuperButtonFunction)
        self.ui.pushButton_SupervisorRefreshTable.clicked.connect(self.displaySuperData)


        # SQL TO COMBOBOX  :(

        imlec = db.cursor()
        imlec.execute('SELECT UNI_ID FROM UNIVERSITY')
        a = imlec.fetchall()
        for i in ''.join((map(str, a))):
            if i != '(':
                if i != ')':
                    if i != ',':
                        self.ui.comboBox_UniversityID.addItem(i)
        imlec.close()

        imlec = db.cursor()
        imlec.execute('SELECT INST_ID FROM INSTITUTE')
        a = imlec.fetchall()
        for i in ''.join((map(str, a))):
            if i != '(':
                if i != ')':
                    if i != ',':
                        self.ui.comboBox_InstituteID.addItem(i)
        imlec.close()

    # ------------------------------------UNIVERSITY MENU--------------------------------------

    def addUniTable(self):

        imlec = db.cursor()

        imlec.execute('INSERT INTO UNIVERSITY VALUES(?,?) ',
                      (
                      self.ui.lineEdit_UniversityUniversityID.text(), self.ui.lineEdit_UniversityUniversityName.text()))
        db.commit()
        imlec.close()
        self.displayUniData()

    def resetUniButtonFunction(self):
        self.ui.lineEdit_UniversityUniversityName.setText("")
        self.ui.lineEdit_UniversityUniversityID.setText("")

    def updateUniButton(self):
        imlec = db.cursor()

        imlec.execute('UPDATE UNIVERSITY SET UNI_NAME = ? WHERE UNI_ID = ?',
                      (
                      self.ui.lineEdit_UniversityUniversityName.text(), self.ui.lineEdit_UniversityUniversityID.text()))
        db.commit()
        imlec.close()
        self.displayData()

    def deleteUniButton(self):
        imlec = db.cursor()

        imlec.execute('DELETE FROM UNIVERSITY WHERE  UNI_ID = ? OR UNI_NAME = ?',
                      (
                      self.ui.lineEdit_UniversityUniversityID.text(), self.ui.lineEdit_UniversityUniversityName.text()))
        db.commit()
        imlec.close()
        self.displayData()

    def searchUniButton(self):
        imlec = db.cursor()
        imlec.execute('SELECT * FROM UNIVERSITY WHERE UNI_ID = ? OR UNI_NAME = ?',
                      (
                      self.ui.lineEdit_UniversityUniversityID.text(), self.ui.lineEdit_UniversityUniversityName.text()))

        result = imlec.fetchall()

        self.ui.tableWidget_UniversityTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_UniversityTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_UniversityTable.setItem(row_number, column_number,
                                                            QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    def displayUniData(self):
        imlec = db.cursor()

        imlec.execute('SELECT * FROM UNIVERSITY')
        result = imlec.fetchall()
        self.ui.tableWidget_UniversityTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_UniversityTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_UniversityTable.setItem(row_number, column_number,
                                                            QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    # ------------------------------------AUTHOR MENU--------------------------------------

    def addAuthorTable(self):
        # self.asd = Ui_UniversityControlMenu()
        imlec = db.cursor()

        imlec.execute('INSERT INTO AUTHOR VALUES(?,?,?) ',
                      (self.ui.lineEdit_AuthorSupervisorID.text(), self.ui.lineEdit_AuthorSupervisorLastName.text(),
                       self.ui.lineEdit_AuthorSupervisorFirstName.text()))
        db.commit()
        imlec.close()
        self.displayAuthorData()

    def resetAuthorButtonFunction(self):
        self.ui.lineEdit_AuthorSupervisorID.setText("")
        self.ui.lineEdit_AuthorSupervisorLastName.setText("")
        self.ui.lineEdit_AuthorSupervisorFirstName.setText("")

    def updateAuthorButton(self):
        imlec = db.cursor()

        imlec.execute('UPDATE AUTHOR SET AUTHOR_LNAME = ?, AUTHOR_FNAME = ? WHERE AUTHOR_ID = ?',
                      (self.ui.lineEdit_AuthorSupervisorLastName.text(), self.ui.lineEdit_AuthorSupervisorFirstName.text(),
                      self.ui.lineEdit_AuthorSupervisorID.text()))
        db.commit()
        imlec.close()
        self.displayAuthorData()

    def deleteAuthorButton(self):
        imlec = db.cursor()

        imlec.execute('DELETE FROM AUTHOR WHERE  AUTHOR_ID = ? OR AUTHOR_LNAME = ? OR AUTHOR_FNAME = ?',
                      (self.ui.lineEdit_AuthorSupervisorID.text(), self.ui.lineEdit_AuthorSupervisorLastName.text(),
                       self.ui.lineEdit_AuthorSupervisorFirstName.text()))
        db.commit()
        imlec.close()
        self.displayAuthorData()

    def searchAuthorButton(self):
        imlec = db.cursor()
        imlec.execute('SELECT * FROM AUTHOR WHERE AUTHOR_ID = ? OR AUTHOR_LNAME = ? OR AUTHOR_FNAME = ?',
                      (self.ui.lineEdit_AuthorSupervisorID.text(), self.ui.lineEdit_AuthorSupervisorLastName.text(),
                       self.ui.lineEdit_AuthorSupervisorFirstName.text()))

        result = imlec.fetchall()

        self.ui.tableWidget_AuthorTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_AuthorTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_AuthorTable.setItem(row_number, column_number,
                                                           QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    def displayAuthorData(self):
        imlec = db.cursor()

        imlec.execute('SELECT * FROM AUTHOR')
        result = imlec.fetchall()
        self.ui.tableWidget_AuthorTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_AuthorTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_AuthorTable.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    # ------------------------------------SUPERVISOR MENU--------------------------------------

    def addSuperTable(self):
        # self.asd = Ui_UniversityControlMenu()
        imlec = db.cursor()

        imlec.execute('INSERT INTO SUPER VALUES(?,?,?) ',
                      (self.ui.lineEdit_AuthorSupervisorID.text(), self.ui.lineEdit_AuthorSupervisorLastName.text(),
                       self.ui.lineEdit_AuthorSupervisorFirstName.text()))
        db.commit()
        imlec.close()
        self.displaySuperData()

    def resetSuperButtonFunction(self):
        self.ui.lineEdit_AuthorSupervisorID.setText("")
        self.ui.lineEdit_AuthorSupervisorLastName.setText("")
        self.ui.lineEdit_AuthorSupervisorFirstName.setText("")

    def updateSuperButton(self):
        imlec = db.cursor()

        imlec.execute('UPDATE SUPER SET SUPER_LNAME = ?, SUPER_FNAME = ? WHERE SUPER_ID = ?',
                      (self.ui.lineEdit_AuthorSupervisorLastName.text(), self.ui.lineEdit_AuthorSupervisorFirstName.text(),
                      self.ui.lineEdit_AuthorSupervisorID.text()))
        db.commit()
        imlec.close()
        self.displaySuperData()

    def deleteSuperButton(self):
        imlec = db.cursor()

        imlec.execute('DELETE FROM SUPER WHERE  SUPER_ID = ? OR SUPER_LNAME = ? OR SUPER_FNAME = ?',
                      (self.ui.lineEdit_AuthorSupervisorID.text(), self.ui.lineEdit_AuthorSupervisorLastName.text(),
                       self.ui.lineEdit_AuthorSupervisorFirstName.text()))
        db.commit()
        imlec.close()
        self.displaySuperData()

    def searchSuperButton(self):
        imlec = db.cursor()
        imlec.execute('SELECT * FROM SUPER WHERE SUPER_ID = ? OR SUPER_LNAME = ? OR SUPER_FNAME = ?',
                      (self.ui.lineEdit_AuthorSupervisorID.text(), self.ui.lineEdit_AuthorSupervisorLastName.text(),
                       self.ui.lineEdit_AuthorSupervisorFirstName.text()))

        result = imlec.fetchall()

        self.ui.tableWidget_SupervisorTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_SupervisorTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_SupervisorTable.setItem(row_number, column_number,
                                                           QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    def displaySuperData(self):
        imlec = db.cursor()

        imlec.execute('SELECT * FROM SUPER')
        result = imlec.fetchall()
        self.ui.tableWidget_SupervisorTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_SupervisorTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_SupervisorTable.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    # ------------------------------------INSTITUTE MENU--------------------------------------

    def addInstTable(self):
        # self.asd = Ui_UniversityControlMenu()
        imlec = db.cursor()

        imlec.execute('INSERT INTO INSTITUTE VALUES(?,?,?) ',
                      (self.ui.lineEdit_InstituteInstituteID.text(), self.ui.lineEdit_InstituteUniversityID.text(),
                       self.ui.lineEdit_InstituteInstituteName.text()))
        db.commit()
        imlec.close()
        self.displayInstData()

    def resetInstButtonFunction(self):
        self.ui.lineEdit_InstituteUniversityID.setText("")
        self.ui.lineEdit_InstituteInstituteName.setText("")
        self.ui.lineEdit_InstituteInstituteID.setText("")

    def updateInstButton(self):
        imlec = db.cursor()

        imlec.execute('UPDATE INSTITUTE SET UNI_ID = ?, INST_NAME = ? WHERE INST_ID = ?',
                      (self.ui.lineEdit_InstituteUniversityID.text(), self.ui.lineEdit_InstituteInstituteName.text(),
                       self.ui.lineEdit_InstituteInstituteID.text()))
        db.commit()
        imlec.close()
        self.displayInstData()

    def deleteInstButton(self):
        imlec = db.cursor()

        imlec.execute('DELETE FROM INSTITUTE WHERE  INST_ID = ? OR UNI_ID = ? OR INST_NAME = ?',
                      (self.ui.lineEdit_InstituteInstituteID.text(), self.ui.lineEdit_InstituteUniversityID.text(),
                       self.ui.lineEdit_InstituteInstituteName.text()))
        db.commit()
        imlec.close()
        self.displayInstData()

    def searchInstButton(self):
        imlec = db.cursor()
        imlec.execute('SELECT * FROM INSTITUTE WHERE INST_ID = ? OR UNI_ID = ? OR INST_NAME = ?',
                      (self.ui.lineEdit_InstituteInstituteID.text(), self.ui.lineEdit_InstituteUniversityID.text(),
                       self.ui.lineEdit_InstituteInstituteName.text()))

        result = imlec.fetchall()

        self.ui.tableWidget_InstituteTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_InstituteTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_InstituteTable.setItem(row_number, column_number,
                                                           QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    def displayInstData(self):
        imlec = db.cursor()

        imlec.execute('SELECT * FROM INSTITUTE')
        result = imlec.fetchall()
        self.ui.tableWidget_InstituteTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_InstituteTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_InstituteTable.setItem(row_number, column_number,
                                                           QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    # ------------------------------------LANGUAGE MENU ***(REMOVED)*** --------------------------------------

    # def addLangTable(self):
    #
    #     imlec = db.cursor()
    #
    #     imlec.execute('INSERT INTO LANG VALUES(?) ', (self.ui.lineEdit_LanguageLanguage.text()))
    #     db.commit()
    #     imlec.close()
    #     self.displayLangData()
    #
    # def resetLangButtonFunction(self):
    #     self.ui.lineEdit_LanguageLanguage.setText("")
    #
    # def updateLangButton(self):
    #     imlec = db.cursor()
    #
    #     imlec.execute('UPDATE LANG SET THE_LANG = ?', (self.ui.lineEdit_LanguageLanguage.text()))
    #     db.commit()
    #     imlec.close()
    #     self.displayLangData()
    #
    # def deleteLangButton(self):
    #     imlec = db.cursor()
    #
    #     imlec.execute('DELETE FROM LANG WHERE THE_LANG = ?', (self.ui.lineEdit_LanguageLanguage.text()))
    #     db.commit()
    #     imlec.close()
    #     self.displayLangData()
    #
    # def searchLangButton(self):
    #     imlec = db.cursor()
    #     imlec.execute('SELECT * FROM LANG WHERE THE_LANG = ?', (self.ui.lineEdit_LanguageLanguage.text()))
    #
    #     result = imlec.fetchall()
    #
    #     self.ui.tableWidget_LanguageTable.setRowCount(0)
    #     for row_number, row_data in enumerate(result):
    #         self.ui.tableWidget_LanguageTable.insertRow(row_number)
    #         for column_number, data in enumerate(row_data):
    #             self.ui.tableWidget_LanguageTable.setItem(row_number, column_number,
    #                                                       QtWidgets.QTableWidgetItem(str(data)))
    #     imlec.close()

    def displayLangData(self):
        imlec = db.cursor()

        imlec.execute('SELECT * FROM LANG')
        result = imlec.fetchall()
        self.ui.tableWidget_LanguageTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_LanguageTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_LanguageTable.setItem(row_number, column_number,
                                                          QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    # -----------------------------------------  MAIN ----------------------------------------

    def exitButtonFuction(self):
        db.close()
        exit()

    def resetButtonFunction(self):
        self.ui.lineEdit_ThesisNo.setText("")
        self.ui.lineEdit_ThesisTitle.setText("")
        self.ui.lineEdit_ThesisAbs.setText("")
        self.ui.comboBox_Type.setCurrentText("")
        self.ui.lineEdit_ThesisYear.setText("")
        self.ui.lineEdit_ThesisPageNo.setText("")
        self.ui.comboBox_Language.setCurrentText("")
        self.ui.lineEdit_ThesisSubDate.setText("")
        self.ui.lineEdit_ThesisAuthorID.setText("")
        self.ui.lineEdit_ThesisSuperID.setText("")
        self.ui.comboBox_UniversityID.setCurrentText("")
        self.ui.comboBox_InstituteID.setCurrentText("")

    def displayData(self):
        imlec = db.cursor()

        imlec.execute('SELECT * FROM THESIS')
        result = imlec.fetchall()
        self.ui.tableWidget_ThesisTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_ThesisTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_ThesisTable.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

    def readtable(self):
        rowCount = self.ui.tableWidget_ThesisTable.rowCount()
        columnCount = self.ui.tableWidget_ThesisTable.columnCount()

    def updateButton(self):
        imlec = db.cursor()

        imlec.execute('UPDATE THESIS SET THE_TITLE = ?, THE_ABS = ?, THE_TYPE = ?, THE_YEAR= ?, THE_NUM_PAGES = ?, '
                      'THE_LANG = ?, THE_SUB_DATE = ?, AUTHOR_ID = ?, SUPER_ID = ?, UNI_ID = ?,  INST_ID = ?  '
                      ' WHERE THE_NO = ?',
                      (self.ui.lineEdit_ThesisTitle.text(), self.ui.lineEdit_ThesisAbs.text(),
                       self.ui.comboBox_Type.currentText(),
                       self.ui.lineEdit_ThesisYear.text(), self.ui.lineEdit_ThesisPageNo.text(),
                       self.ui.comboBox_Language.currentText(),
                       self.ui.lineEdit_ThesisSubDate.text(), self.ui.lineEdit_ThesisAuthorID.text(),
                       self.ui.lineEdit_ThesisSuperID.text(),
                       self.ui.comboBox_UniversityID.currentText(), self.ui.comboBox_InstituteID.currentText(),
                       self.ui.lineEdit_ThesisNo.text()))
        db.commit()
        imlec.close()
        self.displayData()

    def addTable(self):

        imlec = db.cursor()

        imlec.execute('INSERT INTO THESIS VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ',
                      (self.ui.lineEdit_ThesisNo.text(), self.ui.lineEdit_ThesisTitle.text(),
                       self.ui.lineEdit_ThesisAbs.text(), self.ui.comboBox_Type.currentText(),
                       self.ui.lineEdit_ThesisYear.text(), self.ui.lineEdit_ThesisPageNo.text(),
                       self.ui.comboBox_Language.currentText(),
                       self.ui.lineEdit_ThesisSubDate.text(), self.ui.lineEdit_ThesisAuthorID.text(),
                       self.ui.lineEdit_ThesisSuperID.text(),
                       self.ui.comboBox_UniversityID.currentText(), self.ui.comboBox_InstituteID.currentText()))
        db.commit()
        imlec.close()
        self.displayData()

    def deleteButton(self):
        imlec = db.cursor()

        imlec.execute('DELETE FROM THESIS WHERE  THE_NO = ?', (self.ui.lineEdit_ThesisNo.text(),))
        db.commit()
        imlec.close()
        self.displayData()

    def searchButton(self):
        imlec = db.cursor()
        imlec.execute('SELECT * FROM THESIS WHERE THE_NO = ? OR THE_TITLE = ? OR THE_ABS = ? OR THE_TYPE = ? OR '
                      'THE_YEAR= ? OR THE_NUM_PAGES = ? OR THE_LANG = ? OR THE_SUB_DATE = ? OR AUTHOR_ID = ? OR '
                      'SUPER_ID = ? OR UNI_ID = ? OR  INST_ID = ?  ',
                      (self.ui.lineEdit_ThesisNo.text(), self.ui.lineEdit_ThesisTitle.text(),
                       self.ui.lineEdit_ThesisAbs.text(), self.ui.comboBox_Type.currentText(),
                       self.ui.lineEdit_ThesisYear.text(), self.ui.lineEdit_ThesisPageNo.text(),
                       self.ui.comboBox_Language.currentText(), self.ui.lineEdit_ThesisSubDate.text(),
                       self.ui.lineEdit_ThesisAuthorID.text(), self.ui.lineEdit_ThesisSuperID.text(),
                       self.ui.comboBox_UniversityID.currentText(), self.ui.comboBox_InstituteID.currentText()))

        result = imlec.fetchall()

        self.ui.tableWidget_ThesisTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_ThesisTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_ThesisTable.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))
        imlec.close()

def app():
    application = QtWidgets.QApplication(sys.argv)
    win = App()
    # win.show()
    win.showMaximized()
    sys.exit(application.exec_())


app()
