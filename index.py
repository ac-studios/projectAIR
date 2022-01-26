# this file is all we should have to run to begin the game. it starts up the game.
import pyglet
from pyglet.window import key

window = pyglet.window.Window(fullscreen=True)

label = pyglet.text.Label(text = "",font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event 
def on_draw():
    window.clear()
    label.draw()

@window.event  
def on_key_press(symbol, mod):
    label.text += chr(symbol)

pyglet.app.run()