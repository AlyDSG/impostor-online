
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import Clock
from api import enviar_palavra_api, resultado_api


class TelaJogo(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical"
        )

        self.campo_palavra = MDTextField(
            hint_text="Digite uma palavra"
        )

        self.label_resultado = Label(
            text="",
            font_size="40sp",
            color=(1, 0, 0, 1),
            size_hint=(1, None),
            height="80dp"
        )

        layout.add_widget(self.campo_palavra)
        layout.add_widget(self.label_resultado)

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

        self.verificador = Clock.schedule_interval(
            self.verificar_resultado,
            1
        )

        if resultado["todos_enviaram"] == True:
            print("todos enviaram")
        else:
            print("falta jogadores")


    def verificar_resultado(self, intervalo):

        app = App.get_running_app()

        resultado = resultado_api(
            app.codigo_sala,
            app.nick
        )

        print("RESULTADO DA CONSULTA:", resultado)

        if resultado["sucesso"] == True:

            print("ENTROU NO IF")

            self.label_resultado.text = resultado["resultado"]

            Clock.unschedule(self.verificador)

