from PIL import Image, ImageDraw
import hashlib
from datetime import datetime
import json

# Redefining the class with the corrected pattern generation
class MakeProfileIconPython:
    def __init__(self):
        self.md5 = ''
        self.md5_18_color = ''
        self.md5_18_bg = ''
    
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
        return hex_colors

    def generate(self):
        # Reset hex_colors for each new image
        self.hex_colors = []
        
        # Generate date and hash
        date_str = datetime.now().strftime('%Y%m%d%H%M%S%f')
        self.md5 = hashlib.md5(date_str.encode()).hexdigest()
        self.md5_18_color = self.md5[:6]
        self.md5_18_bg = self.md5[7:13]

        # Create image and draw object
        im = Image.new('RGB', (400, 400), 'white')
        draw = ImageDraw.Draw(im)

        # Generate color patterns
        bg_pattern = [self.md5_18_bg] * 8
        self.hex_colors.extend(self.color(draw, 1, bg_pattern))
        
        # Create a color pattern based on the odd/even characters of the hash
        for i in range(2, 8):
            pattern = [self.md5_18_bg] + [self.md5_18_color if self.is_odd(char) else self.md5_18_bg for char in self.md5[i*3-6:i*3-3]] + [self.md5_18_bg]
            self.hex_colors.extend(self.color(draw, i, pattern))

        self.hex_colors.extend(self.color(draw, 8, bg_pattern))

        # Save the image to a file with the current datetime as its name
        file_path = f'./dist/images/{date_str}.png'
        im.save(file_path)
        
        return file_path, date_str

    def generate_with_json(self):
        # Generate the image and get the file path and date string
        file_path, date_str = self.generate()
        
        # Prepare the pattern for JSON
        pattern_str = ''.join(['x' if c == self.md5_18_bg else '-' for c in self.hex_colors])

        # Create JSON object
        json_data = {
            "date": date_str,
            "md5": self.md5,
            "background": f"#{self.md5_18_bg}",
            "color": f"#{self.md5_18_color}",
            "pattern": pattern_str,
            "generator": "3"
        }
        # Save JSON to a file
        json_path = f'./dist/json/{date_str}.json'
        with open(json_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        
        return json_path

# Generate 10 images with corresponding JSON files
make_icon_with_json = MakeProfileIconPython()
image_json_paths = [make_icon_with_json.generate_with_json() for _ in range(30)]
image_json_paths
