from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from api import listar_jogadores
from kivy.clock import Clock
from kivymd.uix.button import MDRaisedButton

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

        botao_sair = MDRaisedButton(
            text="SAIR DO LOBBY",
            on_release=self.sair_lobby
        )

        layout.add_widget(botao_sair)

        

    def on_enter(self):
        app = App.get_running_app()

        jogadores = listar_jogadores(app.codigo_sala)

        nomes = ""

        for jogador in jogadores["jogadores"]:
            nomes += jogador["nick"] + "\n"

        self.texto.text = f"LOBBY: {app.codigo_sala}\n\nJOGADORES:\n{nomes}"
        self.timer_jogadores = Clock.schedule_interval(
            self.atualizar_jogadores,
            1
        )
    def atualizar_jogadores(self, intervalo):
        app = App.get_running_app()

        jogadores = listar_jogadores(app.codigo_sala)

        nomes = ""

        for jogador in jogadores["jogadores"]:
            nomes += jogador["nick"] + "\n"

        self.texto.text = f"LOBBY: {app.codigo_sala}\n\nJOGADORES:\n{nomes}"

    def on_leave(self):
        Clock.unschedule(self.timer_jogadores)

    def sair_lobby(self, instance):
                self.manager.current = "tela_inicial"