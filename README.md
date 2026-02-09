# Computational String Art

A Python-based algorithm capable of recreating an image using only straight lines, also known as string art.  
This project was inspired by the mathematical concepts explained in this video:  
https://youtu.be/WGccIFf6MF8


## 📌 Overview

Computational String Art simulates the physical process of creating string art by stretching threads between nails placed on a circular frame. The algorithm reconstructs a grayscale image by iteratively selecting the best possible straight lines that pass through the darkest regions of the image.

This project demonstrates the application of:

- Geometry
- Greedy optimization
- Image processing
- Computational graphics

It converts a photograph into a visually striking string-art-style reconstruction using only straight line segments.

## Results
Lets take a quick peak how it will look after execution:
(output_comparison.png)


## 🎯 Target Audience

- Students interested in:
  - Algorithms
  - Image processing
  - Computational art
- General developers exploring:
  - Optimization techniques
  - Creative coding
  - Visual computing


## 🧠 How It Works (High-Level)

1. The input image is converted to grayscale and cropped into a perfect circle.
2. A fixed number of nails are placed uniformly along the circumference.
3. Starting from one nail, the algorithm:
   - Evaluates all valid connecting lines.
   - Chooses the line that passes through the darkest average region.
   - Draws that line.
   - Removes the used darkness from the reference image.
4. This process is repeated thousands of times, gradually reconstructing the image using only straight lines.

This method follows a greedy optimization strategy.


## 🛠 Installation & Setup

### Requirements

```
pip install requirements.txt
```
## ▶ How to Run

### This project is configured for manual parameter control.
-Open the Python file and edit:
```
path = r"YOUR_IMAGE_PATH"

BOARD_WIDTH = 80
PIXEL_WIDTH = 0.01
LINE_TRANSPARENCY = 0.3
NUM_NAILS = 300
MAX_ITERATIONS = 5000
```
Then run:
```
python main.py
```
## ⚙ Parameter Description

| Parameter         | Description                              |
| ----------------- | ---------------------------------------- |
| BOARD_WIDTH       | Physical diameter of the circular board  |
| PIXEL_WIDTH       | Pixel resolution scaling factor          |
| NUM_NAILS         | Number of nails placed around the circle |
| MAX_ITERATIONS    | Number of threads drawn                  |
| LINE_TRANSPARENCY | Transparency factor of thread overlay    |
| path              | Input image file path                    |

Higher values of NUM_NAILS and MAX_ITERATIONS result in better quality but slower execution.

## 📂 Output Files

The program generates:

-output*.png → Final string art image
-output_comparison.png → Side-by-side comparison (original vs generated)
-results.txt → Sequence of nail connections

## 📊 Example Output

The comparison output shows:
-Left → Original reference image
-Right → Generated string art

This allows direct visual evaluation of reconstruction accuracy.

## 🧮 Mathematical Foundation

The algorithm is based on:

-Circular geometry
-Parametric equations of a circle
-Line integral minimization
-Greedy optimization

At every step, the algorithm minimizes:
Average Brightness Along Line

This ensures that each string contributes maximum structural detail to the final image.

## 🚀 Future Scope

Generating actual physical string art using the computed nail sequence.
Exploring mechanical or CNC-assisted thread placement.

## 📜 License
This project is open-source and free for educational and personal use.

## ✍ Author

### Arnab Datta

GitHub: https://github.com/Arnab500th