class Animal:
    """ An animal class with name, parent to cat class and dog class """
    def __init__(self, name):
        """ Initialize its name then send a constructor message """
        self.name = name
        self.constructor_message()

    # Use static method since all instances will print the same thing
    @staticmethod
    def eat():
        """ Print out animal eating sounds """
        print("Munch munch.")

    def make_noise(self):
        """ Print out animal grunt with its name """
        print(f"Grrr! says {self.name}.")
    
    # Also static method since all instances will print the same thing
    @staticmethod
    def constructor_message():
        """ Called within the constructor (to inform users) """
        print("An animal has been born.")



class Cat(Animal):
    """ A Cat class inheriting from Animal class """
    def __init__(self, name):
        """  Initialize the name by calling the parent's (Animal) constructor """
        super().__init__(name)

    def make_noise(self):
        """ Overide the parent's make noise method, this time printing cat sounds """
        print(f"Meow says {self.name}.")

    @staticmethod
    def constructor_message():
        """ Overide the parent's constructor mesage method, this time saying cat instead of animal """
        print("A cat has been born.")

class Dog(Animal):
    """ A Dog class inheriting from Animal class """
    def __init__(self, name):
        """  Initialize the name by calling the parent's (Animal) constructor """
        super().__init__(name)

    def make_noise(self):
        """ Overide the parent's make noise method, this time printing dog sounds """
        print(f"Bark says {self.name}.")

    @ staticmethod
    def constructor_message():
        """ Overide the parent's constructor mesage method, this time saying dog instead of animal """
        print("A dog has been born.")



# TEST (suggest using the uploaded test.py for testing)
def main():
    print()
    # Create a cat, then make it eat and make noise
    cat1 = Cat("Garfield")
    cat1.eat()
    cat1.make_noise()

    print()
    # Create the first dog, then make it eat and make noise
    dog1 = Dog("Scooby-Doo")
    dog1.eat()
    dog1.make_noise()

    print()
    # Create the second dog, then make it eat and make noise
    dog2 = Dog("Pluto")
    dog2.eat()
    dog2.make_noise()

    print()
    # Create an animal, then make it eat and make noise
    animal1 = Animal("Beast Boy")
    animal1.eat()
    animal1.make_noise()

if __name__ == "__main__":
    main()