
# get input from the user, we assume the input is always going to be a positive integer
n = int(input("Enter a positive integer: "))

# iterate over the rows, these go from 1 -> n
for row in range(1, n+1):
    # reset the line
    line = ''
    # iterate from 1 to the current row
    # this will result in the 3rd row having 3 elements
    for col in range(1, row+1):
        # add an int representing the position of the column
        line += str(col) + ' '
    # print this line now that there are the correct number of columns
    print(line)
