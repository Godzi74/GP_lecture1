import random

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

print(f_to_c(100))

def c_to_f(c_temp):
    f_temp = (c_temp * (9/5) + 32)
    return c_temp
print(c_to_f(0))

safe_code = []
while len(safe_code) < 3:
    code = random.randint(3, 12)
    if code not in safe_code:
        safe_code.append(code)


codes_cracked = 0

while codes_cracked < 3:
    for x in safe_code:
        print("The code is", x)
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if num2 == 1:
                raise ValueError("You can't pick one for the second number")
                break
            if num1 / num2 == x:
                print("Code cracked")
                ++ codes_cracked
        except ValueError:
            print("That is not a number")
            break
else:
    print("Safe opened")





letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letters_to_points = dict(zip(letters, points))
newList = []

name = input("What is your name?").upper()
score = 0

for letter in name:
    if letter in letters_to_points.keys() and letter not in newList:
        score = score + letters_to_points[letter]
        newList.append(letter)
print(score)