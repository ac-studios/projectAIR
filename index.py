# this file is all we should have to run to begin the game. it starts up the game.
import pyglet
from pyglet.window import key

window = pyglet.window.Window(fullscreen=True)

# intial setup

centerx, centery = window.get_size()[0] // 2, window.get_size()[1] // 2
topx, topy = window.get_size()[0], window.get_size()[1]

titleScreenImage = pyglet.resource.image("assets/ac-studios.png")

pyglet.font.load(name="monospace")

mouseLabel = pyglet.text.Label("", x=0, y=topy-24, font_size=18, font_name="monospace")

# event handlers

@window.event 
def on_draw():
    window.clear()
    titleScreenImage.blit(centerx -64, centery -64)
    mouseLabel.draw()

@window.event  
def on_key_press(symbol, mod):
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event  
def on_mouse_motion(x, y, dx, dy):
    mouseLabel.text = "[mouse x:"+str(x)+",y:"+str(y)+"] press esc to exit"

pyglet.app.run()