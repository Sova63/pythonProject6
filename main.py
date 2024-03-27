
from EmployeeRepos import EmployeeRepos

def addEmployee():
	name = input("")
	surname = input("")
	position = input("")
	repos.add_employee(name=name,surname=surname,position=position)
	print("Сотрудник добавлен")

def view_all_employee():
	data = repos.get_all_employee()
	for key,value in data.items():
		print(key,'-',value.__dict__)

def update_employee_by_id():
	flagg = True
	employee_id = (int(input("Введите ид работника")))
	employee = repos.get_employee_bi_id(employee_id)
	print("Введите наименование атрибута который необходимо поменять")
	for key in employee__dict__.keys():
		print(key)
	while flagg:
		attibute_name = input(">>")
		value = input(f"Введите новое значение(старое{employee.__dict__[attribute_name]})\n>>")
		repos.set_attr_value_by_id(employee_id,attibute_name,value)
		flagg = isNeedMoreChange == 'У'

if __name__=='__main__':
	repos = EmployeeRepos()
	command = [
		{'name':"add","function":addEmployee,"description":"Добавить сотрудника в базу"},
		{'name': "view all", "function":view_all_employee, "description": "Посмотреть всех сотрудников"}
		{'name': "get_by_id", "function": get_employee_by_id, "description": "Посмотреть сотрудника по ид"}
		{'name': "add", "function": update_employee_by_id, "description": "Изменить сотрудника по ид"}
		{'name': "view last", "function": view_last_employee, "description": "Изменить сотрудника по ид"}

	]
	while True:
		isNeedHelp = input("Ввести список команд у/п").strip().lower()
		if isNeedHelp =="У":
			for command in commands:
				print(command['name'],"-",command["description"])
		userChose = input(">>").strip().lower()
		for command in commands:
			if userChose == command["name"]:
				command["function"]()


	#repos.add_employee(name="Имя",surname = "Фамилие",position = "Должность")
	#print(repos.get_attr_value_by_id(0,'position'))
	#employee = Employee(name="Имя2",surname="Фамилие2",position="Должность2")
	#repos.add_employee(employee=employee)
	#print(repos.get_all_employee())

