from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
#Other files
from StartSceen import TitleScreenWidget,BrightnessLevel
from Player import Player
from Levels import MapWidget
#--------

Builder.load_file("titlescreen.kv")

class MainGameWidgets(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        pass
        

class RRRApp(App):
    def build(self):
        Brightness_Manager = BrightnessLevel()
        return MainGameWidgets()




RRRApp().run()