import math
num_list = [1,2,3,4]          # Input
sum_ = 0                      # Initialize
prod = 1
for num in num_list:          # Apply
  sum_ = sum_ + num
  prod = prod * num                 # shorthand notation
print("sum: ", sum_)          # Use
print("prod: ", prod)
print("AM: ", sum_/len(num_list))
print("GM: ", math.pow(prod, 1/len(num_list)))