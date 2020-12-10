#inheritance

class EmployeeRecord:
    def __init__(self):
        self.empName = "Parker"
        self.empAddress = "Yangon"
        self.empPhone   = 4523
        self.empPositioin = "Software Engineering"

    def empReleaionship(self):
        return "Single "

class Accounting(EmployeeRecord):
    def getName(self):
        return self.empName

object = Accounting()
print(object.getName())
print(object.empAddress)

