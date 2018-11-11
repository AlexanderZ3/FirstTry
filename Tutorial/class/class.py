class Employee():
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.' +last +'@compay.com'
    def fullname(self):
        string = '{} + {}'.format(self.first, self.last)
        return  string

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

    def __repr__(self):
        return "Employee('{}','{}')".format(self.first,self.email)

    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)

emp_1 = Employee('abd','whd',4000)
emp_2 = Employee('Alex','Jourge',5000)

print(emp_1)
emp_1.apply_raise()
