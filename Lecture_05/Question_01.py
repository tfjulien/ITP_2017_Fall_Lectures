# pseudo code
# 1.    get input
# 2.    iterate -for number in range(m, n+1)
#   3.1   check the conditions number % i == 0 and number % j != 0
#   3.2   add number to a list
# 4     output list of numbers

i = int(input("enter 'i'"))
j = int(input("enter 'j'"))
m = int(input("enter 'm'"))
n = int(input("enter 'n'"))

valid_numbers = []

for number in range(m, n+1):
    if number % i == 0 and number % j != 0:
        valid_numbers.append(str(number))
print(', '.join(valid_numbers))
