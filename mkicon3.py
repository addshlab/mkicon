from PIL import Image, ImageDraw
import hashlib
from datetime import datetime

class MakeProfileIconPython:
    def __init__(self):
        self.hex_colors = []
    
    def is_odd(self, char):
        return char in ['1', '3', '5', '7', '9', 'b', 'd', 'f']

    def color(self, draw, times, hex_colors):
        # Ensure symmetry by mirroring the colors
        hex_colors = hex_colors[:4] + hex_colors[:4][::-1]
        for i, hex_color in enumerate(hex_colors):
            x1 = i * 50
            x2 = x1 + 50
            y1 = (times - 1) * 50
            y2 = times * 50
            if len(hex_color) == 6:
                r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
                draw.rectangle([x1, y1, x2, y2], fill=(r, g, b))

    def generate(self):
        # Generate date and hash
        date_str = datetime.now().strftime('%Y%m%d%H%M%S%f')
        md5 = hashlib.md5(date_str.encode()).hexdigest()
        md5_18_color = md5[:6]
        md5_18_bg = md5[7:13]

        # Create image and draw object
        im = Image.new('RGB', (400, 400), 'white')
        draw = ImageDraw.Draw(im)

        # Generate color patterns
        bg_pattern = [md5_18_bg] * 8
        self.color(draw, 1, bg_pattern)
        
        # Create a color pattern based on the odd/even characters of the hash
        for i in range(2, 8):
            pattern = [md5_18_bg] + [md5_18_color if self.is_odd(char) else md5_18_bg for char in md5[i*3-6:i*3-3]] + [md5_18_bg]
            self.color(draw, i, pattern)

        self.color(draw, 8, bg_pattern)

        # Save the image to a file with the current datetime as its name
        file_path = f'icon3/profile_icon_{date_str}.png'
        im.save(file_path)
        return file_path

make_icon = MakeProfileIconPython()
image_path = make_icon.generate()
