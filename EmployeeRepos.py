from Emloyee import Employee
class EmployeeRepos:
	def __init__(self):
		self._repos = {}
	def add_employee(self,**kwargs):
		if "employee" in kwargs.keys():
			self._repos.update({self.lastid:kwargs['employee']})
			self.lastid += 1
		elif "name" in kwargs.keys() and "surname" in kwargs.keys() and "position" in kwargs.keys():
			tempEmployee = Employee(kwargs['name'],kwargs['surname'],kwargs['position'])
			self.add_employee(employee=tempEmployee)

	def get_all_employee(self):
		return self._repos

	def get_attr_value_bi_id(self,id:int,attribute_name:str):
		if self._is_attr_exsist(id,attribute_name):
		return self.repos[id].__dict__[attribute_name]



#{
#	"id":Employee
#}