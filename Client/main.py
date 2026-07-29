from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.lobby import Lobby
from screens.tela_inicial import TelaInicial


class ImpostorApp(MDApp):
    
    codigo_sala = ""
    nick = ""


    def build(self):

        sm = ScreenManager()
        sm.add_widget(TelaInicial(name="tela_inicial"))
        sm.add_widget(Lobby(name="lobby"))

        return sm


ImpostorApp().run()