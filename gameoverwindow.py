from kivy.uix.widget import Widget
import game


class GameOverWindow(Widget):
    def update_score(self):
        self.ids.score.text = game.GiveMeWings().game_over_score()



