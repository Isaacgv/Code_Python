"""Desafio."""
from abc import ABC, abstractmethod


class Department:
    """Department."""

    def __init__(self, name, code):
        """Department."""
        self.name = name
        self.code = code


class Employee(ABC):
    """Employee info."""

    def __init__(self, code, name, salary):
        """Employee."""
        self.code = code
        self.name = name
        self.salary = salary

    @abstractmethod
    def calc_bonus(self):
        """Bonus."""
        pass

    def get_hours(self):
        """Hours."""
        return 8


class Manager(Employee):
    """Manager info."""

    def __init__(self, code, name, salary):
        """Manager."""
        super().__init__(code, name, salary)
        self.__department = Department('managers', 1)

    def get_departament(self):
        """Departament Name."""
        return self.__department.name

    def calc_bonus(self):
        """Bonus."""
        return self.salary * 0.15

    def set_departament(self, name):
        """Change Departament."""
        self.__departament.name = name


class Seller(Employee):
    """Seller info."""

    def __init__(self, code, name, salary):
        """Seller."""
        super().__init__(code, name, salary)
        self.department = Department('sellers', 2)
        self.__sales = 0

    def get_departament(self):
        """Department."""
        return self.department.name

    def calc_bonus(self):
        """Bonus."""
        return self.__sales * 0.15

    def set_department(self, name):
        """Set Departament."""
        self.department.name = name

    def get_sales(self):
        """Obtain total sale."""
        return self.__sales

    def put_sales(self, sale):
        """Put Sales."""
        self.__sales += sale
