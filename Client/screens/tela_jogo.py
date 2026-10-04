from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from api import enviar_palavra_api
from kivymd.uix.button import MDRaisedButton
from kivy.app import App

class TelaJogo(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical"
        )

        self.campo_palavra = MDTextField(
        hint_text="Digite uma palavra"
    )
        layout.add_widget(self.campo_palavra)
        
        botao_enviar = MDRaisedButton(
            text="ENVIAR",
            on_release=self.enviar_palavra
        )
        layout.add_widget(botao_enviar)
        self.add_widget(layout)


    def enviar_palavra(self, instance):
        app = App.get_running_app()

        resultado = enviar_palavra_api(
            app.codigo_sala,
            app.nick,
            self.campo_palavra.text
        )

        print(resultado)

        if resultado["todos_enviaram"] == True:
            print("todos enviaram")
        else:
            print("falta jogadores")                