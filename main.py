from math import radians
from PyQt5 import QtWidgets
from design import Ui_MainWindow
from random import randint
import sys

from employee import Employee

def addEmployee(ui: Ui_MainWindow):
    if not ui.showFieldEmpty():
        return
    id = ui.lblUID.text()
    name = ui.txtName.toPlainText()
    age = ui.txtAge.toPlainText()
    salary = ui.txtSalary.toPlainText()
    employee: Employee = Employee(id, name, age, salary)
    ui.employeeList.append(employee)
    ui.clr()
    ui.refreshTableData(ui.employeeList)
    ui.generateID()
    ui.updateTotalEmplCnt(len(ui.employeeList))
    ui.showMessageBox("Employee Added", "Your request to add a new employee is successfull")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnAdd.clicked.connect(lambda: addEmployee(ui))
    MainWindow.show()
    sys.exit(app.exec_())