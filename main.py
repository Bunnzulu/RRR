from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.vertex_instructions import Rectangle
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
        self.clear_widgets()
        self.add_widget(self.Map)
        self.Map.Load_Level()
        self.Player_Spawn()
    
    def Player_Spawn(self):
        with self.Map.canvas.after:
            self.Player.pos["x"] = self.Map.Spawnpoint[0]
            self.Player.pos["y"] = self.Map.Spawnpoint[1]
            self.Player.DrawnRect = Rectangle(pos=(self.Player.pos["x"],self.Player.pos["y"]),size=(self.Player.Width,self.Player.Height),texture=self.Player.Display_image)

    def update(self):
        pass

class RRRApp(App):
    def build(self):
        return MainGameWidgets()




RRRApp().run()