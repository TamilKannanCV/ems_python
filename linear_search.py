from typing import List
from employee import Employee
def linearSearch(datas, toFind: str) -> Employee:
    
    for data in datas:
        employee: Employee = data
        if employee.name == toFind:
            return employee
    
    return None
