from PIL import Image, ImageOps, ImageDraw
from skimage.draw import line
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.perf_counter()

# INPUT CONFIGURATION

path = r"input.jpg"

#NOTE: These inputs generally need to be manually callibrated for a better match
BOARD_WIDTH = 80
PIXEL_WIDTH = 0.02
LINE_TRANSPARENCY = 0.3
NUM_NAILS = 300
MAX_ITERATIONS = 5000


NAILS_SKIP = 20
OUTPUT_TITLE = "output"
# IMAGE SETU

pixels = int(BOARD_WIDTH / PIXEL_WIDTH)
size = (pixels + 1, pixels + 1)

pic = Image.open(path)


def crop_to_circle(img_path):
    """
    Converts the input image into a circular grayscale masked image.
    """
    img = Image.open(img_path).convert("L")
    img = img.resize(size)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    mask = mask.resize(img.size, Image.Resampling.LANCZOS)
    img.putalpha(mask)

    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    return output


ref = crop_to_circle(path)
base = Image.new("L", size, color=255)

# NAIL GEOMETRY

angles = np.linspace(0, 2 * np.pi, NUM_NAILS)

cx = BOARD_WIDTH / (2 * PIXEL_WIDTH)
cy = BOARD_WIDTH / (2 * PIXEL_WIDTH)
radius = BOARD_WIDTH / (2 * PIXEL_WIDTH)

xs = cx + radius * np.cos(angles)
ys = cy + radius * np.sin(angles)

nails = [(int(x), int(y)) for x, y in zip(xs, ys)]

# INITIALIZATION

ref_arr = np.transpose(np.array(ref)[:, :, 0])
curr_nail = 1

results = open("results.txt", "w")
res = ""
# MAIN STRING ART LOOP

for iteration in range(1, MAX_ITERATIONS + 1):

    best_line = None
    next_nail = None
    min_avg_brightness = float("inf")

    for n in range(curr_nail + 1 + NAILS_SKIP,
                   curr_nail + NUM_NAILS - NAILS_SKIP):

        n %= NUM_NAILS

        candidate_line = line(
            nails[curr_nail][0], nails[curr_nail][1],
            nails[n][0], nails[n][1]
        )

        brightness_sum = np.sum(ref_arr[candidate_line])
        num_pixels = len(candidate_line[0])
        avg_brightness = brightness_sum / num_pixels

        if avg_brightness < min_avg_brightness:
            min_avg_brightness = avg_brightness
            best_line = candidate_line
            next_nail = n

    # Remove used darkness
    ref_arr[best_line] = 255

    # Draw selected string
    draw = ImageDraw.Draw(base)
    draw.line(
        (
            nails[curr_nail][0], nails[curr_nail][1],
            nails[next_nail][0], nails[next_nail][1]
        ),
        fill=0
    )

    res += " " + str(next_nail)
    print(f"Iteration {iteration} Complete: ({curr_nail}, {next_nail})")

    curr_nail = next_nail

# OUTPUT STORAGE

results.write(res)
results.close()

output_name = (
    f"{OUTPUT_TITLE}{BOARD_WIDTH}W-{PIXEL_WIDTH}P-"
    f"{NUM_NAILS}N-{MAX_ITERATIONS}-{LINE_TRANSPARENCY}.png"
)

base.save(output_name)

# VISUAL COMPARISON

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(pic)
axes[0].set_title("Reference Image")
axes[0].axis("off")

axes[1].imshow(base, cmap="gray")
axes[1].set_title(f"String Art ({iteration} iterations)")
axes[1].axis("off")

plt.tight_layout()
plt.savefig(f"{OUTPUT_TITLE}_comparison.png", dpi=150, bbox_inches="tight")

print(f"Comparison saved: {OUTPUT_TITLE}_comparison.png")

end_time = time.perf_counter()

Execution_time = end_time - start_time

print(f"Execution time: {Execution_time:.2f} seconds")