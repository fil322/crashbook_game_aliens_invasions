class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} {self.age} years old.')

    def greet_user(self):
        print(f'Hi {self.first_name} {self.last_name}')

# alex = User('Alex', 'Alexov', 21)
# jon = User('Jhon', 'Kolov', 29)
#
# alex.describe_user()
# alex.greet_user()
# jon.describe_user()
# jon.greet_user()

class Admin(User):

    def __init__(self, priveleges):
        self.priveleges = priveleges