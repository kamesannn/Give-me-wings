from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.clock import Clock
from random import randint


class Background(Widget):
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
        self.floor_texture.uvpos = ( (self.floor_texture.uvpos[0] + time_passed)%Window.width, self.floor_texture.uvpos[1])

        # Redraw the texture
        # texture = self.property('cloud_texture')
        # texture.dispatch(self)

        texture = self.property('floor_texture')
        texture.dispatch(self)


class GiveMeWings(App):
    rec = []

    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)

        num_rec = 5
        distance_between_rec = Window.width / (num_rec - 1)
        for i in range(num_rec):
            rec = Pipe()
            rec.rec_center = randint(70 + 100, self.root.height - 100)
            rec.rec_hint = (None, None)
            rec.pos = (Window.width + i*distance_between_rec, 70)
            rec.size = (70, self.root.height - 70)

            self.rec.append(rec)
            self.root.add_widget(rec)
    pass



GiveMeWings().run()