from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.clock import Clock


class Background(Widget):
    cloud_texture = ObjectProperty(None)

    def __int__(self, **kwargs):
        super().__init__(**kwargs)

        # Create Textures
        self.cloud_texture = Image(source="1838449.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

    def scroll_textures(self, time_passed):
        # Update the uvpos of the texture

        # Redraw the texture
        print("scroll")

    pass


class GiveMeWings(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/2.)
    pass


GiveMeWings().run()