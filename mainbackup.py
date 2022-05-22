from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

# Window.size = (1200, 800)


# Define different screens
class MainWindow(Screen):
    pass


class SettingsWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# Designate kv design file
kv = Builder.load_file('main.kv')


class GiveMeWingsApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    GiveMeWingsApp().run()
