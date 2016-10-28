import pyglet
from pyglet.window import Window, mouse, gl

mygame = pyglet.window.Window(800,
                800
    ,
                resizable=False,
                caption="2048 Gaming"
    ,config=pyglet.gl.Config(double_buffer=True),
                vsync=False)
# set a background image (grid for this game)
bgimage = pyglet.image.load("resources/o.gif")
print(bgimage.height, bgimage.width)

# setting an icon for the image
myicon = pyglet.image.load('resources/ttticon.png')
mygame.set_icon(myicon)


# Display an image in the window
# bgimage = pyglet.image.load('resources/greebg.GIF')
# print (bgimage.height, bgimage.width)

# mygame.height= bgimage.height
# mygame.width= bgimage.width

# diff_height = (mygame.height/2)-(bgimage.height/2)
# diff_width = (mygame.width/2)-(bgimage.width/2)
# print (diff_height, diff_width)

@mygame.event
def on_draw():
    mygame.clear()
    bgimage.blit(0, 0)


def update(dt):
    on_draw()


# Handle mouse input
@mygame.event
def on_mouse_press(x, y, button, modifiers):
    width_box = bgimage.width / 3
    height_box = bgimage.height / 3
    print(width_box, height_box)

    if button == mouse.LEFT:
        print("Mouse left clicked at ", x, y)
        if (x < width_box and y < height_box):
            print("Mouse Left clicked in box 7")
        if (x < (2 * width_box) and x > width_box and y < height_box):
            print("Mouse Left clicked in box 8")
        if (x < (3 * width_box) and x > (2 * width_box) and y < height_box):
            print("Mouse Left clicked in box 9")
        if (x < width_box and y > height_box and y < (2 * height_box)):
            print("Mouse Left clicked in box 4")
        if (x > width_box and x < (2 * width_box) and y > height_box and y < (2 * height_box)):
            print("Mouse Left clicked in box 5")
        if (x > (2 * width_box) and x < (3 * width_box) and y > height_box and y < (2 * height_box)):
            print("Mouse Left clicked in box 6")
        if (x < width_box and y > (2 * height_box) and y < (3 * height_box)):
            print("Mouse Left clicked in box 1")
        if (x > width_box and x < (2 * width_box) and y > (2 * height_box) and y < (3 * height_box)):
            print("Mouse Left clicked in box 2")
        if (x > (2 * width_box) and x < (3 * width_box) and y > (2 * height_box) and y < (3 * height_box)):
            print("Mouse Left clicked in box 3")
        if x in [width_box, (2 * width_box), (3 * width_box)] and y in [height_box, (2 * height_box), (3 * height_box)]:
            print("Mouse clicked on line")


# Set window update function and frequency.
pyglet.clock.schedule_interval(update, 1 / 60)

# launches the application window.
pyglet.app.run()
