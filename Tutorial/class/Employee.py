class Employee:

	raise_amount = 1.04

	def __init__(self,first,last,salary):
		self.first = first
		self.last = last
		self.salary = salary
		self.email = first + '.' + last + '@e.ntu.edu.sg'
	def fullname(self):
        return '{}{}'.format(self.first,self.last)

    def salary_raise(self,amount):
    	self.salary = int (self.salary * raise_amount)
    
