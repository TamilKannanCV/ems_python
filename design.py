import random
from PyQt5 import QtCore, QtGui, QtWidgets
from linear_search import linearSearch
from employee import Employee

class Ui_MainWindow(object):
    
    employeeList = list()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(630, 702)
        MainWindow.setMaximumSize(QtCore.QSize(630, 702))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 601, 131))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.txtSalary = QtWidgets.QTextEdit(self.groupBox)
        self.txtSalary.setGeometry(QtCore.QRect(90, 80, 171, 31))
        self.txtSalary.setObjectName("txtSalary")
        self.txtAge = QtWidgets.QTextEdit(self.groupBox)
        self.txtAge.setGeometry(QtCore.QRect(290, 40, 171, 31))
        self.txtAge.setObjectName("txtAge")
        self.lblUID = QtWidgets.QLabel(self.groupBox)
        self.lblUID.setGeometry(QtCore.QRect(20, 40, 65, 30))
        self.lblUID.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUID.setObjectName("lblUID")
        self.generateID()
        self.txtName = QtWidgets.QTextEdit(self.groupBox)
        self.txtName.setGeometry(QtCore.QRect(90, 40, 171, 31))
        self.txtName.setObjectName("txtName")
        self.txtName.setFocus()
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(520, 150, 90, 26))
        self.btnAdd.setObjectName("btnAdd")
        self.btnClr = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clr())
        self.btnClr.setGeometry(QtCore.QRect(420, 150, 90, 26))
        self.btnClr.setObjectName("btnClr")
        self.btnDisp = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.showDetails())
        self.btnDisp.setGeometry(QtCore.QRect(320, 150, 90, 26))
        self.btnDisp.setObjectName("btnDisp")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 601, 281))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tblAllEmployees = QtWidgets.QTableWidget(self.groupBox_2)
        self.tblAllEmployees.setGeometry(QtCore.QRect(10, 31, 581, 211))
        self.tblAllEmployees.setObjectName("tblAllEmployees")
        self.tblAllEmployees.setColumnCount(4)
        self.tblAllEmployees.horizontalHeader().setStretchLastSection(True)
        self.tblAllEmployees.setHorizontalHeaderLabels(["ID","Name", "Age", "Salary"])
        self.tblAllEmployees.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblAllEmployees.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tblAllEmployees.itemSelectionChanged.connect(self.selectionItemChanged)
        self.lblTotalEmpl = QtWidgets.QLabel(self.groupBox_2)
        self.lblTotalEmpl.setGeometry(QtCore.QRect(430, 250, 171, 20))
        self.lblTotalEmpl.setScaledContents(False)
        self.lblTotalEmpl.setWordWrap(False)
        self.lblTotalEmpl.setObjectName("lblTotalEmpl")
        self.updateTotalEmplCnt(0)
        self.btnDelete = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDelete.setEnabled(False)
        self.btnDelete.setGeometry(QtCore.QRect(10, 247, 86, 30))
        self.btnDelete.setCheckable(False)
        self.btnDelete.setFlat(False)
        self.btnDelete.setObjectName("btnDelete")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 480, 601, 181))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.txtSearchName = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtSearchName.setGeometry(QtCore.QRect(10, 30, 171, 31))
        self.txtSearchName.setObjectName("txtSearchName")
        self.btnSearch = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSearch.setGeometry(QtCore.QRect(200, 30, 86, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.btnSearch.clicked.connect(self.onSearch)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 131, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblSearchResult = QtWidgets.QLabel(self.groupBox_3)
        self.lblSearchResult.setGeometry(QtCore.QRect(20, 100, 581, 81))
        self.lblSearchResult.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblSearchResult.setObjectName("lblSearchResult")
        self.btnAbt = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbt.setGeometry(QtCore.QRect(530, 670, 86, 26))
        self.btnAbt.setFlat(True)
        self.btnAbt.setObjectName("btnAbt")
        self.btnAbt.clicked.connect(self.showAbtDialog)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Record Management"))
        self.groupBox.setTitle(_translate("MainWindow", "Employee Details"))
        self.txtSalary.setPlaceholderText(_translate("MainWindow", "Employee Salary"))
        self.txtAge.setPlaceholderText(_translate("MainWindow", "Employee Age"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "Employee Name"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnClr.setText(_translate("MainWindow", "Clear"))
        self.btnDisp.setText(_translate("MainWindow", "Show All"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Employees Found"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Search Employee"))
        self.txtSearchName.setPlaceholderText(_translate("MainWindow", "Search by name"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Search Result:"))
        self.lblSearchResult.setText(_translate("MainWindow", "n/a"))
        self.btnAbt.setText(_translate("MainWindow", "About"))


    # Clears the field
    def clr(self):
        self.txtName.clear()
        self.txtAge.clear()
        self.txtSalary.clear()
    
    def generateID(self):
        self.lblUID.setText(str(random.randint(111, 999)))

    def updateTotalEmplCnt(self, cnt:int):
        self.lblTotalEmpl.setText("Total employees: " + str(cnt))

    def refreshTableData(self, data:list):
        self.tblAllEmployees.setRowCount(data.__len__())
        for index, value in enumerate(data):
            employee: Employee = value
            self.tblAllEmployees.setItem(index, 0, QtWidgets.QTableWidgetItem(employee.id))
            self.tblAllEmployees.setItem(index, 1, QtWidgets.QTableWidgetItem(employee.name))
            self.tblAllEmployees.setItem(index, 2, QtWidgets.QTableWidgetItem(employee.age))
            self.tblAllEmployees.setItem(index, 3, QtWidgets.QTableWidgetItem(employee.salary))
            self.tblAllEmployees.itemPressed.connect(self.onItemSelected)

    def onSearch(self):
        searchStr = self.txtSearchName.toPlainText()
        if not searchStr:
            self.showMessageBox("Search error", "Enter a name to search")
            return
        
        employee: Employee = linearSearch(self.employeeList, searchStr)
        if employee is None:
            self.lblSearchResult.setText("No result found")
        else:
            self.lblSearchResult.setText("ID: " + employee.id + "\nName: "+ employee.name + "\n"+ "Age: "+ employee.age + "\n"+ "Salary: Rs " + employee.salary)
    
    # Shows a message box
    def showMessageBox(self, title:str, message: str):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowIcon(QtGui.QIcon("logo.png"))
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            msgBox.close()

    def showDetails(self):
        details = "Employee details"
        if self.employeeList.__len__() == 0:
            self.showMessageBox("Details", "No details found to display")
            return
        for i in self.employeeList:
            emp: Employee = i
            details += "\n" + emp.id + "\n\tName: " + emp.name + "\n\tAge: "+emp.age + "\n\tSalary: " + emp.salary
        self.showMessageBox("Details", details)

    def onItemSelected(self, item :QtWidgets.QTableWidgetItem):
        self.btnDelete.setEnabled(True)
        self.btnDelete.clicked.connect(lambda :self.deleteClicked(item) )

    def deleteClicked(self, item):
        self.employeeList.pop(item.row())
        self.refreshTableData(self.employeeList)
        self.updateTotalEmplCnt(len(self.employeeList))
        self.showMessageBox(title="Employee deleted", message="Your request for deleting employee is successful")

    def showFieldEmpty(self) -> bool:
        if not self.txtName.toPlainText().strip() or not self.txtAge.toPlainText().strip() or not self.txtSalary.toPlainText().strip():
            self.showMessageBox(title="Fill required fields", message="Make sure to fill all the necessary fileds")
            return False
        return True

    def showAbtDialog(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("About")
        msgBox.setWindowIcon(QtGui.QIcon("logo.png"))
        msgBox.setText("This project is developed for 'Data Structure Mini Project' by \n\t - Tamil Kumaran S\n\t - Tamil Kannan C V")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            msgBox.close()

    def selectionItemChanged(self):
        if self.tblAllEmployees.selectedItems().__len__() == 0:
            self.btnDelete.setEnabled(False)
        
