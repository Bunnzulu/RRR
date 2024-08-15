from kivy.app import App
from kivy.uix.widget import Widget
import pytmx
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.image import Image as CoreImage

class MapWidget(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Blocks = [] # Use for Collsions
        self.Blocks_coords = []
        self.Tile_size = 32
        self.Spawnpoint = ()
        self.Current_Level = "Graphics\Maps\Level1.tmx"
        # Window.bind(mouse_pos=self.on_hover)
    
    def Load_Level(self):
        Map = pytmx.TiledMap(self.Current_Level)
        for layer in Map.layers:
            if layer.name != "Objects":
                for x,y,image in layer.tiles():
                    if layer.name == "Background":
                        image = CoreImage(image[0]).texture
                        with self.canvas:
                            x,y,size = self.Tile_Transformation(x,y,layer)
                            Rectangle(pos=(x,y),size=(size,size),texture=image)
                            # self.Blocks_coords.append((x,y,size))
                    elif layer.name == "Main":
                        image = CoreImage(image[0]).texture
                        with self.canvas:
                            x,y,size = self.Tile_Transformation(x,y,layer)
                            Rectangle(pos=(x,y),size=(size,size),texture=image)
                            self.Add_Block(x,y,size)
                            # self.Blocks_coords.append((x,y,size))
        for obj in Map.objects:
            if obj.name == "Spawn":
                self.Spawnpoint = (obj.x,int(((Map.height*self.Tile_size)-obj.y)*Window.height/(Map.layers[0].height*self.Tile_size)))
                # print(self.Spawnpoint)
        
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
        size = self.Tile_size * scale
        return int(tr_x),int(tr_y),int(size)
    
    def Add_Block(x,y,size): # This needs to get a blocks top,left,right,bottom
        pass 

    def on_size(self,*args):
        self.Blocks = []
        self.Blocks_coords = []
        self.canvas.clear()
        self.Load_Level()

if __name__ == "__main__":
    class MapApp(App):
        def build(self):
            
            return MapWidget()

    MapApp().run()