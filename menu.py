from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.core.window import Window
from pipe import Pipe
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.properties import NumericProperty
from kivy.clock import Clock
from random import randint
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget




# Define different screens
class MainWindow(Screen):
    def startSound(self):
        Sound = SoundLoader.load('game-start.mp3')
        Sound.play()
    def clickSound(self):
        Sound = SoundLoader.load('click.mp3')
        Sound.play()

class SettingsWindow(Screen):
    def clickSound(self):
        Sound = SoundLoader.load('click.mp3')
        Sound.play()

class GameWindow(Screen):

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
        self.floor_texture.uvpos = (
        (self.floor_texture.uvpos[0] + time_passed) % Window.width, self.floor_texture.uvpos[1])

        # Redraw the texture
        # texture = self.property('cloud_texture')
        # texture.dispatch(self)

        texture = self.property('floor_texture')
        texture.dispatch(self)


class Character(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    velocity = NumericProperty(0)

    # def character_image(self, time_passed):
    #     if time_passed % 2 == 0:
    #         self.source = "run1.png"
    #     else:
    #         self.source = "run2.png"

    def _on_key_down(self,keyboard,keycode,text,modifiers):
        if text == "w":
            self.source = "jump1.png"
            self.velocity = 150
        if text == "s":
            self.source = "slide.png"
            self.velocity = -100


# Designate kv design file
# kv = Builder.load_file("menu.kv")


class GiveMeApp(App):
    # playing bgm
    pipes = []
    GRAVITY = 300
    music = SoundLoader.load('Ultraman Nexus OST - Heroic - Extended (320 kbps).mp3')
    was_colliding = False


    def build(self):
        self.music.play()

    def move_character(self, time_passed):
        character = self.root.ids.character
        character.y = character.y + character.velocity * time_passed
        character.velocity = character.velocity - self.GRAVITY * time_passed
        self.check_collision()

    def check_collision(self):
        character = self.root.ids.character
        # Go through each pipe and check if it collides
        is_colliding = False
        for pipe in self.pipes:
            if pipe.collide_widget(character):
                is_colliding = True
                # Check if character is between the gap
                if character.y < (pipe.pipe_center - pipe.GAP_SIZE / 2.0):
                    self.game_over()
                if character.top > (pipe.pipe_center + pipe.GAP_SIZE / 2.0):
                    self.game_over()
        # if character.y < 96:
        #     self.game_over()
        if character.top > Window.height:
            self.game_over()

        if self.was_colliding and not is_colliding:
            self.root.ids.score.text = str(int(self.root.ids.score.text) + 1)
        self.was_colliding = is_colliding

    def game_over(self):
        self.root.ids.character.pos = (70, ((self.root.height - 96) / 4 - 33))
        for pipe in self.pipes:
            self.root.remove_widget(pipe)
        self.frames.cancel()
        self.music.stop()

    def next_frame(self, time_passed):
        self.move_character(time_passed)
        self.move_pipes(time_passed)
        self.root.ids.GameWindow.scroll_textures(time_passed)

    def on_start(self):
        # self.root.ids.score.text = "0"
        self.was_colliding = False
        self.pipes = []
        # Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)
        # Clock.schedule_interval(self.move_character, 1/60.)
        self.frames = Clock.schedule_interval(self.next_frame, 1 / 60.)

        # Create pipes
        num_pipes = 200
        distance_between_pipes = Window.width / 3
        for i in range(num_pipes):
            pipe = Pipe()
            # pipe.pipe_center = randint(96 + 100, self.root.height - 100)
            pipe.size_hint = (None, None)
            pipe.pos = (Window.width + i * distance_between_pipes, 96)
            pipe.size = (64, self.root.height - 96)

            self.pipes.append(pipe)
            self.root.add_widget(pipe)

        # Move the pipes
        # Clock.schedule_interval(self.move_pipes, 1/60.)

    def move_pipes(self, time_passed):
        for pipe in self.pipes:
            pipe.x -= time_passed * 100
        # Check if we need to reposition the pipe on the right side
        distance_between_pipes = Window.width / 3

        pipe_xs = list(map(lambda pipe: pipe.x, self.pipes))
        right_most_x = max(pipe_xs)
        if right_most_x <= Window.width - distance_between_pipes:
            most_left_pipe = self.pipes[pipe_xs.index(min(pipe_xs))]
            most_left_pipe.x = Window.width

        return ScreenManager()


# if __name__ == "__main__":
GiveMeApp().run()