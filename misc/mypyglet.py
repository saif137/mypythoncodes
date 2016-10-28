import pyglet
from pyglet.window import key
from pyglet.window import mouse

textwindow = pyglet.window.Window()
imagewindow = pyglet.window.Window()
image = pyglet.resource.image('resources/pythonconcepts.png')

label = pyglet.text.Label("Hello to pyglet",
                          font_name='Times New Roman',
                          font_size=36,
                          x=textwindow.width//2, y=textwindow.height//2,
                          anchor_x='center', anchor_y='center')


#Requires AVBin to play mp3.
#Can be downloaded from: https://github.com/downloads/AVbin/AVbin/AVbin10-win32.exe
#or: https://github.com/downloads/AVbin/AVbin/AVbin10-win64.exe
pyglet.lib.load_library('resources/avbin')
pyglet.have_avbin=True
music = pyglet.resource.media("resources/snake_sound.mp3", streaming=False)

@textwindow.event
def on_draw():
    textwindow.clear()
    label.draw()

@textwindow.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        print "Enter pressed"
        music.play()
    else:
        print "Other key pressed"

@textwindow.event
def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
        print "Left button clicked on mouse at (" + str(x) + "," + str(y) + ")"
        music.play
    else:
        print "Other key pressed"


#Short sounds, such as a gunfire shot used in a game,
# should be decoded in memory before they are used,
# so that they play more immediately
# and incur less of a CPU performance penalty.
# Specify streaming=False in this case:

@imagewindow.event
def on_draw():
    imagewindow.clear()
    image.blit(0,0)


pyglet.app.run()