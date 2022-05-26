from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch


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
        
        self.music = SoundLoader.load('03-Meydan-Tired-of-life.mp3')
        self.music.play()

        # self.music.volume(kv.on_value())
        def EffectVal(self, value):
            self._volume(value)

        def _volume(self, vol):
            print('_volume')
            vol = round(vol)
            vol_value = vol / 100

            # self.volume_text.text = str(vol)
            self.volume_bar.value = vol

            if not self.music:
                return

            self.music.volume = vol_value



        return kv


if __name__ == "__main__":
    GiveMeWingsApp().run()
