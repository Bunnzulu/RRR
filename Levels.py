from kivy.app import App
from kivy.uix.widget import Widget
import pytmx
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.image import Image as CoreImage

class MapWidget(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Load_Level("Graphics\Maps\Level1.tmx")
        print(Window.width,Window.height)
    def Load_Level(self,Level):
        Map = pytmx.TiledMap(Level)
        for layer in Map.layers:
            for x,y,image in layer.tiles():
                image = CoreImage(image[0]).texture
                with self.canvas:
                    Rectangle(pos=(x*1000/40,y),size=(32,32),texture=image)
                    print(x*1000/40)
    
    def Tile_Transformation(x,y,layer):
        pass
    



if __name__ == "__main__":
    class MapApp(App):
        def build(self):
            return MapWidget()

    MapApp().run()