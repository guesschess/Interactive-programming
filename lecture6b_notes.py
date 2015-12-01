# vedio lecture 6b: Tips 
# exmample 1
class ball:
    # tips1: the init method often return the object that has been created
    # so you do not need to return anything in init method
    def __init__(self,pos,rad):
        self.position = pos
        self.radius = rad
        
        
    def get_position(self):
        return self.position

b = ball([0,0], 5)
print b.get_position()

# example 2
# while loop
def countdown(n):
    # print a count down from n to 0
    i = n
    while i >= 0:
        print i
        i -= 1

# for loop
def countdown(n):
    i = n
    for i in range(n, -1,-1):
        print i

# the difference between while and for loop is
# the wihle loop return the single number, while
# the for loop create a list


# example 3
def collatz(n):
    # prints the numbers in the Collatz sequence for n.
    while n >1:
        if (n % 2) == 0:
            n = n /2
            print n
            
        else:
            n = n * 3 + 1
            print n

collatz(10)
## Tips: if appears "TimeLimitError" on the screen, it might be some logic erros in 
## the program
