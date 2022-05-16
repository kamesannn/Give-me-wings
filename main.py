
from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('main.kv')

#class FloatLayout(FloatLayout):
#    pass
class MainLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        #Window.clearcolor = (1,0,0,1)
        return MainLayout()


if __name__ == '__main__':
    MyApp().run()