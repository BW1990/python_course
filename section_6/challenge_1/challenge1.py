# Challenge Numero Uno
# Ask for name and age
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry

name = input("What is your name? ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday!")
else:
    print("I'm sorry, you cannot come on the holiday")
