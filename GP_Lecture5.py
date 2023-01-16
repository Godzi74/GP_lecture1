import random

class Collectible:

    totalPoints = 0
    def __int__(self, name):
        self.name = name

    def Collect(self):
        Collectible.totalPoints += self.value

class Coin(Collectible):
    def __int__(self, name, value):
        Collectible.__int__(self, name)
        self.value = value

class Potion(Collectible):

    colour = {"Red": 50, "Blue": 100, "Green": 150}

    def __int__(self, name, value):
        Collectible.__int__(self, name)
        self.value = value
        self.colour = random.choice(list(Potion.colour))

potions = Potion()

class Enemy:
    weapons = {"Sword": 5, "Lance": 10, "Axe": 15}

    names = ["Edwin", "Harry", "Benadryl", "Katie", "Manan"]
    locations = ["Krypton", "Uxbridge", "Ohio", "Florida"]
    abilities = ["strength", "superspeed", "invisibility", "flight"]


    def __init__(self, name, location, ability):
        self.name = name
        self.location = location
        self.ability = ability

    def SetBio(self, bio):
        if not isinstance(bio, str):
            print("That's not right")
            return
        self.bio = bio

    def GetBio(self):
        return self.bio

    def GetRandomWeapon(self, weapon):
        self.weapon = random.choice(list(Enemy.weapons.items()))

for i in range(5):
    name = Enemy.names[i]
    location = random.choice(Enemy.locations)
    abilities = random.choice(Enemy.abilities)
    newEnemy = Enemy(name, location, abilities)
    print("{} is from {} with the superpower of {}".format(name, location, abilities))

enemy1 = Enemy("Alear", "Engage", "Rally")
enemy1.SetBio("This character is cool")
#enemy1.GetRandomWeapon()
enemy2 = Enemy("Shez", "Fodlan", "Pulse")
#enemy2.SetBio("This character is epic")
#enemy2.GetRandomWeapon()
print(vars(enemy1))
print(vars(enemy2))

