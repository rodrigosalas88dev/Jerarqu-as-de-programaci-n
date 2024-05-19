"""
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
"""

"""
Ejercicio
"""


class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Waw, Waw!")


class Cat(Animal):

    def sound(self):
        print("Miau, miau!")


def print_sound(animal: Animal):
    animal.sound()


my_animal = Animal("Animal")
my_dog = Dog("Kiro")
my_cat = Cat("Mila")
print_sound(my_dog)
print_sound(my_cat)

"""
Extra
"""


class Employee:

    def __init__(self, id: int, name: str):
        self.name = name
        self.id = id
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def coordinate_project(self):
        print(f"{self.name} esta coordinando varios proyectos")


class ProjectManager(Employee):

    def coordinate_project(self):
        print(f"{self.name} esta coordinando un proyecto")

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project


class Programmer(Employee):

    def __init__(self, id: int, name: str, lenguage: str):
        super().__init__(id, name)
        self.lenguage = lenguage

    def code(self):
        print(f"{self.name} esta programando en lenguaje {self.lenguage}")

    def add_employee(self, employee: Employee):
        print(f"Un programador no puede agregar empleados a su cargo. {
              employee.name} no se añadirá")


my_manager = Manager(1, "Mouredev")
my_project_manager = ProjectManager(2, "Brais", "Poyecto 1")
my_project_manager2 = ProjectManager(3, "Rodri", "Poyecto 2")
my_programmer = Programmer(4, "Salas", "Python")
my_programmer2 = Programmer(5, "Jose", "Java Script")
my_programmer3 = Programmer(6, "Sebastian", "Java")
my_programmer4 = Programmer(7, "Nelly", "C++")

my_manager.add_employee(my_project_manager)
my_manager.add_employee(my_project_manager2)
my_project_manager.add_employee(my_programmer)
my_project_manager.add_employee(my_programmer2)
my_project_manager2.add_employee(my_programmer3)
my_project_manager2.add_employee(my_programmer4)
my_programmer.add_employee(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_project()

my_manager.print_employees()
my_project_manager.print_employees()
my_project_manager2.print_employees()
my_programmer.print_employees()
