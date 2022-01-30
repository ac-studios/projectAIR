# this file is all we should have to run to begin the game. it starts up the game.
import pyglet
from pyglet.window import key
import math
#hello
window = pyglet.window.Window(fullscreen=True)

# intial setup

centerx, centery = window.get_size()[0] // 2, window.get_size()[1] // 2
topx, topy = window.get_size()[0], window.get_size()[1]

titleScreenImage = pyglet.resource.image("assets/ac-studios.png")

pyglet.font.add_file("assets/fonts/static/RobotoMono-Light.ttf")
fontRobotoMono = pyglet.font.load(name="Roboto Mono Light")

mouseLabel = pyglet.text.Label("", x=0, y=topy-24, font_size=18, font_name="Roboto Mono Light")
fpsLabel = pyglet.text.Label("", x=0, y=topy-52, font_size=18, font_name="Roboto Mono Light")

centerlinex = pyglet.shapes.Line(0, centery, topx, centery)
centerliney = pyglet.shapes.Line(centerx, topy, centerx, 0)

debug = False

# event handlers

@window.event 
def on_draw():
    window.clear()
    titleScreenImage.blit(centerx, centery)
    if(debug == True):
        mouseLabel.draw()
        centerlinex.draw()
        centerliney.draw()
        fpsLabel.text = "[fps:"+str(math.floor(pyglet.clock.get_fps()))+"]"
        fpsLabel.draw()  

@window.event  
def on_key_press(symbol, mod):
    if symbol == key.ESCAPE:
        pyglet.app.exit()
    if symbol == key.F3:
        global debug
        debug = not(debug)

@window.event  
def on_mouse_motion(x, y, dx, dy):
    mouseLabel.text = "[mouse x:"+str(x)+",y:"+str(y)+"] f3->debug esc->exit"

pyglet.app.run()