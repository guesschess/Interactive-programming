import simplegui

# global variables
a = 5

#define event handlers
def keydown(key):
    global a
    a = a * 2
    print a 

def keyup(key):
    global a
    a = a - 3
    print a

# register handlers
frame = simplegui.create_frame("Testing", 100, 100)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start
frame.start()
