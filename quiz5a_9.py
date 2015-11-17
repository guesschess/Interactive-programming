import math
a = [0,1]
def add_list(n):
    sum = 0
    for i in range(n):
        sum = a[-1] + a[-2]
        a.append(sum)
    return sum

print add_list(10)
