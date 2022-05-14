from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image


class Background(Widget):
    cloud_texture = ObjectProperty(None)

    def __int__(self, **kwargs):
        super().__init__(**kwargs)

        # Create Textures
        self.cloud_texture = Image(source="1838449.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

    pass


class GiveMeWings(App):
    pass


GiveMeWings().run()