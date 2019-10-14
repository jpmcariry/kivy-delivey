from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import FadeTransition

class Tela1(Screen, object):
    def funcao(self):
        print("dentro da funcao")
    def verificar(self):
        if(self.ids.login.text=="test" and self.ids.senha.text=="test"):
            self.manager.current="Tela2"
        else:
            print("login e senha incorretos")
    def mudar_btn(self):
        self.ids.btn.back_color=""
        print("deve ter muado")


class Tela2(Screen, object):
    pass

class Window(ScreenManager, object):
    pass

arquivo_kv = Builder.load_file("programa.kv")
screenmanager = Window()
screenmanager.add_widget(Tela1())

class ProgramaApp(App):
    def build(self):
        return arquivo_kv

ProgramaApp().run()