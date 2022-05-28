from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.clock import Clock
from random import randint
from pipe import Pipe
from kivy.properties import NumericProperty


class Background(Widget):
    # cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create textures
        # self.cloud_texture = Image(source="1838449.png").texture
        # self.cloud_texture.wrap = 'repeat'
        # self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

        self.floor_texture = Image(source="NicePng_minecraft-dirt-block-png_2255256.png").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width / self.floor_texture.width, -1)

    def on_size(self, *args):
        # self.cloud_texture.uvsize = (self.width / self.cloud_texture.width, -1)
        self.floor_texture.uvsize = (self.width / self.floor_texture.width, -1)

    def scroll_textures(self, time_passed):
        # Update the uvpos of the texture
        # self.cloud_texture.uvpos = ( (self.cloud_texture.uvpos[0] + time_passed)%Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ( (self.floor_texture.uvpos[0] + time_passed)%Window.width, self.floor_texture.uvpos[1])

        # Redraw the texture
        # texture = self.property('cloud_texture')
        # texture.dispatch(self)

        texture = self.property('floor_texture')
        texture.dispatch(self)

class Character(Image):
    velocity = NumericProperty(0)

    def on_touch_down(self, touch):
        self.source = "run1.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "jump1.png"
        super().on_touch_up(touch)


class GiveMeWings(App):
    pipes = []
    GRAVITY = 300

    def move_character(self, time_passed):
        character = self.root.ids.character
        character.y = character.y + character.velocity * time_passed
        character.velocity = character.velocity - self.GRAVITY * time_passed
        self.check_collision()

    def check_collision(self):
        character = self.root.ids.character
        # Go through each pipe and check if it collides
        for pipe in self.pipes:
            if pipe.collide_widget(character):
                self.game_over()

    def game_over(self):
        self.root.ids.character.pos = (70, ((self.root.height - 96) / 4 - 33))
        for pipe in self.pipes:
            self.root.remove_widget(pipe)
        self.frames.cancel()

    def next_frame(self, time_passed):
        self.move_character(time_passed)
        self.move_pipes(time_passed)
        self.root.ids.background.scroll_textures(time_passed)

    def on_start(self):
        self.pipes = []
        # Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)
        # Clock.schedule_interval(self.move_character, 1/60.)
        self.frames = Clock.schedule_interval(self.next_frame, 1/60.)

        # Create pipes
        num_pipes = 5
        distance_between_pipes = Window.width / (num_pipes - 1)
        for i in range(num_pipes):
            pipe = Pipe()
            pipe.pipe_center = randint(96 + 100, self.root.height - 100)
            pipe.size_hint = (None, None)
            pipe.pos = (Window.width + i*distance_between_pipes, 96)
            pipe.size = (64, self.root.height - 96)

            self.pipes.append(pipe)
            self.root.add_widget(pipe)

        # Move the pipes
        # Clock.schedule_interval(self.move_pipes, 1/60.)

    def move_pipes(self, time_passed):
        for pipe in self.pipes:
            pipe.x -= time_passed * 100
        # Check if we need to reposition the pipe on the right side
        num_pipes = 5
        distance_between_pipes = Window.width / (num_pipes - 1)

        pipe_xs = list(map(lambda pipe: pipe.x, self.pipes))
        right_most_x = max(pipe_xs)
        if right_most_x <= Window.width - distance_between_pipes:
            most_left_pipe = self.pipes[pipe_xs.index(min(pipe_xs))]
            most_left_pipe.x = Window.width



    pass



GiveMeWings().run()