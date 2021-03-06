
# get input from the user, we assume the input is always going to be a positive integer
n = int(input("Enter a positive integer: "))

# iterate over the rows, these go from n -> 1
for row in range(n, 0, -1):
    # clear the previous line
    line = ''
    # iterate from 1 to the current row
    # this will result in the 3rd row having 3 elements
    for col in range(1, row+1):
        # add an '*' for each column
        line += '* '
    # print this line now that we have the correct number of columns
    print(line)
