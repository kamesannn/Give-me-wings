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
import os



# Define different screens
class MainWindow(Screen):
    start_sound = SoundLoader.load('game-start.mp3')
    click_soundeffect = SoundLoader.load('click.mp3')
    bgm = SoundLoader.load('magical_kid_124bpm_proud_music_preview.mp3')

    def start_click_sound(self):
        self.start_sound.play()

    def start_game_pressed(self):
        os.system("python game.py")
        GiveMeWings().state_game_start = True
        Window.close()
        self.bgm.stop()

    def quit_pressed(self):
        Window.close()

    def click_sound(self):
        self.click_soundeffect.play()


class SettingsWindow(Screen):
    click_soundeffect = SoundLoader.load('click.mp3')

    def click_sound(self):
        self.click_soundeffect.play()


class InstructionWindow(Screen):
    click_soundeffect = SoundLoader.load('click.mp3')

    def click_sound(self):
        self.click_soundeffect.play()


class WindowManager(ScreenManager):
    pass


# Designate kv design file
kv = Builder.load_file('mainmenu.kv')


class MainMenu(App):
    bgm = SoundLoader.load('magical_kid_124bpm_proud_music_preview.mp3')

    # playing bgm
    def build(self):
        self.bgm.play()

        return kv


if __name__ == "__main__":
    MainMenu().run()