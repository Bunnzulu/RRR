from kivy.app import App
from kivy.uix.widget import Widget
import pytmx
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.image import Image as CoreImage
from StartSceen import BrightnessLevel

class MapWidget(Widget):
    Map = None
    Brightness_Manager = BrightnessLevel()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Blocks = [] # Use for Collsions
        self.Blocks_coords = []
        self.Tile_size = 32
        self.Spawnpoint = ()
        self.Window_change = False
        self.Current_Level = "Graphics\Maps\Level1.tmx"
        self.BrightRect = None
        self.BrightColor = None
        # Window.bind(mouse_pos=self.on_hover)
    
    def Load_Level(self):
        self.Map = pytmx.TiledMap(self.Current_Level)
        for layer in self.Map.layers:
            if layer.name != "Objects":
                for x,y,image in layer.tiles():
                    if layer.name == "Background":
                        image = CoreImage(image[0]).texture
                        with self.canvas:
                            x,y = self.Tile_Transformation(x,y,layer)
                            Rectangle(pos=(x,y),size=(self.Tile_size,self.Tile_size),texture=image)
                            # self.Blocks_coords.append((x,y,size))
                    elif layer.name == "Main":
                        image = CoreImage(image[0]).texture
                        with self.canvas:
                            x,y = self.Tile_Transformation(x,y,layer)
                            Rectangle(pos=(x,y),size=(self.Tile_size,self.Tile_size),texture=image)
                            self.Add_Block(x,y,self.Tile_size)
                            # self.Blocks_coords.append((x,y,size))
        for obj in self.Map.objects:
            if obj.name == "Spawn":
                y_ratio = obj.y/(self.Map.layers[0].height *32)
                x_ratio = obj.x/(self.Map.layers[0].width *32)
                self.Spawnpoint = (int(x_ratio*Window.width),int(Window.height*y_ratio))
        self.Get_brightness(self.Brightness_Manager.return_brightness())

    def Get_brightness(self,Brightness):
        try:
            if self.BrightColor:
                self.canvas.children.remove(self.BrightColor)
                self.canvas.children.remove(self.BrightRect)
        except:pass
        with self.canvas:
            Brightness = (100 - Brightness)/100
            self.BrightColor = Color(0,0,0,Brightness)
            self.BrightRect = Rectangle(pos=(0,0),size=(Window.width,Window.height))

    # def on_hover(self, window, pos):
    #     for block in self.Blocks_coords:
    #         if (block[0] <= pos[0] <= block[0] + block[2]) and (block[1] <= pos[1] <= block[1] + block[2]):
    #             print(block[0:2])
    #             print(block[0] + block[2],block[1] + block[2])
    
    def Tile_Transformation(self,x,y,layer):
        x_scale = Window.width/(layer.width *self.Tile_size)
        y_scale = Window.height/(layer.height * self.Tile_size)
        scale = max(x_scale,y_scale) # Figure out later
        tr_x = x * self.Tile_size * x_scale
        tr_y = (layer.height - y - 1) * self.Tile_size * y_scale 
        self.Tile_size = self.Tile_size * scale
        return int(tr_x),int(tr_y)
    
    def Add_Block(self,x,y,size): # This needs to get a blocks top,left,right,bottom
        Rect = Widget(pos=(x, y), size=(size, size))
        self.Blocks.append(Rect)

    def on_size(self,*args):
        self.Blocks = []
        # self.Blocks_coords = []
        self.canvas.clear()
        self.Load_Level()
        self.Window_change = True

if __name__ == "__main__":
    class MapApp(App):
        def build(self):
            
            return MapWidget()

    MapApp().run()