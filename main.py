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
from game import GiveMeWings
from game import Background
from game import Character

Builder.load_file("givemewings.kv")


# Define different screens
class MainWindow(Screen):
    on_game = False
    game_over = False

    menu_widget = ObjectProperty()

    def startSound(self):
        Sound = SoundLoader.load('game-start.mp3')
        Sound.play()

    def clickSound(self):
        Sound = SoundLoader.load('click.mp3')
        Sound.play()

    def on_touch_down(self, touch):
        return super(Screen, self).on_touch_down(touch)

    def start_game_pressed(self):
        self.on_game = True
        self.menu_widget.opacity = 0

class SettingsWindow(Screen):
    def clickSound(self):
        Sound = SoundLoader.load('click.mp3')
        Sound.play()

# class InstructionWindow(Screen):



class WindowManager(ScreenManager):
    pass


# Designate kv design file
kv = Builder.load_file('mainmenu.kv')


class MainMenu(App):
    # playing bgm
    def build(self):
        self.music = SoundLoader.load('03-Meydan-Tired-of-life.mp3')
        self.music.play()

        return kv

if __name__ == "__main__":
    MainMenu().run()