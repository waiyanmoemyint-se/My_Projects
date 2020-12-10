class EmployeeRecord:
    def __init__(self,empName,empMobile,empSalary,empEmail,empPosition):
        self.employee_Name = empName
        self.employee_Mobile = empMobile
        self.employee_Salary =  empSalary
        self.employee_Email  =  empEmail
        self.employee_Position  = empPosition

class Accounting:
    def __init__(self):
        self.profit = 0
        self.sale   = 45000
        self.salaries = 4560000

    def profitLost(self):
        if self.profit >0:
            return ("Congraulations You company is in the profit")
        elif self.profit<0:
            return ("Company is'nt in profit nor in loss")
        else:
            return ("Company is in the loss")

class Marketing:
    def __init__(self):
        self.pendingOrders  = 20
        self.delivering     = 15
        self.totalOrders     = 90

accObject = Accounting()
print(accObject.profitLost())





