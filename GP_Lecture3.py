import random

playerStats = {"health": 10, "atk": 5}

text1 = """You begin in a grand forest with thick bushes and giant trees. You come across an apple tree.
 Would you like to climb the apple tree?"""
print(text1)

text2 = """ The tree begins to grumble and shake. The tree is not just any tree, but the wise old tree capable
of speaking and claims he has been cursed by the wicked witch of the west, who needs to be defeated to restore the power
of eternal life back into its fruit. Do you accept this quest"""

yesApple = input()

if yesApple == "y":
    playerStats['health'] = 20
    print("""Your health has increased to {}""".format(playerStats['health']))
    print(text2)

else:
    print(text2)

questAccept = input()
if questAccept == "y":
    print("""---------Quest accepted----------""")

print("""The tree uses its branch to point into a direction deeper into the forest""")


tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14:
"Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19:
"The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

randomiser = {}
randomiser["first"] = random.choice(list(tarot.values()))
randomiser["second"] = random.choice(list(tarot.values()))
randomiser["third"] = random.choice(list(tarot.values()))

fortune = {}
fortune['past'] = randomiser.pop("first")
fortune['present'] = randomiser.pop("second")
fortune['future'] = randomiser.pop("third")

for key,val in fortune.items():
    print("Your", key, "is the", val, "card")

availableItems = {"health potion": 10, "cake": 5, "green elixir": 20, "lombas bread": 25, "bogweed": 15, "rabbit stew": 30}
healthPoints = 20
healthPoints = healthPoints + availableItems.pop('green elixir')
print(healthPoints)

animalsOnCampus = {}
animalsOnCampus['Foxes'] = 8
animalsOnCampus['Birds'] = 12
animalsOnCampus['Alligators'] = 0
print(animalsOnCampus)
animalsOnCampus['Foxes'] = 4
print(animalsOnCampus)

translations = {'mountain': 'blenon', 'bread': 'havon', 'friend': 'ragiros', 'horse': 'anne'}
print(translations['mountain'])


userList = []
newUserList = []

print("Gimme a list")
user = input()
userList = user.split()

for number in userList:
    if int(number) % 2 != 0:
        newUserList.append(number)
print(newUserList)