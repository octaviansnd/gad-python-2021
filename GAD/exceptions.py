class Animal:
    def __init__(self, name):
        self.name = name

    def pee(self):
        print(f'{self.name} is peeing on my shoe!')


class Dog(Animal):
    def bark(self):
        print(f'{self.name}: HAM! HAM!')

    def pet(self):
        while True:
            try:
                var = int(input(f'How many times do you want to pet {self.name}?: '))
            except ValueError:
                print('I said a number you son of a b*tch!!!')
            else:
                break
        print(f'I want to pet {self.name} {var} times!')


dog1 = Dog('Marius')
dog1.pee()
dog1.bark()
dog1.pet()


