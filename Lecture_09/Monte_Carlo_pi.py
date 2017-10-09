#         area of circle    pi*r^2     pi*r^2
# ratio = -------------- = -------- = --------
#         area of square    (2r)^2      4r^2


#            pi
# ratio =   ---
#            4

# 4 * ratio = pi
import random


def in_circle(x, y, r):
    return x ** 2 + y ** 2 <= r ** 2


count_in_circle = 0

for iteration in range(1, 10000000):
    x = (random.random() * 2) - 1
    y = (random.random() * 2) - 1

    if in_circle(x, y, 1):
        count_in_circle += 1
    print((count_in_circle / iteration) * 4)
