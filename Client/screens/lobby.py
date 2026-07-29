from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App


class Lobby(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical"
        )

        self.texto = Label(
            text="LOBBY",
            color=(0,0,0,1),
            font_size=50
        )

        layout.add_widget(self.texto)
        self.add_widget(layout)


    def on_enter(self):
        app = App.get_running_app()
        self.texto.text = f"LOBBY: {app.codigo_sala}"