import math
import simplegui      


n = 0

def algori(start):
    """Initializes n."""
    global n 
    n = start
    if n % 2 == 0:
        return n / 2
    else:
        return n * 3 + 1
# timer callback

def update():
    """???  Part of mystery computation."""
    # Stop iterating after max_iterations
    global n
    if n == 1:
        timer.stop()       
    else:
        n = algori(n)
    print n 

# register event handlers

timer = simplegui.create_timer(50, update)

# start program
algori(23)
timer.start()
