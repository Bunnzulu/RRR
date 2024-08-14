
class Player():
    def __init__(self):
        self.player_idle_Forward = "Graphics\Sprites\IdleF.png"
        self.player_idle_Backward = "Graphics\Sprites\IdleB.png"
        self.player_jump = "Graphics\Sprites\Jump.png"
        
        self.Direction_x = 0
        self.Direction_y = 0
    
    def Input(self,input):
        print(input)
    
    def update(self):
        pass