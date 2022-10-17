# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Benjamin")
print(19)
petName = "Bob"
petAge = 10

print(petName)
print(petAge)

tax = 1.14
amongUS = 12
eldenRing = 60
projectGrove = 20
price = 0
totalPrice = 0

price += (amongUS + eldenRing + projectGrove)

totalPrice += (price * tax)
print("Your new price is", totalPrice)
print("Your new price is $ %f"% totalPrice)

age = 12
height = 1.8743
name = "Ben"

##print("Your name is {}, your age is {} and you are {:.2f} tall".format(name, age, height))
##favNum = int(input("What's your favourite number?"))
##print(favNum)

userNum = int(input("Give me a number"))
if userNum <= 100:
    print("Wow that's a small number")
elif 100 < userNum <= 1000:
    print("That's not a big number yet")
else: print("That's a big number")

if userNum % 2 == 0:
    print("even")
else: print("odd")
#work please

