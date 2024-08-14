from PIL import Image

# Load the spritesheet
spritesheet = Image.open(r'Graphics\Sprites\buddie0 sprite sheet x3.png')

# Define the size of each sprite (assuming all sprites are the same size)
sprite_width = 96  # Change to the width of your sprite
sprite_height = 96  # Change to the height of your sprite

# Number of rows and columns in the spritesheet
rows = spritesheet.height // sprite_height
cols = spritesheet.width // sprite_width

# Extract individual sprites
sprites = []
for row in range(rows):
    for col in range(cols):
        # Calculate the position of the sprite in the spritesheet
        x = col * sprite_width
        y = row * sprite_height
        # Crop the sprite
        sprite = spritesheet.crop((x, y, x + sprite_width, y + sprite_height))
        sprites.append(sprite)

# Save or use the individual sprites
for i, sprite in enumerate(sprites):
    if i in (0,8,16,24,25,26,27,32,33,34,35,36,37,38,39):
        sprite.save(f'sprite_{i}.png')  # Save each sprite as a separate image file



class Player():
    def __init__(self):
        self.Forward_sprites = []
        self.Backword_sprites = []
        self.Direction_x = 0
        self.Direction_y = 0
    
    def Input(self,input):
        print(input)