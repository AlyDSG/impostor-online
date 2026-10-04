from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.lobby import Lobby
from screens.tela_inicial import TelaInicial
from screens.tela_jogo import TelaJogo


class ImpostorApp(MDApp):
    
    codigo_sala = ""
    nick = ""


    def build(self):

        sm = ScreenManager()
        sm.add_widget(TelaInicial(name="tela_inicial"))
        sm.add_widget(Lobby(name="lobby"))
        sm.add_widget(TelaJogo(name="jogo"))


        return sm


ImpostorApp().run()