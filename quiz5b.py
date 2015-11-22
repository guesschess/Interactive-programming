# Question 7
my_list = [1,2,3,4,5,6,7]
def is_even(number):
    """Returns whether the number is even."""
    return number % 2 == 0
print [is_even(number) for number in my_list]


# Question 9
import simplegui

frame_size = [300, 300]
image_size = [100,100 ]

def draw(canvas):
    canvas.draw_image(image, [220, 100], image_size,
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")

frame.start()
