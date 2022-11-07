gameInv = []
text1 = """You begin in a grand forest with thick bushes and giant trees. You come across an apple tree.
 Would you like to clime the apple tree?"""

text2y = """ The tree begins to grumble and shake. The tree is not just any tree, but the wise old tree capable
of speaking and continues to ramble about uninteresting topics. Do you give the apple back?"""
print(text1)
treeClimb = input();
if treeClimb.lower() == "yes":
    print("You've obtained an apple.")
    gameInv.append("apple")

print(text2y)
appleTree = input()

if appleTree.lower() == "yes":
    print("The apple was lost.")
    gameInv.remove("apple")

word = "Python"
newWord = ""
for i in word:
    if i == "t":

        newWord = word.replace("t", "")

    print(newWord)
for i in word:
    if i != "t":
        newWord = i
print(newWord)

password = "lmao"
usrAttempt = 3

while usrAttempt > 0:
    userGuess = input("guess a password")
    if userGuess != password:
        usrAttempt -= 1
    if userGuess == password:
        print("Welcome!")
        break
else: print("You've been locked out")

numbers = [2, 3, 5, 7, 66, 89, 134]
print("Gimme a number")
userNum = int(input())
output= []

for i in numbers:
    if i < userNum:
        output.append(i)
print(output)

inventoryList = ["tentacle sweeper", "bomb", "sword"]

print("The winds howl and the sea trembles as the Tentacle Monster emerges to the surface")
choice = input("Choose your weapon!")

if choice in inventoryList and choice == "tentacle sweeper":
    print("The wicked monster flails its tentacles as they're swept away into the stratosphere")

elif choice in inventoryList and choice == "bomb": print("The monster swats the bombs back at you and completely wrecks your ship.")

elif choice in inventoryList and choice == "sword": print("YOu swing at the monster and it grabs your sword arm with its tentacles and tosses you into the sea.")

else: print("As you don't have that weapon, you curl your fists and prepare to attack. You don a mask and scream FALCON PUNCH! The monster never stood a chance")

sentence = "Hello world"
lChecker = int(0)
for i in sentence:
    if i == "l":
        lChecker += 1

print(lChecker)
