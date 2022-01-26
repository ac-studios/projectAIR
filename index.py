# this file is all we should have to run to begin the game. it starts up the game.
import arcade
from engine.renderer import append2, append2all, RendererInstance

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.window_commands.get_display_size()
SCREEN_TITLE = "projectAIR"

# main window
class projectAIR(arcade.Window):
    def __init__(self, width, height, title):
        # enable fullscreen and builtins from arcade
        super().__init__(width, height, title, fullscreen=True)

        # set background color to white
        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

        # here is the instance for the renderer we need
        self._instance = RendererInstance()

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.sprites = arcade.SpriteList()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self._instance.clear()

        append2all(self.sprites, arcade, self._instance)

        self.sprites.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    # create an instance of the main class
    game = projectAIR(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # begin setup
    game.setup()
    # run it
    arcade.run()


if __name__ == "__main__":
    # execute
    main()