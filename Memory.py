# implementation of card game - Memory

import simplegui
import random

turns = 0
# Check the game's state

list1 = []
list2 = []
# the number of revealed cards
state = 0

# helper function to initialize globals
def new_game():
    global turns,started,list1,list2,state,exposed
    turns = 0
    state = 0
    list1 = [0,1,2,3,4,5,6,7]
    list2 = [0,1,2,3,4,5,6,7]
    # the concealded numbers 
    list1.extend(list2)
    # exposed cards
    exposed = [False for i in range(16)]
    # shuffle the cards
    label.set_text("Turns = "+ str(turns))
    return random.shuffle(list1)
 
# define event handlers
def mouseclick(pos):
    global turns, state, color,click1,click2
    index = int(pos[0]/50)
    if state == 0:
        click1 = index
        state =1
        exposed[click1] = True        
    elif state == 1:
        if exposed[index] == False:
            state =2
            click2 = index
            exposed[click2] = True
            turns +=1
    elif state == 2:
        if exposed[index] == False:
            # if two cards are unpaired
            if list1[click1] == list1[click2]:
                state = 0
            else:
                exposed[click1] = False
                exposed[click2] = False
                state = 1
                click1 = index
                exposed[click1] = True    
    label.set_text("Turns = " + str(turns))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list1
    # text behind the cards
    for a in range(0, 16):
        if exposed[a] == True:
            canvas.draw_text(str(list1[a]), (a*51,50), 50,"Red")
        else:
            canvas.draw_polygon([[a*50,0],[(a+1)*50,0],[(a+1)*50,100],[a*50,100]],
                                 .5,"Black","Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
