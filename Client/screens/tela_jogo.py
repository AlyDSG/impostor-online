from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label


class TelaJogo(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            Label(
                text="JOGO",
                font_size=50
            )
        )