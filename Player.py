
from kivy.core.image import Image as CoreImage

class Player():
    def __init__(self):
        self.pos = {"x":0,"y":0}
        self.Width = 32
        self.Height = 32
        self.player_idle_Forward = "Graphics\\Sprites\\IdleF.png"
        self.player_idle_Backward = "Graphics\\Sprites\\IdleB.png"
        self.player_fjump = "Graphics\\Sprites\\FJump.png"
        self.player_bjump = "Graphics\\Sprites\\BJump.png"
        self.FWalking = ["FRun1","FRun3"]
        self.FRunning = ["FRun1","FRun2","FRun3","FRun4"]
        self.FWalking = ["BRun1","BRun3"]
        self.BRunning = ["BRun1","BRun2","BRun3","BRun4"]
        self.Direction_x = 0
        self.Direction_y = 0
        self.FWalkIndex = 0
        self.BWalkIndex = 0
        self.FRunningIndex = 0
        self.BRunningIndex = 0
        self.Walkspeed = 1
        self.SprintSpeed = self.Walkspeed * 2
        self.Forward = True
        self.inair = False
        self.image = self.player_idle_Forward
        self.Display_image = CoreImage(self.image).texture
        self.DrawnRect = ''
    
    def Input(self,input):
        pass
    
    def Animation(self):
        pass

    def gravity(self):
        if self.inair:
            self.Direction_y -= 1
    
    def update(self):
        self.Display_image = CoreImage(self.image).texture
        self.gravity()
        self.pos["x"] += self.Direction_x
        self.pos["y"] += self.Direction_y
