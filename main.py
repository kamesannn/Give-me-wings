import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.core.window import Window

Builder.load_file('main.kv')

class MainLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        #Window.clearcolor = (1,0,0,1)
        return MainLayout()


if __name__ == '__main__':
    MyApp().run()