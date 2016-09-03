'''
Object oriented TIC TAC TOE implementation using pyglet on Python
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''

import pyglet
from pyglet.window import key, mouse, gl


class mytictactoe(pyglet.window.Window):  # inheriting Window class

    # Background image use for game
    bgimage = pyglet.resource.image('resources/greebg.GIF')
    # Images for cross and O
    cimage = pyglet.resource.image("resources/cross.gif")
    oimage = pyglet.resource.image("resources/o.gif")
    #Sprites for each position
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

    #Turn identifier, 0 means O, 1 means X
    move = 0 # means o
    #Holds moves for each of 9 boxes
    moves = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
    #To differentiate between win and draw
    win = 0
    #Label for win notification
    winlabel = pyglet.text.Label("",
                                 font_name='Times New Roman',
                                 font_size=24,
                                 x=190, y=175,
                                 anchor_x='center', anchor_y='center',color=(0,0,0,255))

    def __init__(self):
        super(mytictactoe, self).__init__(400, 300,
                                          resizable=False,  # Make sure it is not resizable
                                          caption="Tic Tac Toe",  # Caption of window
                                          config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
                                          vsync=False  # For flicker-free animation
                                          )  # Calling base class constructor
        # Get an instance of current platform
        platform = pyglet.window.get_platform()
        # Get an instance of current display
        display = platform.get_default_display()
        # Get an instance of current screen
        screen = display.get_default_screen()
        # Make sure that game approximately is placed as center of screen
        # This will adjust for different resolution. Relative positioning
        # Using resolution to center game window
        self.set_location(screen.width // 2 - 200, screen.height // 2 - 150)
        # image for icon of game window
        myicon = pyglet.image.load('resources/ttticon.png')
        # Setting icon for game window
        self.set_icon(myicon)  # setting icon

    # This function handles mouse events
    def on_mouse_press(self, x, y, button, modifiers):
        # Check if left mouse button i clicked
        if button == mouse.LEFT:
            # printing coordinates on console
            print "Left button clicked on mouse at (" + str(x) + "," + str(y) + ")"
            if self.win == 1:
                return; # game over
            if (x >= 0 and x < 130) and (y >= 200 and y <= 300):
                print("1")
                if self.moves[0] > -1:
                    return; # move already made
                self.mymove() # Make move to change player
                self.moves[0] = self.move # Set the move to history list
                if self.move == 0 : # Show the move according to player
                    self.osprite1.visible = True
                else:
                    self.csprite1.visible = True
            elif (x >= 130 and x < 265) and (y >= 200 and y <= 300):
                print("2")
                if self.moves[1] > -1:
                    return; # move already made
                self.mymove()# Make move to change player
                self.moves[1] = self.move# Set the move to history list
                if self.move == 0 :# Show the move according to player
                    self.osprite2.visible = True
                else:
                    self.csprite2.visible = True
            elif (x >= 265 and x <= 400) and (y >= 200 and y <= 300):
                print("3")
                if self.moves[2] > -1:
                    return; # move already made
                self.mymove()
                self.moves[2] = self.move
                if self.move == 0 :# Show the move according to player
                    self.osprite3.visible = True
                else:
                    self.csprite3.visible = True
            elif (x >= 0 and x < 130) and (y >= 100 and y < 200):
                print("4")
                if self.moves[3] > -1:
                    return; # move already made
                self.mymove()
                self.moves[3] = self.move
                if self.move == 0 :# Show the move according to player
                    self.osprite4.visible = True
                else:
                    self.csprite4.visible = True
            elif (x >= 130 and x < 265) and (y >= 100 and y < 200):
                print("5")
                if self.moves[4] > -1:
                    return; # move already made
                self.mymove()
                self.moves[4] = self.move
                if self.move == 0 :# Show the move according to player
                    self.osprite5.visible = True
                else:
                    self.csprite5.visible = True
            elif (x >= 265 and x <= 400) and (y >= 100 and y < 200):
                print("6")
                if self.moves[5] > -1:
                    return; # move already made
                self.mymove()
                self.moves[5] = self.move
                if self.move == 0 :# Show the move according to player
                    self.osprite6.visible = True
                else:
                    self.csprite6.visible = True
            elif (x >= 0 and x < 130) and (y >= 0 and y < 100):
                print("7")
                if self.moves[6] > -1:
                    return; # move already made
                self.mymove()
                self.moves[6] = self.move
                if self.move == 0 :# Show the move according to player
                    self.osprite7.visible = True
                else:
                    self.csprite7.visible = True
            elif (x >= 130 and x < 265) and (y >= 0 and y < 100):
                print("8")
                if self.moves[7] > -1:
                    return; # move already made
                self.mymove()
                self.moves[7] = self.move
                if self.move == 0 :# Show the move according to player
                    self.osprite8.visible = True
                else:
                    self.csprite8.visible = True
            elif (x >= 265 and x <= 400) and (y >= 0 and y < 100):
                print("9")
                if self.moves[8] > -1:
                    return; # move already made
                self.mymove()
                self.moves[8] = self.move
                if self.move == 0 :# Show the move according to player
                    self.osprite9.visible = True
                else:
                    self.csprite9.visible = True
            else:
                print ("out of screen")
        else:
            print "Other mouse key pressed"

        #Check for win
        self.checkwin()

    def on_draw(self):
        self.clear()
        self.bgimage.blit(0, 0)
        self.csprite1.draw()
        self.csprite2.draw()
        self.csprite3.draw()
        self.csprite4.draw()
        self.csprite5.draw()
        self.csprite6.draw()
        self.csprite7.draw()
        self.csprite8.draw()
        self.csprite9.draw()
        self.osprite1.draw()
        self.osprite2.draw()
        self.osprite3.draw()
        self.osprite4.draw()
        self.osprite5.draw()
        self.osprite6.draw()
        self.osprite7.draw()
        self.osprite8.draw()
        self.osprite9.draw()
        self.winlabel.draw()

    def update(self, dt):
        self.on_draw()

    # To swap the turn on each move
    def mymove(self):
        if mytictactoe.move == 0:
            mytictactoe.move = 1
        else:
            mytictactoe.move = 0

    #To check for win or a draw
    def checkwin(self):
        if self.moves[0] == self.moves[1] == self.moves[2] or\
           self.moves[3] == self.moves[4] == self.moves[5] or\
           self.moves[6] == self.moves[7] == self.moves[8] or\
           self.moves[0] == self.moves[3] == self.moves[6] or\
           self.moves[1] == self.moves[4] == self.moves[7] or\
           self.moves[2] == self.moves[5] == self.moves[8] or\
           self.moves[0] == self.moves[4] == self.moves[8] or\
           self.moves[2] == self.moves[4] == self.moves[6] :
            print("Win")
            self.win = 1
            self.winlabel.text = "Player : " + str(self.move) + " is the winner"
        else:
            for element in self.moves:
                if element <= -1 :
                    return
            self.win = 1
            self.winlabel.text = "Game is a draw"

if __name__ == "__main__":
    mygame = mytictactoe()  # Instantiate tictactoc game class
    pyglet.clock.schedule_interval(mygame.update, 1 / 60.)
    pyglet.app.run()
