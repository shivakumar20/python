#Dunder_Method
class Monster:

    #Attributes
    #health = 90
    #energy = 40

    #-----------Dunder_Method------------
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy
        print(f'The new values of health and energy : {self.health} , {self.energy}')

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        print("The monster was called ")

    def __add__(self,other):
        return self.health + other
    
    def __str__(self):
        return f'A monster with {self.health} and energy {self.energy}'

    #Methods
    def attack(self,amount):
        print('The monster has attacked! ')
        print(f'{amount} damage is dealt')
        monster.energy = 20
        print(monster.energy)

    def move(self,speed):
        print(f'The speed of the monster is : {speed}')

monster = Monster(25,50)
monster1 = Monster(health=40,energy=80)

print(len(monster1))

print(f'The list of dunder methodes : {dir(monster1)}')

monster1()

print(monster1 + 20)

print(monster1)