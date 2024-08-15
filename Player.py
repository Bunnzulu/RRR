from kivy.uix.widget import Widget
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
        self.BWalking = ["BRun1","BRun3"]
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
        self.CollideWiget = Widget(pos=(self.pos["x"],self.pos["y"]),size=(self.Width,self.Height))
        self.Borders = []
    
    def Input(self,key):
        if key == "left":
            self.Direction_x = -self.Walkspeed
            self.Forward = False
        elif key == "right":
            self.Direction_x = self.Walkspeed
            self.Forward = True
        elif key == "spacebar":
            self.Direction_y = 10
            self.inair = True
    
    def Movement_Reset(self):
        self.Direction_x = 0
        self.Direction_y = 0
        if self.Forward:self.image = self.player_idle_Forward
        else:self.image = self.player_idle_Backward

    def Collision(self):
        self.CollideWiget = Widget(pos=(self.pos["x"],self.pos["y"]),size=(self.Width,self.Height))
        for border in self.Borders:
            if self.CollideWiget.collide_widget(border):
                if self.Direction_y < 0:
                    if self.pos["y"] < border.pos[1]+border.size[1]:
                        self.pos["y"] = border.pos[1]+border.size[1]
                        self.inair = False
                        self.Direction_y = 0
                elif self.Direction_y > 0:
                    if self.pos["y"] + self.Height > border.pos[1]:
                        self.pos["y"] = border.pos[1] - self.Height
                        self.inair = False
                        # self.Direction_y = 0

    def Animations(self):
        if not self.inair:
            if self.Direction_x == self.Walkspeed:
                self.FWalkIndex += 0.1
                if self.FWalkIndex >= len(self.FWalking): self.FWalkIndex = 0
                self.image = f"Graphics\\Sprites\\{self.FWalking[int(self.FWalkIndex)]}.png"
                self.BWalkIndex = 0
                self.FRunningIndex = 0
                self.BRunningIndex = 0
            elif self.Direction_x == -self.Walkspeed:
                self.BWalkIndex += 0.1
                if self.BWalkIndex >= len(self.BWalking): self.BWalkIndex = 0
                self.image = f"Graphics\\Sprites\\{self.BWalking[int(self.BWalkIndex)]}.png"
                self.FWalkIndex = 0
                self.FRunningIndex = 0
                self.BRunningIndex = 0
        else:
            if self.Direction_x == self.Walkspeed:
                self.image = self.player_fjump
                self.BWalkIndex = 0
                self.FRunningIndex = 0
                self.BRunningIndex = 0
            elif self.Direction_x == -self.Walkspeed:
                self.image = self.player_bjump
                self.BWalkIndex = 0
                self.FRunningIndex = 0
                self.BRunningIndex = 0

    def gravity(self):
        self.Direction_y -= 1
    
    def update(self):
        self.Animations()
        self.Collision()
        self.gravity()
        self.Display_image = CoreImage(self.image).texture
        self.pos["x"] += self.Direction_x
        self.pos["y"] += self.Direction_y
