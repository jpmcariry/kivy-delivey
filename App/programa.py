from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen



arquivo_kv = Builder.load_file("kivy_lang.kv")

class ProgramaApp(App):
    def build(self):
        return arquivo_kv

ProgramaApp().run()
