n = int(input("Enter a positive integer: "))

# keep track of how many numbers there are
count = 1

for row in range(n, 0, -1):
    line = ''
    for col in range(1, row+1):
        # add the current number to the line
        line += str(count) + ' '
        # add 1 to the count for the next position
        count += 1
    print(line)

# solution with formatting
# there are many ways to do this

count = 1

# this is the formula to calculate triangle numbers
greatest_int = n * (n+1) // 2
# knowing how many characters there are in the largest numbers is required to calculate the offset
number_of_characters = len(str(greatest_int))

for row in range(n, 0, -1):
    line = ''
    for col in range(1, row+1):
        # this will offset the numbers to ensure that they are right aligned
        line += '{:>{}} '.format(count, number_of_characters)
        count += 1
    print(line)