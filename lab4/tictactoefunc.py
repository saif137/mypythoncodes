'''
Procedural TIC TAC TOE implementation using pyglet on Python
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''

import pyglet
from pyglet.window import Window, mouse, gl

mygame = Window(400, 300,
              resizable=False,  # Make sure it is not resizable
              caption="Tic Tac Toe",  # Caption of window
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False  # For flicker-free animation
              )  # Calling base class constructor

# Background image use for game
bgimage = pyglet.resource.image('resources/greebg.GIF')

# Get an instance of current platform
platform = pyglet.window.get_platform()
# Get an instance of current display
display = platform.get_default_display()
# Get an instance of current screen
screen = display.get_default_screen()
# Make sure that game approximately is placed as center of screen
# This will adjust for different resolution. Relative positioning
# Using resolution to center game window
mygame.set_location(screen.width // 2 - 200, screen.height // 2 - 150)
# image for icon of game window
myicon = pyglet.image.load('resources/ttticon.png')
# Setting icon for game window
mygame.set_icon(myicon)  # setting icon

# Images for cross and O
cimage = pyglet.resource.image("resources/cross.gif")
oimage = pyglet.resource.image("resources/o.gif")
# Sprites for each position
csprite1 = pyglet.sprite.Sprite(cimage, 20, 210)
csprite1.visible = False
csprite2 = pyglet.sprite.Sprite(cimage, 150, 210)
csprite2.visible = False
csprite3 = pyglet.sprite.Sprite(cimage, 285, 210)
csprite3.visible = False
csprite4 = pyglet.sprite.Sprite(cimage, 20, 110)
csprite4.visible = False
csprite5 = pyglet.sprite.Sprite(cimage, 150, 110)
csprite5.visible = False
csprite6 = pyglet.sprite.Sprite(cimage, 285, 110)
csprite6.visible = False
csprite7 = pyglet.sprite.Sprite(cimage, 20, 10)
csprite7.visible = False
csprite8 = pyglet.sprite.Sprite(cimage, 150, 10)
csprite8.visible = False
csprite9 = pyglet.sprite.Sprite(cimage, 285, 10)
csprite9.visible = False

osprite1 = pyglet.sprite.Sprite(oimage, 20, 210)
osprite1.visible = False
osprite2 = pyglet.sprite.Sprite(oimage, 150, 210)
osprite2.visible = False
osprite3 = pyglet.sprite.Sprite(oimage, 285, 210)
osprite3.visible = False
osprite4 = pyglet.sprite.Sprite(oimage, 20, 110)
osprite4.visible = False
osprite5 = pyglet.sprite.Sprite(oimage, 150, 110)
osprite5.visible = False
osprite6 = pyglet.sprite.Sprite(oimage, 285, 110)
osprite6.visible = False
osprite7 = pyglet.sprite.Sprite(oimage, 20, 10)
osprite7.visible = False
osprite8 = pyglet.sprite.Sprite(oimage, 150, 10)
osprite8.visible = False
osprite9 = pyglet.sprite.Sprite(oimage, 285, 10)
osprite9.visible = False

# Turn identifier, 0 means O, 1 means X
move = 0  # means o
# Holds moves for each of 9 boxes
moves = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
# To differentiate between win and draw
win = 0
# Label for win notification
winlabel = pyglet.text.Label("",
                             font_name='Times New Roman',
                             font_size=24,
                             x=190, y=175,
                             anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))

def update(self, dt):
    on_draw()

# To swap the turn on each move
def mymove():
    global move
    if move == 0:
        move = 1
    else:
        move = 0


# To check for win or a draw
def checkwin():
    global win
    if moves[0] == moves[1] == moves[2] or \
                            moves[3] == moves[4] == moves[5] or \
                            moves[6] == moves[7] == moves[8] or \
                            moves[0] == moves[3] == moves[6] or \
                            moves[1] == moves[4] == moves[7] or \
                            moves[2] == moves[5] == moves[8] or \
                            moves[0] == moves[4] == moves[8] or \
                            moves[2] == moves[4] == moves[6]:
        print("Win")
        win = 1
        winlabel.text = "Player : " + str(move) + " is the winner"
    else:
        for element in moves:
            if element <= -1:
                return
        win = 1
        winlabel.text = "Game is a draw"

@mygame.event
def on_draw():
    mygame.clear()
    bgimage.blit(0, 0)
    csprite1.draw()
    csprite2.draw()
    csprite3.draw()
    csprite4.draw()
    csprite5.draw()
    csprite6.draw()
    csprite7.draw()
    csprite8.draw()
    csprite9.draw()
    osprite1.draw()
    osprite2.draw()
    osprite3.draw()
    osprite4.draw()
    osprite5.draw()
    osprite6.draw()
    osprite7.draw()
    osprite8.draw()
    osprite9.draw()
    winlabel.draw()


# This function handles mouse events
@mygame.event
def on_mouse_press(x, y, button, modifiers):
    # Check if left mouse button i clicked
    if button == mouse.LEFT:
        # printing coordinates on console
        print "Left button clicked on mouse at (" + str(x) + "," + str(y) + ")"
        if win == 1:
            return;  # game over
        if (x >= 0 and x < 130) and (y >= 200 and y <= 300):
            print("1")
            if moves[0] > -1:
                return;  # move already made
            mymove()  # Make move to change player
            moves[0] = move  # Set the move to history list
            if move == 0:  # Show the move according to player
                osprite1.visible = True
            else:
                csprite1.visible = True
        elif (x >= 130 and x < 265) and (y >= 200 and y <= 300):
            print("2")
            if moves[1] > -1:
                return;  # move already made
            mymove()  # Make move to change player
            moves[1] = move  # Set the move to history list
            if move == 0:  # Show the move according to player
                osprite2.visible = True
            else:
                csprite2.visible = True
        elif (x >= 265 and x <= 400) and (y >= 200 and y <= 300):
            print("3")
            if moves[2] > -1:
                return;  # move already made
            mymove()
            moves[2] = move
            if move == 0:  # Show the move according to player
                osprite3.visible = True
            else:
                csprite3.visible = True
        elif (x >= 0 and x < 130) and (y >= 100 and y < 200):
            print("4")
            if moves[3] > -1:
                return;  # move already made
            mymove()
            moves[3] = move
            if move == 0:  # Show the move according to player
                osprite4.visible = True
            else:
                csprite4.visible = True
        elif (x >= 130 and x < 265) and (y >= 100 and y < 200):
            print("5")
            if moves[4] > -1:
                return;  # move already made
            mymove()
            moves[4] = move
            if move == 0:  # Show the move according to player
                osprite5.visible = True
            else:
                csprite5.visible = True
        elif (x >= 265 and x <= 400) and (y >= 100 and y < 200):
            print("6")
            if moves[5] > -1:
                return;  # move already made
            mymove()
            moves[5] = move
            if move == 0:  # Show the move according to player
                osprite6.visible = True
            else:
                csprite6.visible = True
        elif (x >= 0 and x < 130) and (y >= 0 and y < 100):
            print("7")
            if moves[6] > -1:
                return;  # move already made
            mymove()
            moves[6] = move
            if move == 0:  # Show the move according to player
                osprite7.visible = True
            else:
                csprite7.visible = True
        elif (x >= 130 and x < 265) and (y >= 0 and y < 100):
            print("8")
            if moves[7] > -1:
                return;  # move already made
            mymove()
            moves[7] = move
            if move == 0:  # Show the move according to player
                osprite8.visible = True
            else:
                csprite8.visible = True
        elif (x >= 265 and x <= 400) and (y >= 0 and y < 100):
            print("9")
            if moves[8] > -1:
                return;  # move already made
            mymove()
            moves[8] = move
            if move == 0:  # Show the move according to player
                osprite9.visible = True
            else:
                csprite9.visible = True
        else:
            print ("out of screen")
    else:
        print "Other mouse key pressed"

    #Check for win
    checkwin()

def update(dt):
    on_draw()

pyglet.clock.schedule_interval(update, 1 / 60.)

pyglet.app.run()