from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.window import Window
from kivy.properties import Clock
from kivy.graphics.context_instructions import Color
# from kivy.uix.widget import Widget
#Other files
from StartSceen import TitleScreenWidget
from Player import Player
from Levels import MapWidget
from Pausemenu import PauseWidgets
#--------

Builder.load_file("titlescreen.kv")

class MainGameWidgets(RelativeLayout):
    Game_start = False
    PMenu = None
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Map = MapWidget()
        self.Old_Window_Size = [Window.width,Window.height]
        self.Player = Player()
        self.Pause = False
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)
        self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update,1/60)
        Window.bind(mouse_pos=self.Mouse_Motion)
    
    def on_start_click(self):
        self.clear_widgets()
        Builder.unload_file("titlescreen.kv")
        self.add_widget(self.Map)
        self.Old_Window_Size = [Window.width,Window.height]
        self.Map.Load_Level()
        self.Game_start = True
        self.Player.Borders = self.Map.Blocks
        self.Player_Spawn()
    
    def on_pause_back_click(self):
        self.Pause = False
        Builder.unload_file("PMenu.kv")
        self.remove_widget(self.PMenu)

    def Player_Spawn(self):
        with self.Map.canvas.after:
            self.Player.pos["x"] = self.Map.Spawnpoint[0]
            self.Player.pos["y"] = self.Map.Spawnpoint[1]
            self.Player.DrawnRect = Rectangle(pos=(self.Player.pos["x"],self.Player.pos["y"]),size=(self.Player.Width,self.Player.Height),texture=self.Player.Display_image)
    
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None

    def Mouse_Motion(self, window, pos):
        self.Player.mousepos = pos

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if self.Game_start:
            if keycode[1] == "p" and not self.Pause:
                self.Pause = True
                Builder.load_file("PMenu.kv")
                self.PMenu = PauseWidgets()
                self.add_widget(self.PMenu)
            if not self.Pause:
                self.Player.Input(keycode)
        return True

    def on_keyboard_up(self,keyboard,keycode):
        self.Player.Movement_Reset()
        return True

    def Borders(self):
        if (self.Player.pos["x"] < 0 or self.Player.pos["x"] > Window.width) or (self.Player.pos["y"] < 0 or self.Player.pos["y"] > Window.height):
            self.Player.Death = True
    
    def Death(self):
        if self.Player.Death:
            self.Player.pos["x"] = self.Map.Spawnpoint[0]
            self.Player.pos["y"] = self.Map.Spawnpoint[1]
            self.Redraw_Player()
            self.Player.Death = False

    def Redraw_Player(self):
        self.Map.canvas.after.children.remove(self.Player.DrawnRect)
        with self.Map.canvas.after:
            Color(1,1,1,1)
            self.Player.DrawnRect = Rectangle(pos=(self.Player.pos["x"],self.Player.pos["y"]),size=(self.Player.Width,self.Player.Height),texture=self.Player.Display_image)

    def Window_Change(self):
        if self.Map.Map and self.Map.Window_change:
            x_ratio = self.Player.pos["x"]/self.Old_Window_Size[0]
            y_ratio = self.Player.pos["y"]/self.Old_Window_Size[1]
            self.Player.pos["x"] = int(x_ratio*Window.width)
            self.Player.pos["y"] = int(y_ratio*Window.height)
            self.Player.Borders = self.Map.Blocks
            self.Map.Window_change = False
            self.Old_Window_Size = [Window.width,Window.height]

    def update(self,dt):
        if self.Game_start and not self.Pause:
            self.Player.update()
            self.Window_Change()
            self.Redraw_Player()
            self.Borders()
            self.Death()

class RRRApp(App):
    def build(self):
        return MainGameWidgets()




RRRApp().run()