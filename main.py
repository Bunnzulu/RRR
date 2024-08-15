from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.window import Window
from kivy.properties import Clock
# from kivy.uix.widget import Widget
#Other files
from StartSceen import TitleScreenWidget
from Player import Player
from Levels import MapWidget
#--------

Builder.load_file("titlescreen.kv")

class MainGameWidgets(RelativeLayout):
    Game_start = False
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Map = MapWidget()
        self.Player = Player()
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)
        self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update,1/60)
    
    def on_start_click(self):
        self.clear_widgets()
        self.add_widget(self.Map)
        self.Map.Load_Level()
        self.Game_start = True
        self.Player_Spawn()
    
    def Player_Spawn(self):
        with self.Map.canvas.after:
            self.Player.pos["x"] = self.Map.Spawnpoint[0]
            self.Player.pos["y"] = self.Map.Spawnpoint[1]
            self.Player.DrawnRect = Rectangle(pos=(self.Player.pos["x"],self.Player.pos["y"]),size=(self.Player.Width,self.Player.Height),texture=self.Player.Display_image)
    
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.Player.Input(keycode[1])
        return True

    def on_keyboard_up(self,keyboard,keycode):
        self.Player.Movement_Reset()
        return True

    def Redraw_Player(self):
        self.Map.canvas.after.children.remove(self.Player.DrawnRect)
        with self.Map.canvas.after:
            self.Player.DrawnRect = Rectangle(pos=(self.Player.pos["x"],self.Player.pos["y"]),size=(self.Player.Width,self.Player.Height),texture=self.Player.Display_image)

    def update(self,dt):
        if self.Game_start:
            self.Player.update()
            self.Redraw_Player()

class RRRApp(App):
    def build(self):
        return MainGameWidgets()




RRRApp().run()