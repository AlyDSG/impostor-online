from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from api import criar_sala as criar_sala_api, listar_jogadores, entrar_sala
from kivy.uix.label import Label
from kivy.app import App
from kivymd.uix.textfield import MDTextField

class TelaInicial(MDScreen):
    
    def teste(self, instance):
        
        print("TESTE 1")
        print(self.campo_nick.text)

        dados = criar_sala_api()

        app = App.get_running_app()
        app.codigo_sala = dados["codigo"]
        app.nick = self.campo_nick.text

        print(app.codigo_sala)
        print(app.nick)

        self.label_codigo.text = f"Sala: {dados['codigo']}"
        self.manager.current = "lobby"
        resultado = entrar_sala(app.codigo_sala, app.nick)
        print(resultado)
                
        
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

        layout.add_widget(self.campo_nick)

        botao = MDRaisedButton(
            text="TESTE",
            size_hint=(1, None),
            height="50dp",
            on_release=self.teste
        )

        self.label_codigo = Label(
            text="TESTE LABEL",
            size_hint=(1, None),
            height="50dp",
            font_size="24sp",
            color=(0, 0, 0, 1)
        )

        layout.add_widget(botao)
        layout.add_widget(self.label_codigo)

        self.add_widget(layout)