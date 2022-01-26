# this file completely writes functions for outputting text, drawing images,
# etc...

from numpy import isin


class Image:
    def __init__(self, source, x, y, width, height):
        self.source = source
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = "renderer/image"

class TextBox:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = "renderer/textbox"

def append2(stack, arcade, instance, obj):
    # does some math and appends the correct
    # object with updated values to match
    if(isinstance(obj, TextBox)):
        # it is a textbox
        pass
    elif(isinstance(obj, Image)):
        # it is an image
        img = obj.source
        # the 1 here is scaling, ill implement those calculations later
        temp = arcade.Sprite(img, 1)
        # math to get the center coordinates
        temp.center_x = (obj.width / 2) + obj.x
        temp.center_y = obj.y - (obj.height / 2)
        stack.append(temp)
    else:
        # it is not a renderable type
        pass

def append2all(stack, arcade, instance):
    # calls append2 on all renderable objects in 
    # instance.stack
    for Object in instance.stack:
        append2(stack, arcade, instance, Object)

class RendererInstance:
    def __init__(self):
        self.stack = []
    def clear(self):
        self.stack = []
    def append(self, val):
        self.stack.append(val)

instance = RendererInstance()