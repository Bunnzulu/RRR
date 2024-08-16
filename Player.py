from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage

class Player():
    def __init__(self):
        self.pos = {"x":0,"y":0}
        self.Width = 32
        self.Height = 32
        self.player_idle_Forward = "Graphics\\\Sprites\\\IdleF.png"
        self.player_idle_Backward = "Graphics\\\Sprites\\\IdleB.png"
        self.player_fjump = "Graphics\\\Sprites\\\FJump.png"
        self.player_bjump = "Graphics\\\Sprites\\\BJump.png"
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
    
    def Input(self,keycode):
        if keycode[1] == "left":
            self.Direction_x = -self.Walkspeed
            self.Forward = False
        elif keycode[1] == "right":
            self.Direction_x = self.Walkspeed
            self.Forward = True
        elif keycode[1] == "spacebar" and not self.inair:
            self.Direction_y = 10
            self.inair = True
            print("Death")
        elif keycode[1] == 'shift':
            self.Direction_x = -self.SprintSpeed
            self.Forward = False
        elif keycode[1] == 'rshift':
            self.Direction_x = self.SprintSpeed
            self.Forward = True
    
    def Movement_Reset(self):
        self.Direction_x = 0
        self.Direction_y = 0
        if self.Forward:self.image = self.player_idle_Forward
        else:self.image = self.player_idle_Backward

    def Collision(self):
        self.CollideWiget = Widget(pos=(self.pos["x"],self.pos["y"]),size=(self.Width,self.Height))
        #Vertical
        for border in self.Borders:
            if self.CollideWiget.collide_widget(border):
                if self.Direction_y < 0: #Falling
                    if self.pos["y"] < border.top <= self.CollideWiget.top:
                        self.pos["y"] = border.top
                        self.inair = False
                        self.Direction_y = 0
                elif self.Direction_y > 0:
                    if self.CollideWiget.top > border.y > self.pos["y"] and border.x < self.CollideWiget.center_x < border.right:
                        self.pos["y"] = border.y - self.Height
                        self.Direction_y = 0
        #Horizontal
        for border in self.Borders:
            if self.CollideWiget.collide_widget(border):
                if self.Direction_x < 0:
                    if self.CollideWiget.x < border.right <= self.CollideWiget.right and border.y < self.CollideWiget.center_y < border.top:
                        self.pos["x"] = border.right
                        self.Direction_x = 0
                elif self.Direction_x > 0:
                    if border.y < self.CollideWiget.center_y < border.top and self.CollideWiget.right > border.x >= self.CollideWiget.x:
                        self.pos["x"] = border.x - self.Width
                        self.Direction_x = 0

    def Animations(self):
        if not self.inair:
            if self.Direction_x == self.Walkspeed:
                self.FWalkIndex += 0.1
                if self.FWalkIndex >= len(self.FWalking): self.FWalkIndex = 0
                self.image = f"Graphics\\\Sprites\\\{self.FWalking[int(self.FWalkIndex)]}.png"
                self.BWalkIndex = 0
                self.FRunningIndex = 0
                self.BRunningIndex = 0
            elif self.Direction_x == -self.Walkspeed:
                self.BWalkIndex += 0.1
                if self.BWalkIndex >= len(self.BWalking): self.BWalkIndex = 0
                self.image = f"Graphics\\\Sprites\\\{self.BWalking[int(self.BWalkIndex)]}.png"
                self.FWalkIndex = 0
                self.FRunningIndex = 0
                self.BRunningIndex = 0
            elif self.Direction_x == self.SprintSpeed:
                self.FRunningIndex += 0.1
                if self.FRunningIndex >= len(self.FRunning): self.FRunningIndex = 0
                self.image = f"Graphics\\\Sprites\\\{self.FRunning[int(self.FRunningIndex)]}.png"
                self.BWalkIndex = 0
                self.FWalkIndex = 0
                self.BRunningIndex = 0
            elif self.Direction_x == -self.SprintSpeed:
                self.BRunningIndex += 0.1
                if self.BRunningIndex >= len(self.BRunning): self.BRunningIndex = 0
                self.image = f"Graphics\\\Sprites\\\{self.BRunning[int(self.BRunningIndex)]}.png"
                self.FWalkIndex = 0
                self.FRunningIndex = 0
                self.BWalkIndex = 0
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
