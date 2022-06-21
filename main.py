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
import os

# Builder.load_file("givemewings.kv")


# Define different screens
class MainWindow(Screen):
    start_sound = SoundLoader.load('game-start.mp3')
    click_sound = SoundLoader.load('click.mp3')
    bgm = SoundLoader.load('03-Meydan-Tired-of-life.mp3')
    game_start = False
    game_over = False

    def startSound(self):
        self.start_sound.play()

    def clickSound(self):
        self.click_sound.play()

    def start_game_pressed(self):
        os.system("python game.py")
        self.game_start = True

        if self.game_start == True:
            self.bgm.stop()
        # self.stop()
        # Window.close()

    def quit_pressed(self):
        Window.close()


class SettingsWindow(Screen):
    def clickSound(self):
        Sound = SoundLoader.load('click.mp3')
        Sound.play()


class InstructionWindow(Screen):
    def clickSound(self):
        Sound = SoundLoader.load('click.mp3')
        Sound.play()


class WindowManager(ScreenManager):
    pass


# Designate kv design file
kv = Builder.load_file('mainmenu.kv')


class MainMenu(App):
    # playing bgm
    def build(self):
        self.bgm = SoundLoader.load('magical_kid_124bpm_proud_music_preview.mp3')
        self.bgm.play()



        return kv

if __name__ == "__main__":
    MainMenu().run()