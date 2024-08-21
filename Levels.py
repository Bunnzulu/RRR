from kivy.app import App
from kivy.uix.widget import Widget
import pytmx
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.image import Image as CoreImage
from kivy.uix.label import Label
from kivy.graphics import Rotate,PushMatrix,PopMatrix,Translate
from StartSceen import BrightnessLevel

class MapWidget(Widget):
    Map = None
    Brightness_Manager = BrightnessLevel()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Blocks = [] 
        self.HMovingBlocks = []
        self.VMovingBlocks = []
        self.Blocks_coords = []
        self.HBorders = []
        self.VBorders = []
        self.Tile_size = 32
        self.Spawnpoint = ()
        self.Window_change = False
        self.Level = 4
        self.Current_Level = f"Graphics\\Maps\\Level{self.Level}.tmx"
        self.BrightRect = None
        self.BrightColor = None
        self.Sprint_label = Label
        self.Player_Amno = Label
        self.NextDoor = Widget
        # Window.bind(mouse_pos=self.on_hover)
    
    def Load_Level(self):
        platform = []
        self.Map = pytmx.TiledMap(self.Current_Level)
        for layer in self.Map.layers:
            if layer.name != "Objects":
                for x,y,image in layer.tiles():
                    if layer.name == "Background":
                        image = CoreImage(image[0]).texture
                        with self.canvas:
                            x,y = self.Tile_Transformation(x,y,layer)
                            Rectangle(pos=(x,y),size=(self.Tile_size,self.Tile_size),texture=image)
                    elif layer.name == "Main":
                        image = CoreImage(image[0]).texture
                        with self.canvas:
                            x,y = self.Tile_Transformation(x,y,layer)
                            Rectangle(pos=(x,y),size=(self.Tile_size,self.Tile_size),texture=image)
                            self.Add_Block(x,y,self.Tile_size)
                    elif layer.name == "HMoving":
                        image = CoreImage(image[0]).texture
                        x,y = self.Tile_Transformation(x,y,layer)
                        block = Rectangle(pos=(x,y),size=(self.Tile_size,self.Tile_size),texture=image)
                        self.canvas.add(block)
                        platform.append(block)
                        self.Add_Block(x,y,self.Tile_size)
                    elif layer.name == "VMoving":
                        image = CoreImage(image[0]).texture
                        x,y = self.Tile_Transformation(x,y,layer)
                        block = Rectangle(pos=(x,y),size=(self.Tile_size,self.Tile_size),texture=image)
                        self.canvas.add(block)
                        self.VMovingBlocks.append([block,1])
                        self.Add_Block(x,y,self.Tile_size)
        if platform:self.HMovingBlocks.append([platform,1])
        for obj in self.Map.objects:
            y_ratio = obj.y/(self.Map.layers[0].height *32)
            x_ratio = obj.x/(self.Map.layers[0].width *32)
            y = int((self.Map.layers[0].height *32)-(Window.height*y_ratio))
            pos=(int(x_ratio*Window.width),y)
            if obj.name == "Spawn":
                self.Spawnpoint = pos
            elif obj.name == "Rule":
                color = obj.properties.get('Color', '#FFFFFF')
                color = color.lstrip('#')  
                a = int(color[0:2], 16) / 255.0
                g = int(color[2:4], 16) / 255.0
                b = int(color[4:6], 16) / 255.0
                r = int(color[6:], 16) / 255.0
                font_size = obj.properties.get('font_size')
                text = Label(text=obj.Text,pos=pos,color=(r,g,b,a),font_size=font_size,font_name="Fonts\Montserrat-Black.ttf")
                with text.canvas.before:
                    PushMatrix()
                    Translate(text.center_x, text.center_y)
                    Rotate(angle=int(-obj.rotation))
                    Translate(-text.center_x, -text.center_y)
                with text.canvas.after:
                    PopMatrix()
                self.add_widget(text)
            elif obj.name == "Anmo":
                image = CoreImage(obj.image[0]).texture
                with self.canvas:
                    Rectangle(pos=pos,size=(obj.width,obj.height),texture=image)
            elif obj.name == "AInfo":
                self.Player_Amno = Label(text="0/10",pos=pos,color=(0,0,0,1),font_size=20,font_name="Fonts\Montserrat-Black.ttf")
                self.add_widget(self.Player_Amno)
            elif obj.name == "Gun":
                image = CoreImage(obj.image[0]).texture
                with self.canvas:
                    Rectangle(pos=pos,size=(obj.width,obj.height),texture=image)
            elif obj.name == "GunInfo":
                color = obj.properties.get('Color', '#FFFFFF')
                color = color.lstrip('#')  
                a = int(color[0:2], 16) / 255.0
                g = int(color[2:4], 16) / 255.0
                b = int(color[4:6], 16) / 255.0
                r = int(color[6:], 16) / 255.0
                font_size = obj.properties.get('font_size')
                text = Label(text=obj.Text,pos=pos,color=(r,g,b,a),font_size=font_size,font_name="Fonts\Montserrat-Regular.ttf")
                self.add_widget(text)
            elif obj.name == "NextSign":
                color = obj.properties.get('Color', '#FFFFFF')
                color = color.lstrip('#')  
                a = int(color[0:2], 16) / 255.0
                g = int(color[2:4], 16) / 255.0
                b = int(color[4:6], 16) / 255.0
                r = int(color[6:], 16) / 255.0
                font_size = obj.properties.get('font_size')
                text = Label(text=obj.Text,pos=pos,color=(r,g,b,a),font_size=font_size,font_name="Fonts\Montserrat-Black.ttf")
                self.add_widget(text)
            elif obj.name == "Note":
                color = obj.properties.get('Color', '#FFFFFF')
                color = color.lstrip('#')  
                a = int(color[0:2], 16) / 255.0
                g = int(color[2:4], 16) / 255.0
                b = int(color[4:6], 16) / 255.0
                r = int(color[6:], 16) / 255.0
                font_size = obj.properties.get('font_size')
                text = Label(text=obj.Text,pos=pos,color=(r,g,b,a),font_size=font_size,font_name="Fonts\Montserrat-Black.ttf")
                self.add_widget(text)
            elif obj.name == "Next":
                self.NextDoor = Widget(pos=pos,size=(obj.width,obj.height))
                with self.canvas:
                    Rectangle(pos=pos,size=(obj.width,obj.height))
            elif obj.name == "SC":
                color = obj.properties.get('Color', '#FFFFFF')
                color = color.lstrip('#')  
                a = int(color[0:2], 16) / 255.0
                g = int(color[2:4], 16) / 255.0
                b = int(color[4:6], 16) / 255.0
                r = int(color[6:], 16) / 255.0
                font_size = obj.properties.get('font_size')
                self.Sprint_label = Label(text=obj.Text,pos=pos,color=(r,g,b,a),font_size=font_size,font_name="Fonts\Montserrat-Black.ttf")
                self.add_widget(self.Sprint_label)
            elif obj.name == "H":
                self.HBorders.append(round(pos[0]))
            elif obj.name == "V":
                self.VBorders.append(round(pos[1]))
                # with self.canvas:
                #     Rectangle(pos=pos,size=(10,10))
            
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

    def Move_Blocks(self):
        for index, block in enumerate(self.HMovingBlocks):
            for i, plat in enumerate(block[0]):
                x, y = plat.pos
                for o in range(len(self.Blocks)):
                    if self.Blocks[o].pos == plat.pos:
                        self.Blocks.remove(self.Blocks[o])
                        break

                x += block[1]
                plat.pos = (x, y)
                
                width = plat.size[0]
                if round(plat.pos[0]) in self.HBorders or round(plat.pos[0] + width) in self.HBorders:
                    block[1] *= -1
                
                block[0][i].pos = (x, y)
                block[0][i].texture.bind()
                self.Add_Block(x,y,block[0][i].size[1])

        for block in self.VMovingBlocks:
            x, y = block[0].pos
            for o in range(len(self.Blocks)):
                if self.Blocks[o].pos[0] == block[0].pos[0] and self.Blocks[o].pos[1] == block[0].pos[1]:
                    self.Blocks.remove(self.Blocks[o])
                    break
            y += block[1]
            block[0].pos = (x, y)
            self.Add_Block(x,y,block[0].size[1])
            block[0].texture.bind()

            height = block[0].size[1]
            if round(block[0].pos[1]) in self.VBorders or round(block[0].pos[1] + height) in self.VBorders:
                block[1] *= -1 


    def Tile_Transformation(self,x,y,layer):
        x_scale = Window.width/(layer.width *self.Tile_size)
        y_scale = Window.height/(layer.height * self.Tile_size)
        scale = max(x_scale,y_scale) # Figure out later
        tr_x = x * self.Tile_size * x_scale
        tr_y = (layer.height - y - 1) * self.Tile_size * y_scale 
        self.Tile_size = self.Tile_size * scale
        return int(tr_x),int(tr_y)
    
    def Add_Block(self,x,y,size):
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

