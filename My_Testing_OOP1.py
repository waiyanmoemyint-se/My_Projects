class Employees:
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + " " + last +"@company.com"
    def fullname(self):
        return "{} {} {}".format(self.first,self.last,self.pay)

emp_1  = Employees("Miracle","James",23121212)
emp_2  = Employees("Stock","Jam",2321212)



print(Employees.fullname(emp_1))
print(Employees.fullname(emp_2))

