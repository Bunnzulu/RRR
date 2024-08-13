from kivy.app import App
from kivy.uix.widget import Widget
import pytmx
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.image import Image as CoreImage

class MapWidget(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Blocks = []
        self.Blocks_coords = []
        self.Tile_size = 32
        # Window.bind(mouse_pos=self.on_hover)
        self.Load_Level("Graphics\Maps\Level1.tmx")
    
    def Load_Level(self,Level):
        Map = pytmx.TiledMap(Level)
        for layer in Map.layers:
            for x,y,image in layer.tiles():
                image = CoreImage(image[0]).texture
                with self.canvas:
                    x,y,size = self.Tile_Transformation(x,y,layer)
                    self.Blocks.append(Rectangle(pos=(x,y),size=(size,size),texture=image))
                    self.Blocks_coords.append(self.Tile_Transformation(x,y,layer))
                    print(x,y,size)
    
    # def on_hover(self, window, pos):
    #     for block in self.Blocks_coords:
    #         if (block[0] <= pos[0] <= block[0] + block[2]) and (block[1] <= pos[1] <= block[1] + block[2]):
    #             print(block[0:2])
    #             print(block[0] + 32,block[1] + 32)
    
    def Tile_Transformation(self,x,y,layer):
        x_scale = Window.width/(layer.width *self.Tile_size)
        y_scale = Window.height/(layer.height * self.Tile_size)
        scale = min(x_scale,y_scale)
        tr_x = x * self.Tile_size * scale
        tr_y = (layer.height - y - 1) * self.Tile_size * scale 
        size = self.Tile_size * scale
        return int(tr_x),int(tr_y),int(size)

if __name__ == "__main__":
    class MapApp(App):
        def build(self):
            return MapWidget()

    MapApp().run()