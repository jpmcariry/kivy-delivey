from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import WindowBase
from kivy.uix.button import Button
from kivy.graphics import Canvas
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import io
from kivy.core.image import Image as CoreImage
data = io.BytesIO(open("src\\img\\ifood-logo.png", "rb").read())
im = CoreImage(data, ext="png")

import sys
import os


class Programa(Screen, object):
    x = NumericProperty(0)
    y = NumericProperty(0)
    size_btn_out = ReferenceListProperty(x, y)
    def logar(self):
        print(self.ids.login.text)
        print(self.ids.senha.text)
        if (self.ids.login.text == "test" and self.ids.senha.text == "test"):
            {"login":self.ids.login.text,"senha":self.ids.senha.text}
            self.manager.current = "crud"
        else:
            print("senha ou login errados")


class Crud(Screen, object):

    def crud_print(self):
        print("dentro da tela crud!!")


class Pesquisa(Screen, object):

    def pesquisar(self):
        print("dentro da tela !")


class WindowManager(ScreenManager, object):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(Programa())
kv_file = Builder.load_file("main.kv")


class Editor(App):
    def build(self):
        return kv_file


if __name__ == '__main__':
    Editor().run()
