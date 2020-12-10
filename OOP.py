class EmployeeRecord:
    def __init__(self,empName,empMobile,empSalary,empEmail,empPosition):
        self.employee_Name = empName
        self.employee_Mobile = empMobile
        self.employee_Salary =  empSalary
        self.employee_Email  =  empEmail
        self.employee_Position  = empPosition

class Accounting:
    def __init__(self):
        self.profit = 1500000
        self.sale   = 45000
        self.salaries = 4560000

class Marketing:
    def __init__(self):
        self.pendingOrders  = 20
        self.delivering     = 15
        self.totalOrders     = 90
print("\n___________________________________________")
empObject  = EmployeeRecord("WaiYan MoeMyint","09764599920",150000,"wymm999@gmail.com","Software Engineering")
print(empObject.employee_Email)
print(empObject.employee_Position)
print(empObject.employee_Name)
print(empObject.employee_Mobile)
print(empObject.employee_Salary)

print("\n___________________________________________")
accounting_object   = Accounting()
print(accounting_object.sale)
print(accounting_object.profit)
print(accounting_object.salaries)

print("\n___________________________________________")
marketing_object   = Marketing()
print(marketing_object.delivering)
print(marketing_object.pendingOrders)
print(marketing_object.totalOrders)


