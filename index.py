import pyglet
from pyglet.window.key import *


window = pyglet.window.Window(fullscreen=True)

pyglet.font.add_file('assets/fonts/static/Uni.ttf')
uni = pyglet.font.load('Uni', 48)
topx,topy=window.get_size()[0],window.get_size()[1]
txt_label = pyglet.text.Label('AC Studios Presents', anchor_x='center', anchor_y='center', x = topx//2, y = topy//2, font_size=48, font_name='Uni')
pause = False
background = (0,0,0)
@window.event
def on_draw():
    pyglet.gl.glClearColor(*background, 1)
    window.clear()

    txt_label.draw()
pyglet.app.run()

