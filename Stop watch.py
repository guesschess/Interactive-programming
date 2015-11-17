Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
# template for "Stopwatch: The Game"
import simplegui
import math
# define global variables
a = 0
b = 0
c = 0
d = 0
started = False
total_count = 0 
win_count = 0
count = 0
canvas_height = 200
canvas_width = 200

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# screen timer's time format
def format(t):
    global a, b, c, d
    # minute:a, second:bc, tenth_sec:d
    a = t / 600
    b = (t % 600) / 100
    c = ((t % 600) % 100) / 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global started
    timer.start()
    started = True

def stop():
    global started, count, total_count, win_count
    if started:
        if count % 10 == 0 and count != 0:
            total_count +=1
            win_count +=1 
        elif count != 0:
            total_count +=1
    started = False
    timer.stop()
         
def restart():
    global started, count, total_count, win_count
    started = False
    count = 0
    total_count = 0
    win_count = 0
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count +=1

# define draw handler
def draw_handler(canvas):
    global count, canvas_width, canvas_height
    text = format(count)
    canvas.draw_text(text, (canvas_width/4, canvas_height /4), 12, "black")
    canvas.draw_text(str(win_count) + "/" + str(total_count), 
                     (canvas_width * 3/4, canvas_height /4), 12, "black")    
    
# create frame
frame = simplegui.create_frame("Stop Watch", canvas_width, canvas_height)
frame.set_canvas_background('white')

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Restart", restart, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

