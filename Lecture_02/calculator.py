value_1 = input("Enter the first value: ")
operator = input("Enter the operator: ")
value_2 = input("Enter the second value: ")

values_valid = True
if value_1.isdigit() and value_2.isdigit():
    value_1 = int(value_1)
    value_2 = int(value_2)
else:
    print("At least one of the values is not an integer")
    values_valid = False

valid_operator = True
if operator not in '+-*/':
    print("Operator is not valid")
    valid_operator = False

if valid_operator and values_valid:
    if operator == '+':
        print(value_1, '+', value_2, '=', value_1 + value_2)
    elif operator == '-':
        print(value_1, '-', value_2, '=', value_1 - value_2)
    elif operator == '*':
        print(value_1, '*', value_2, '=', value_1 * value_2)
    elif operator == '/':
        print(value_1, '/', value_2, '=', value_1 / value_2)

