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
        self.Player = Player()
    
    def on_start_click(self):
        app = App.get_running_app()
        print(app.root.children)
        self.Map.Load_Level()
        self.remove_widget(self.ids.Start)
        self.add_widget(self.Map)
    

class RRRApp(App):
    def build(self):
        return MainGameWidgets()




RRRApp().run()