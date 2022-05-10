class Employee():
    """Сбор данных о работнике."""
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase = 5000):
        """Увеличение оклада"""
        new_salary = self.salary + increase
        return new_salary