from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text="Name: ", font_size=32))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.enter = Button(text="Enter", font_size=32)

        self.enter.bind(on_press=self.press)
        self.add_widget(self.enter)

    def press(self, instance):
        name = self.name.text
        print(f"Hello {name}!!")


class MyApp(App):
    def build(self):
        self.title = "window"
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()