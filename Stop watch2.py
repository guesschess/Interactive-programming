import simplegui

# global variables
a = 0 # minutes
b = 0 
c = 0 # seconds
d = 0 # tenth_second
total_count = 0
win_count = 0
started = False
time = 0
string = ""
# helper function
# the format of the clock 
def clock():
    global a,b,c,d,time,string
    a = time / 600
    b = (time % 600) / 100
    c = ((time % 600) % 100) / 10
    d = ((time % 600) % 100) % 10
    string = str(a) + ":" + str(b) + str(c) + ":" + str(d)
    return string

# check 
def check():
    global d, total_count, win_count
    if (d == 0):
        total_count += 1
        win_count += 1
    else:
        total_count += 1

# event handlers
def click():
    global time
    if started == True:
        time += 1
    return time

def start():
    global started
    if started == False:
        started = True
        click()
        timer.start()

def stop():
    global started
    if started == True:
        started = False
        timer.stop()
        
def reset():
    global started, time, total_count, win_count
    if started == True:
        started = False
        timer.stop()
        time = 0
        total_count = 0
        win_count = 0
        
# draw clock and score
def draw(canvas):
    global string
    canvas.draw_text(string, (200,200),20,"White")
    canvas.draw_text(str(win_count) + "/" + str(total_count), (100,100), 10, "White")
# create a frame
frame = simplegui.create_frame("Stop Watch", 450, 450)

# register handlers
timer = simplegui.create_timer(100, click)
button1 = frame.add_button("Start", start)
button2 = frame.add_button("Stop", stop)
button3 = frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# start
frame.start()
