from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from api import criar_sala as criar_sala_api, listar_jogadores
from kivy.uix.label import Label
from kivy.app import App


class TelaInicial(MDScreen):
    
    def teste(self, instance):
        dados = criar_sala_api()
        app = App.get_running_app()
        app.codigo_sala = dados["codigo"]
        print(app.codigo_sala)
        self.label_codigo.text = f"Sala: {dados['codigo']}"
        self.manager.current = "lobby"
             
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20
        )

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
        self.add_widget(layout)
        layout.add_widget(self.label_codigo)