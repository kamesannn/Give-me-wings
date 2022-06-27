from kivy.core.window import Window
from kivy.uix.widget import Widget
import game
import os


class GameOverWindow(Widget):  # Game over window
    # if not game over then hide window
    def show_window(self):
        self.opacity = 0

        if (game.GiveMeWings().state_game_over == True):
            self.opacity = 1

    # def restart_game(self):
    #     Window.close()
    #     os.system("python game.py")
    #
    # def back_to_main(self):
    #     Window.close()
    #     os.system("python main.py")
    #