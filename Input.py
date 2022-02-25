
""" 
name1 = input("Enter your name: ")
age1 = input("Enter your age: ")
print("Oh I see. You are " + age1 + " years old. Welcome, " + name1 + "! I hope you are doing good.")

# Function using Strings
def welcome_message(name, age):
    print("Hello " + name + "! Welcome to my python welcome message, hehe. And you are " + age + " years old. cool!")

welcome_message(name = input("Enter your name: "), age = input("Enter your age: "))

# Function using Numbers
def cube(num):
    return num*num*num

result = cube(float(input("Enter the number you want to cube and it will go to result_var: ")))
print(result)
print(cube(float(input("Enter the number you want to cube: "))))

"""
# If statement

i_am_here = True
i_am_alive = False

"""
if i_am_here and i_am_alive:
    print("You exist. You are here!")
    print("Oh thank God, you are alive!")
    name = input("Tell me, what is your name?: ")
    print("Welcome back, " + str(name) + "!")
else:
    print("Where are you?")
    print(input("Answer me, are still there: "))

if i_am_here and i_am_alive:
    print("You exist and you are alive!")
elif i_am_here and not(i_am_alive):
    print("You exist but " + str(place = input("Where are you?: ")))
    print("Oh, okay. You are in " + place + ".")
else:
    print(input("Where are you?"))
    print(input("Answer me, are still there: "))


# if statement and comparisons

def min_num(num1, num2, num3, num4):
    if num1 <= num2 and num1 <=num3 and num1 <= num4:
        return num1
    elif num2 <= num1 and num2 <=num3 and num2 <= num4:
        return num2
    elif num3 <= num1 and num3 <=num2 and num3 <= num4:
        return num3
    else:
        return num4


print(min_num(111,23,3,4))



# Calculator and Operator

num1 = float(input("Enter your first number: "))
oper = input("Enter your operator: ")
num2 = float(input("Enter your second numer: "))

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
else:
    print("Invalid operator")


# Dictionary 

amino_acidConversion = {
    "Ala": "Alanine",
    "Arg": "Arginine",
    "Asn": "Asparagine",
    "Asp": "Aspartic acid",
    "Cys": "Cysteine",
    "Glu": "Glutamic acid",
    "Gln": "Glutamine",
    "Gly": "Glycine",
    "His": "His",
    "Ile": "Isoleucine",
    "Leu": "Leucine",
    "Lys": "Lysine",
    "Met": "Methionine",
    "Phe": "Phenylalanine",
    "Pro": "Proline",
    "Ser": "Serine",
    "Thr": "Threonine",
    "Trp": "Tryptophan",
    "Tyr": "Tyrosine",
    "Val": "Valine",
}

print(amino_acidConversion.get("Ler", "Not a valid amino acid abbreviation."))

# While Loop

i = int(input("Enter a number: "))
while i <= 10:
    print(i)
    i += 3
print("While looping done")



# Guessing Game

secret_word = "alcohol"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter your guess word: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess == True:
    print("Better luck next time.")
else:
    print("You guessed the word. Congratulation!")



# For Loop

for letter in "Isopropyl":
    print(letter)

amino_acids = ["Tyrosine", "Alanine", "Glutamine", "Phenylalanine"]
for amino_acid in amino_acids:
    print(amino_acid + " is an example of amino acid.")

for index in range(4, 11):
    print(index)

print("")

for index in range(len(amino_acids)):
    print(str(index) + ". "+ str(amino_acids[index]))



# Exponent Function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(int(input("Enter the base number: ")), int(input("Enter the exponenet: "))))



# 2 Dimensional List and Nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in number_grid:
    for column in row:
        print(column)



# Building a Translator
# Building a DNA complement generator


def base_complement_translator(base_sequence):
    complement = ""
    for base in base_sequence:
        if base.upper() in "A":
            complement = complement + "T"
        elif base.upper() in "T":
            complement = complement + "A"
        elif base.upper() in "G":
            complement = complement + "C"
        elif base.upper() in "C":
            complement = complement + "G"
        else:
            complement = complement + "-"
    return complement

query_base_sequence = input("Enter a base sequence: ")

print("")
print("Query base sequence:             " + query_base_sequence.upper())
bar = ""
for base in query_base_sequence:
    if base.upper() in "ATGC":
        bar = bar + "|"
    else:
        bar = bar + " "
print("                                 " + bar)
print("Complement of the base sequence: " + base_complement_translator(query_base_sequence))



# Try Except Block

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

# Reading Files

employee_file = open("employees.txt", "r")

for phrase in employee_file.readlines():
    print(phrase)
    
employee_file.close()





# Writing a File

text_file = open("employees2.txt", "w")

text_file.write("\n" + input("Enter a new phrase: "))

text_file = open("employees.txt", "r")
print(text_file.readlines()[-1])




# Try and Except Block

try:
    dividend = int(input("Enter a dividend: "))
    divisor = int(input("Enter a divisor: "))
    quotient = dividend/divisor
    print(quotient)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("A number is cannot be divided by zero")

"""

# Writing a File

phrases = open("employees3.txt", "w")
number = 0
while number in range(100):
    number += 1
    phrases.write("\n" + str(number) + ". Hello, All Purpose Keeper.")


python_file = open("this_is_a_python.py", "w")
python_file.write("print('Hello')")

