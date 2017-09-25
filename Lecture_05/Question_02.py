print('\ncontinue statement')
numbers = [1, 3, 5, 6, 9, 10]
for number in numbers:
    if number % 2 == 0:
        break
    print(number)
print('finished')