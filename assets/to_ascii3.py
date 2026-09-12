from PIL import Image, ImageOps, ImageFilter, ImageChops
import sys

path = sys.argv[1]
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 80
char_aspect = 0.52
ramp = " .:-=+*#%@"

img = Image.open(path).convert("L")

edges = img.filter(ImageFilter.FIND_EDGES)
edges = edges.filter(ImageFilter.MaxFilter(3))
edges = ImageOps.autocontrast(edges, cutoff=0)

gamma = 0.45
base = img.point(lambda p: int(255 * ((p / 255) ** gamma)))
base = base.point(lambda p: max(0, p - 60))

combined = ImageChops.lighter(base, edges)

w, h = combined.size
rows = max(1, int((h / w) * cols * char_aspect))
small = combined.resize((cols, rows), Image.LANCZOS)

pixels = list(small.getdata())
lines = []
for r in range(rows):
    row_chars = []
    for c in range(cols):
        p = pixels[r * cols + c]
        idx = int(p / 255 * (len(ramp) - 1))
        row_chars.append(ramp[idx])
    lines.append("".join(row_chars))

print("\n".join(lines))
