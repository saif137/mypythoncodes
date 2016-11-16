'''
Procedural TIC TAC TOE implementation using pyglet on Python
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''

import pyglet
from pyglet.window import Window, mouse, gl

mygame = Window(800, 600,
              resizable=False,  # Make sure it is not resizable
              caption="Bluetooth RC Car Control",  # Caption of window
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False  # For flicker-free animation
              )  # Calling base class constructor

# Background image use for game
bgimage = pyglet.resource.image('resources/bImage1.png')

# Get an instance of current platform
platform = pyglet.window.get_platform()
# Get an instance of current display
display = platform.get_default_display()
# Get an instance of current screen
screen = display.get_default_screen()
# Make sure that game approximately is placed as center of screen
# This will adjust for different resolution. Relative positioning
# Using resolution to center game window
mygame.set_location(screen.width // 2 - 400, screen.height // 2 - 300)
# image for icon of game window
myicon = pyglet.image.load('resources/bluetoothIcon.jpg')
# Setting icon for game window
mygame.set_icon(myicon)  # setting icon


up_image = pyglet.resource.image("resources/up.png")
down_image = pyglet.resource.image("resources/down.png")
left_image = pyglet.resource.image("resources/left.png")
right_image = pyglet.resource.image("resources/right.png")
up_left_image = pyglet.resource.image("resources/up_left.png")
up_right_image = pyglet.resource.image("resources/up_right.png")
down_left_image = pyglet.resource.image("resources/down_left.png")
down_right_image = pyglet.resource.image("resources/down_right.png")
stop_image = pyglet.resource.image("resources/stop.png")

up_image_active = pyglet.resource.image("resources/up_active.png")
down_image_active = pyglet.resource.image("resources/down_active.png")
left_image_active = pyglet.resource.image("resources/left_active.png")
right_image_active = pyglet.resource.image("resources/right_active.png")
up_left_image_active = pyglet.resource.image("resources/up_left_active.png")
up_right_image_active = pyglet.resource.image("resources/up_right_active.png")
down_left_image_active = pyglet.resource.image("resources/down_left_active.png")
down_right_image_active = pyglet.resource.image("resources/down_right_active.png")
stop_image_active = pyglet.resource.image("resources/stop_active.png")


##--------------------------------------------------------------------------##


up = pyglet.sprite.Sprite(up_image, 375, 280)
up.visible = True

down = pyglet.sprite.Sprite(down_image, 375, 140)
down.visible = True

left = pyglet.sprite.Sprite(left_image, 305, 210)
left.visible = True

right = pyglet.sprite.Sprite(right_image, 445, 210)
right.visible = True

up_left = pyglet.sprite.Sprite(up_left_image, 305, 280)
up_left.visible = True

up_right = pyglet.sprite.Sprite(up_right_image, 445, 280)
up_right.visible = True

down_left = pyglet.sprite.Sprite(down_left_image, 305, 140)
down_left.visible = True

down_right = pyglet.sprite.Sprite(down_right_image, 445, 140)
down_right.visible = True

stop = pyglet.sprite.Sprite(stop_image, 375, 210)
stop.visible = True


up_active = pyglet.sprite.Sprite(up_image_active, 375, 280)
up_active.visible = False

down_active = pyglet.sprite.Sprite(down_image_active, 375, 140)
down_active.visible = False

left_active = pyglet.sprite.Sprite(left_image_active, 305, 210)
left_active.visible = False

right_active = pyglet.sprite.Sprite(right_image_active, 445, 210)
right_active.visible = False

up_left_active = pyglet.sprite.Sprite(up_left_image_active, 305, 280)
up_left_active.visible = False

up_right_active = pyglet.sprite.Sprite(up_right_image_active, 445, 280)
up_right_active.visible = False

down_left_active = pyglet.sprite.Sprite(down_left_image_active, 305, 140)
down_left_active.visible = False

down_right_active = pyglet.sprite.Sprite(down_right_image_active, 445, 140)
down_right_active.visible = False

stop_active = pyglet.sprite.Sprite(stop_image_active, 375, 210)
stop_active.visible = False

    
##--------------------------------------------------------------------------##

@mygame.event
def on_draw():              
    mygame.clear()              
    bgimage.blit(0, 0)
    
    up.draw()
    down.draw()
    left.draw()
    right.draw()
    up_left.draw()
    up_right.draw()
    down_left.draw()
    down_right.draw()
    stop.draw()

    up_active.draw()
    down_active.draw()
    left_active.draw()
    right_active.draw()
    up_left_active.draw()
    up_right_active.draw()
    down_left_active.draw()
    down_right_active.draw()
    stop_active.draw()
    


# This function handles mouse events

@mygame.event
def on_mouse_press(x, y, button, modifiers):                                
    # Check if left mouse button i clicked                                  
    if button == mouse.LEFT:                                                
        # printing coordinates on console
        print ("Left button clicked on mouse at (" + str(x) + "," + str(y) + ")")
##        if win == 1:
##            return;  # game over
        if (x >= 375 and x < 425) and (y >= 280 and y <= 330):
            print("up")
            up_image.visible = False
            up_image_active.visible = True
            on_draw()

        elif (x >= 375 and x <= 425) and (y >= 140 and y <= 190):
            print("down")
            down_image.visible = False
            down_image_active.visible = True
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 210 and y <= 260):
            print("left")
            left_image.visible = False
            left_image_active.visible = True
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 210 and y <= 260):
            print("right")
            right_image.visible = False
            right_image_active.visible = True
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 280 and y <= 330):
            print("up_left")
            up_left.visible = False
            up_left_active.visible = True
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 280 and y <= 330):
            print("up_right")
            up_right_image.visible = False
            up_right_image_active.visible = True
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 140 and y <= 190):
            print("down_left")
            down_left_image.visible = False
            down_left_image_active.visible = True
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 140 and y <= 190):
            print("down_right")
            down_right_image.visible = False
            down_right_image_active.visible = True
            on_draw()
 
        elif (x >= 375 and x <= 425) and (y >= 210 and y <= 260):
            print("stop")
            stop_image.visible = False
            stop_image_active.visible = True
            on_draw()

    else:
        print ("Other mouse key pressed")



@mygame.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("\nrelease\n")
        up.visible = True
        down.visible = True
        left.visible = True
        right.visible = True
        up_left.visible = True
        up_right.visible = True
        down_left.visible = True
        down_right.visible = True
        stop.visible = True

        up_active.visible = False
        down_active.visible = False
        left_active.visible = False
        right_active.visible = False
        up_left_active.visible = False
        up_right_active.visible = False
        down_left_active.visible = False
        down_right_active.visible = False
        stop_active.visible = False

def update(dt):
    on_draw()

#def update(self, dt):
#    on_draw()


pyglet.clock.schedule_interval(update, 1 / 60.)

pyglet.app.run()
