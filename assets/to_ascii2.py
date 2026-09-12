from PIL import Image, ImageOps, ImageFilter
import sys

path = sys.argv[1]
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 70
mode = sys.argv[3] if len(sys.argv) > 3 else "edge"
char_aspect = 0.52

ramp = " .:-=+*#%@"

img = Image.open(path).convert("L")
img = ImageOps.autocontrast(img, cutoff=1)

if mode == "edge":
    edges = img.filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.autocontrast(edges, cutoff=0)
    base = img.point(lambda p: p * 0.35)
    combined = Image.blend(base, edges, alpha=0.75)
    src = combined
else:
    src = img

w, h = src.size
rows = max(1, int((h / w) * cols * char_aspect))
src = src.resize((cols, rows), Image.LANCZOS)

pixels = list(src.getdata())
lines = []
for r in range(rows):
    row_chars = []
    for c in range(cols):
        p = pixels[r * cols + c]
        idx = int(p / 255 * (len(ramp) - 1))
        row_chars.append(ramp[idx])
    lines.append("".join(row_chars))

print("\n".join(lines))
