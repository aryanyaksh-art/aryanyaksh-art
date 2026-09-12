from PIL import Image, ImageDraw, ImageFont
import sys

txt_path = sys.argv[1]
out_path = sys.argv[2]

with open(txt_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

font = None
for candidate in [
    "C:/Windows/Fonts/consola.ttf",
    "C:/Windows/Fonts/cour.ttf",
]:
    try:
        font = ImageFont.truetype(candidate, 14)
        break
    except Exception:
        continue
if font is None:
    font = ImageFont.load_default()

char_w, char_h = 8, 16
cols = max(len(l) for l in lines)
rows = len(lines)
img_w = cols * char_w + 40
img_h = rows * char_h + 40

bg = (13, 17, 23)
fg = (201, 209, 217)

img = Image.new("RGB", (img_w, img_h), bg)
draw = ImageDraw.Draw(img)
for i, line in enumerate(lines):
    draw.text((20, 20 + i * char_h), line, font=font, fill=fg)

img.save(out_path)
print(f"saved {out_path} ({img_w}x{img_h})")
