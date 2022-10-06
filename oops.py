class Monster:

    #Attributes
    health = 90
    energy = 40

    #Methods
    def attack(self,amount):
        print('The monster has attacked! ')
        print(f'{amount} damage is dealt')
        monster.energy = 20
        print(monster.energy)

    def move(self,speed):
        print(f'The speed of the monster is : {speed}')

monster = Monster()
monster1 = Monster()
monster2 = Monster()
monster3  = Monster()