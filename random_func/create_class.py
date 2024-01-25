class Dog: 
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def sound(self):
        print(self.name + ' Bark!')

myDog = Dog('Rover')
anotherDog = Dog('GiGi')

myDog.sound()
anotherDog.sound()