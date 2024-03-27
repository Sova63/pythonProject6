
from EmployeeRepos import EmployeeRepos
if __name__=='__main__':
	repos = EmployeeRepos()
	repos.add_employee(name="Имя",surname = "Фамилие",position = "Должность")
	print(repos.get_attr_value_bi_id(0,'position'))
	employee = Employee(name="Имя2",surname="Фамилие2",position="Должность2")
	repos.add_employee(employee=employee)
	print(repos.get_all_employee())

