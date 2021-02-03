class Employee:
    employee_counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1
    def display_counter(self):
        print('Всего сотрудников: ', Employee.employee_counter)
    def info_of_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))


emp1 = Employee('Артем', 10000)
emp2 = Employee('Ирина', 5000)
emp3 = Employee('Эрик', 1000)
emp1.info_of_employee()
emp2.info_of_employee()
emp3.info_of_employee()
print('Всего сотрудников', Employee.employee_counter)

emp1.age = 7  # Добавит атрибут 'age'.
emp1.age = 8  # Изменит атрибут 'age'.
del emp1.age  # Удалит атрибут 'age'.


hasattr(emp1, 'age')  # возвращает true если атрибут 'age' существует
getattr(emp1, 'age')  # возвращает значение атрибута 'age'
setattr(emp1, 'age', 8)  # устанавливает атрибут 'age' на 8
delattr(emp1, 'age')  # удаляет атрибут 'age'
'''
__dict__ — словарь, содержащий пространство имен класса.
__doc__ — строка документации класса. None если, документация отсутствует.
__name__ — имя класса.
__module__ — имя модуля, в котором определяется класс. Этот атрибут __main__ в интерактивном режиме.
__bases__ — могут быть пустые tuple, содержащие базовые классы, в порядке их появления в списке базового класса.
Так же есть наслеование классов
'''