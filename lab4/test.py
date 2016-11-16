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

pyglet.app.run()