'''
Procedural TIC TAC TOE implementation using pyglet on Python
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''

import pyglet, sched
from pyglet.window import Window, mouse, gl, key


lista = []
check = 0
startTime = 0


def listOut(lista):
    for i in lista:
        print(i[0]+"--------"+str(i[1]))

def print_event(name):
    print ('EVENT:', time.time(), name)

def schedule(lista):
    s = sched.scheduler(time.time, time.sleep)
    count = 1
    for i in lista:
        s.enter(i[1], count, print_event, (i[0],))
        count = count + 1
    print("Replay Started"+"\n")
    s.run()
    print("\n"+"Replay Ended")

import time

def recorder(event):
    global lista
    global check
    global startTime

    if check == 1:
       lista.append((event,time.time()-startTime))




mygame = Window(800, 600,
              resizable=False,  # Make sure it is not resizable
              caption="Bluetooth RC Car Control",  # Caption of window
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False  # For flicker-free animation
              )  # Calling base class constructor
mygame.set_exclusive_keyboard()

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
stop_image = pyglet.resource.image("resources/stop.jpg")
record_image = pyglet.resource.image("resources/record.png")
replay_image = pyglet.resource.image("resources/replay.png")

up_image_active = pyglet.resource.image("resources/up_active.png")
down_image_active = pyglet.resource.image("resources/down_active.png")
left_image_active = pyglet.resource.image("resources/left_active.png")
right_image_active = pyglet.resource.image("resources/right_active.png")
up_left_image_active = pyglet.resource.image("resources/up_left_active.png")
up_right_image_active = pyglet.resource.image("resources/up_right_active.png")
down_left_image_active = pyglet.resource.image("resources/down_left_active.png")
down_right_image_active = pyglet.resource.image("resources/down_right_active.png")
stop_image_active = pyglet.resource.image("resources/stop_active.jpg")
record_image_active = pyglet.resource.image("resources/record_active.png")


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

record = pyglet.sprite.Sprite(record_image, 305, 80)
record.visible = True

replay = pyglet.sprite.Sprite(replay_image, 305, 20)
replay.visible = True


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

record_active = pyglet.sprite.Sprite(record_image_active, 305, 80)
record_active.visible = False

    
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
    record.draw()
    replay.draw()

    up_active.draw()
    down_active.draw()
    left_active.draw()
    right_active.draw()
    up_left_active.draw()
    up_right_active.draw()
    down_left_active.draw()
    down_right_active.draw()
    stop_active.draw()
    record_active.draw()
    
##--------------------------------------------------------------------------##

# This function handles mouse events

@mygame.event
def on_mouse_press(x, y, button, modifiers):                                

    global lista
    global check
    global startTime
                                     
    if button == mouse.LEFT:                                                
        # printing coordinates on console
        print ("Left button clicked on mouse at (" + str(x) + "," + str(y) + ")")
##        if win == 1:
##            return;  # game over
        if (x >= 375 and x < 425) and (y >= 280 and y <= 330):
            print("up pressed")
            recorder("Up-press")
            up.visible = False
            up_active.visible = True
            on_draw()

        elif (x >= 375 and x <= 425) and (y >= 140 and y <= 190):
            print("down pressed")
            recorder("Down-press")
            down.visible = False
            down_active.visible = True
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 210 and y <= 260):
            print("left pressed")
            recorder("Left-press")
            left.visible = False
            left_active.visible = True
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 210 and y <= 260):
            print("right pressed")
            recorder("Right-press")
            right.visible = False
            right_active.visible = True
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 280 and y <= 330):
            print("up_left pressed")
            recorder("Up-press")
            recorder("Left-press")
            up_left.visible = False
            up_left_active.visible = True
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 280 and y <= 330):
            print("up_right pressed")
            recorder("Up-press")
            recorder("Right-press")            
            up_right.visible = False
            up_right_active.visible = True
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 140 and y <= 190):
            print("down_left pressed")
            recorder("Down-press")
            recorder("Left-press") 
            down_left.visible = False
            down_left_active.visible = True
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 140 and y <= 190):
            print("down_right pressed")
            recorder("Down-press")
            recorder("Right-press")
            down_right.visible = False
            down_right_active.visible = True
            on_draw()
 
        elif (x >= 375 and x <= 425) and (y >= 210 and y <= 260):
            print("stop pressed")
            stop.visible = False
            stop_active.visible = True
            on_draw()
            
        elif (x >= 305 and x <= 495) and (y >= 80 and y <= 120):
            if record.visible == True:
                print("recording on")
                record.visible = False
                record_active.visible = True
                on_draw()
                check = 1
                startTime = time.time()
                lista = []
            else:
                print("recording stop")
                record.visible = True
                record_active.visible = False
                on_draw()
                check = 0
                
        elif (x >= 305 and x <= 495) and (y >= 20 and y <= 60):
            if lista == None:
                print("No record")
            else:
                listOut(lista)
                schedule(lista)
        

    else:
        print ("Other mouse key pressed")

##--------------------------------------------------------------------------##

@mygame.event
def on_mouse_release(x, y, button, modifiers):

    global lista
    global check
    global startTime
    
    if button == mouse.LEFT:
        print ("Left button released on mouse at (" + str(x) + "," + str(y) + ")")
##        if win == 1:
##            return;  # game over
        if (x >= 375 and x < 425) and (y >= 280 and y <= 330):
            print("up released")
            recorder("Up-release")
            up.visible = True
            up_active.visible = False
            on_draw()

        elif (x >= 375 and x <= 425) and (y >= 140 and y <= 190):
            print("down released")
            recorder("Down-release")
            down.visible = True
            down_active.visible = False
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 210 and y <= 260):
            print("left released")
            recorder("Left-release")
            left.visible = True
            left_active.visible = False
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 210 and y <= 260):
            print("right released")
            recorder("Right-release")
            right.visible = True
            right_active.visible = False
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 280 and y <= 330):
            print("up_left released")
            recorder("Up-release")
            recorder("Left-release") 
            up_left.visible = True
            up_left_active.visible = False
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 280 and y <= 330):
            print("up_right released")
            recorder("Up-release")
            recorder("Right-release")
            up_right.visible = True
            up_right_active.visible = False
            on_draw()

        elif (x >= 305 and x <= 355) and (y >= 140 and y <= 190):
            print("down_left released")
            recorder("Down-release")
            recorder("Left-release")
            down_left.visible = True
            down_left_active.visible = False
            on_draw()

        elif (x >= 445 and x <= 495) and (y >= 140 and y <= 190):
            print("down_right released")
            recorder("Down-release")
            recorder("Right-release")
            down_right.visible = True
            down_right_active.visible = False
            on_draw()
 
        elif (x >= 375 and x <= 425) and (y >= 210 and y <= 260):
            print("stop released")
            stop.visible = True
            stop_active.visible = False
            on_draw()

            
##--------------------------------------------------------------------------##


@mygame.event
def on_key_press(symbol, modifiers):
    global lista
    global check
    global startTime

    if symbol == key.UP:
        print("Up key pressed")
        recorder("Up-press")
        up.visible = False
        up_active.visible = True
        on_draw()
    elif symbol == key.DOWN:
        print("Down key pressed")
        recorder("Down-press")
        down.visible = False
        down_active.visible = True
        on_draw()
    elif symbol == key.LEFT:
        print("Left key pressed")
        recorder("Left-press")
        left.visible = False
        left_active.visible = True
        on_draw()
    elif symbol == key.RIGHT:
        print("Right key pressed")
        recorder("Right-press")
        right.visible = False
        right_active.visible = True
        on_draw()
    elif symbol == key.SPACE:
        print("space pressed")
        if record.visible == True:
            print("recording on")
            record.visible = False
            record_active.visible = True
            on_draw()
            check = 1
            startTime = time.time()
            lista = []
        else:
            print("recording stop")
            record.visible = True
            record_active.visible = False
            on_draw()
            check = 0
    elif symbol == key.R:
        print("R pressed")
        if lista == None:
            print("No record")
        else:
            listOut(lista)
            schedule(lista)


##--------------------------------------------------------------------------##


@mygame.event
def on_key_release(symbol, modifiers):

    global lista
    global check
    global startTime

    if symbol == key.UP:
        print("Up key released")
        recorder("Up-release")
        up.visible = True
        up_active.visible = False
        on_draw()
    elif symbol == key.DOWN:
        print("Down key released")
        recorder("Down-release")
        down.visible = True
        down_active.visible = False
        on_draw()
    elif symbol == key.LEFT:
        print("Left key pressed")
        recorder("Left-release")
        left.visible = True
        left_active.visible = False
        on_draw()
    elif symbol == key.RIGHT:
        print("Right key pressed")
        recorder("Right-release")
        right.visible = True
        right_active.visible = False
        on_draw()


##--------------------------------------------------------------------------##
        

def update(dt):
    on_draw()

pyglet.clock.schedule_interval(update, 1 / 60.)

pyglet.app.run()
