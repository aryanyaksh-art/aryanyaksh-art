from PIL import Image, ImageEnhance
import sys

path = sys.argv[1]
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 46
char_aspect = 0.52

ramp = " .:-=+*#%@"

img = Image.open(path).convert("L")
img = ImageEnhance.Contrast(img).enhance(1.35)
w, h = img.size
rows = max(1, int((h / w) * cols * char_aspect))
img = img.resize((cols, rows))

pixels = list(img.getdata())
lines = []
for r in range(rows):
    row_chars = []
    for c in range(cols):
        p = pixels[r * cols + c]
        idx = int(p / 255 * (len(ramp) - 1))
        row_chars.append(ramp[idx])
    lines.append("".join(row_chars))

print("\n".join(lines))
