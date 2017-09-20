# for i in range(1, 20):
#     print("i is now {}".format(i))
#
number = "9,233,372,036,854,775,807"
cleanedNumber = '';
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

for char in number:
    if char in '0123456789':
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This is parrot is " + state)

for i in range(0, 100, 5):
    print("i is {}".format(i))
