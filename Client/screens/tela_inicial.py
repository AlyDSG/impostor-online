from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from api import criar_sala, listar_jogadores, entrar_sala
from kivy.uix.label import Label
from kivy.app import App
from kivymd.uix.textfield import MDTextField


class TelaInicial(MDScreen):

    def entrar_sala_tela_inicial(self, instance):

        app = App.get_running_app()
        app.nick = self.campo_nick.text
        app.codigo_sala = self.campo_codigo.text
        

        if not app.nick.strip():
            print("Digite um nick!")
            return
        
        resultado = entrar_sala(app.codigo_sala, app.nick)
        if resultado["sucesso"] == True:
            self.manager.current = "lobby"
        else:
            print(resultado["erro"])

    def criar_sala_tela_inicial(self, instance):

        dados = criar_sala()

        app = App.get_running_app()
        app.codigo_sala = dados["codigo"]
        app.nick = self.campo_nick.text

        self.label_codigo.text = f"Sala: {dados['codigo']}"
        if not app.nick.strip():
            print("Digite um nick!")
            return
        
        resultado = entrar_sala(app.codigo_sala, app.nick)
        print(resultado)

        self.manager.current = "lobby"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20
        )

        self.campo_nick = MDTextField(
            hint_text="Seu nick"
        )
        self.campo_codigo = MDTextField(
            hint_text="Codigo da sala"
        )
        
        layout.add_widget(self.campo_codigo)
        layout.add_widget(self.campo_nick)


        botao = MDRaisedButton(
            text="Criar sala",
            size_hint=(1, None),
            height="50dp",
            on_release=self.criar_sala_tela_inicial
        )

        bota_entrada = MDRaisedButton(
            text="Entrar na sala",
            size_hint=(1, None),
            height="50dp",
            on_release=self.entrar_sala_tela_inicial
        )

        self.label_codigo = Label(
            text="Impostor Online",
            size_hint=(1, None),
            height="50dp",
            font_size="24sp",
            color=(0, 0, 0, 1)
        )

        layout.add_widget(botao)
        layout.add_widget(bota_entrada)
        layout.add_widget(self.label_codigo)

        self.add_widget(layout)