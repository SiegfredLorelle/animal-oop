class Animal:

    def __init__(self, name):
        self.name = name
        self.constructor_message()

    @staticmethod
    def eat():
        print("Munch munch.")

    def make_noise(self):
        print(f"Grrr! says {self.name}.")
    
    @staticmethod
    def constructor_message():
        print("An animal has been born.")



class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"Meow says {self.name}.")

    @staticmethod
    def constructor_message():
        print("A cat has been born.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"Bark says {self.name}.")

    @ staticmethod
    def constructor_message():
        print("A dog has been born.")
