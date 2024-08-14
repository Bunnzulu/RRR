from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
#Other files
from StartSceen import TitleScreenWidget
from Player import Player
from Levels import MapWidget
#--------

Builder.load_file("titlescreen.kv")

class MainGameWidgets(RelativeLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Map = MapWidget()

    
    def on_start_click(self):
        self.Map.Load_Level()
        self.add_widget(self.Map)
        self.ids.Start.disabled = True
        

class RRRApp(App):
    def build(self):
        return MainGameWidgets()




RRRApp().run()