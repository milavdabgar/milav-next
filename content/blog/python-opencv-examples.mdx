---
title: "Comprehensive Guide to OpenCV with Python"
date: 2025-03-06
description: "A practical tutorial covering essential OpenCV operations in Python with code examples"
summary: "This guide walks you through OpenCV basics in Python, from image loading and manipulation to advanced techniques like edge detection and contour analysis, with practical code examples for each concept."
tags: ["python", "opencv", "computer vision", "image processing", "tutorial", "programming"]
---

OpenCV (Open Source Computer Vision Library) is a powerful tool for image processing and computer vision tasks. This guide provides practical examples of using OpenCV with Python to perform common image manipulation operations.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation and Setup](#installation-and-setup)
- [Basic Image Operations](#basic-image-operations)
  - [Loading and Displaying Images](#loading-and-displaying-images)
  - [Accessing and Modifying Pixels](#accessing-and-modifying-pixels)
- [Drawing on Images](#drawing-on-images)
  - [Lines and Rectangles](#lines-and-rectangles)
  - [Circles and Random Shapes](#circles-and-random-shapes)
- [Image Transformations](#image-transformations)
  - [Rotation](#rotation)
  - [Resizing](#resizing)
  - [Flipping](#flipping)
  - [Cropping](#cropping)
- [Image Arithmetic](#image-arithmetic)
- [Bitwise Operations](#bitwise-operations)
- [Masking](#masking)
- [Color Spaces](#color-spaces)
- [Histograms](#histograms)
  - [Grayscale Histograms](#grayscale-histograms)
  - [Color Histograms](#color-histograms)
  - [Histogram Equalization](#histogram-equalization)
  - [Masked Histograms](#masked-histograms)
- [Image Smoothing](#image-smoothing)
- [Thresholding](#thresholding)
  - [Simple Thresholding](#simple-thresholding)
  - [Adaptive Thresholding](#adaptive-thresholding)
- [Edge Detection](#edge-detection)
  - [Gradients (Sobel \& Laplacian)](#gradients-sobel--laplacian)
  - [Canny Edge Detector](#canny-edge-detector)
- [Contour Detection](#contour-detection)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)
  - [1. Image Not Loading](#1-image-not-loading)
  - [2. OpenCV Version Compatibility](#2-opencv-version-compatibility)
  - [3. Memory Errors with Large Images](#3-memory-errors-with-large-images)
  - [4. Windows Not Closing](#4-windows-not-closing)
  - [5. Slow Performance](#5-slow-performance)
  - [6. Video Capture Issues](#6-video-capture-issues)
  - [7. Color Space Conversion Errors](#7-color-space-conversion-errors)
- [Conclusion](#conclusion)

## Installation and Setup

Before starting, make sure you have OpenCV installed:

```python
# Install OpenCV using pip
pip install opencv-python

# For additional modules (including non-free algorithms)
pip install opencv-contrib-python
```

For this tutorial, we'll be using OpenCV 4.x, which has some syntax differences from older versions, particularly in functions like `findContours()`.

## Basic Image Operations

### Loading and Displaying Images

Let's start with the basics of loading and displaying images:

```python
import numpy as np
import cv2

# Load an image from file
img = cv2.imread('path/to/your/image.png')

# Display the image in a window
cv2.imshow('image', img)

# Wait for a key press (0 means wait indefinitely)
cv2.waitKey(0)

# Close all open windows
cv2.destroyAllWindows()

# You can create a resizable window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image to a new file
cv2.imwrite('output.jpg', img)
```

### Accessing and Modifying Pixels

You can access and modify individual pixels or regions:

```python
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Access a pixel value at coordinates (0, 0)
# Note: OpenCV uses BGR color order, not RGB
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Modify a pixel value
image[0, 0] = (0, 0, 255)  # Set to red
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Access and modify a region (ROI - Region of Interest)
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# Set the corner region to green
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
```

## Drawing on Images

### Lines and Rectangles

You can draw various shapes on images:

```python
import numpy as np
import cv2

# Create a blank canvas (black image)
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Draw a green line from top-left to bottom-right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a thicker red line from top-right to bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)  # 3 is the line thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a green rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a thicker red rectangle
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a filled blue rectangle
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)  # -1 means filled
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
```

### Circles and Random Shapes

Let's draw circles:

```python
# Create a new blank canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Find the center of the canvas
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# Draw concentric circles
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw random circles
for i in range(0, 25):
    # Generate random radius, color, and position
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    
    # Draw the circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
```

## Image Transformations

### Rotation

Rotating images is a common operation:

```python
import imutils  # A convenience package (pip install imutils)
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Get the image dimensions
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Generate the rotation matrix
M = cv2.getRotationMatrix2D(center, 45, 1.0)  # 45 degrees, scale 1.0
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# Rotate by -90 degrees
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

# Using the imutils convenience function
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
```

### Resizing

Resize images while maintaining aspect ratio:

```python
import imutils
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Resize based on width
r = 150.0 / image.shape[1]  # Calculate ratio to make width = 150px
dim = (150, int(image.shape[0] * r))  # Calculate new height to maintain aspect ratio
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# Resize based on height
r = 50.0 / image.shape[0]  # Calculate ratio to make height = 50px
dim = (int(image.shape[1] * r), 50)  # Calculate new width to maintain aspect ratio
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# Using the imutils convenience functions
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height=50)
cv2.imshow("Resized via Function h=50", resized)
cv2.waitKey(0)
```

### Flipping

Flip images horizontally, vertically, or both:

```python
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Flip horizontally (1)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# Flip vertically (0)
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# Flip both horizontally and vertically (-1)
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
```

### Cropping

Crop a region of interest from an image:

```python
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Cropping is done via array slicing [startY:endY, startX:endX]
cropped = image[30:120, 240:335]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
```

## Image Arithmetic

Understanding image arithmetic and handling overflows:

```python
import numpy as np
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# OpenCV's add/subtract functions handle 8-bit overflow by clamping
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))  # 255
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))  # 0

# But NumPy wraps around (modulo 256)
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))  # 44 (200+100=300, 300%256=44)
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))  # 206 (50-100=-50, -50%256=206)

# Increase brightness
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

# Decrease brightness
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
```

## Bitwise Operations

Perform bitwise operations on images:

```python
import numpy as np
import cv2

# Create a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# Create a circle
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# Bitwise AND (intersection of the two)
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# Bitwise OR (combination of the two)
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# Bitwise XOR (non-overlapping regions)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# Bitwise NOT (inverts the pixels)
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
```

## Masking

Apply masks to focus on specific image regions:

```python
import numpy as np
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Create a rectangular mask
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)

# Apply the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Create a circular mask
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
```

## Color Spaces

Work with different color spaces:

```python
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Convert to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# Convert to LAB color space
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
cv2.waitKey(0)
```

## Histograms

### Grayscale Histograms

Calculate and visualize image histograms:

```python
from matplotlib import pyplot as plt
import cv2

image = cv2.imread('path/to/your/image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Calculate histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
```

### Color Histograms

Calculate and visualize color histograms:

```python
from matplotlib import pyplot as plt
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Split the image into its channels
chans = cv2.split(image)
colors = ("b", "g", "r")

# Plot the color histogram
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

# 2D histograms for pairs of channels
fig = plt.figure()

# Green and Blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

# Green and Red
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

# Blue and Red
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

# Information about the histogram dimensions
print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

# 3D histogram (all three channels)
hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

plt.show()
```

### Histogram Equalization

Improve image contrast using histogram equalization:

```python
import numpy as np
import cv2

image = cv2.imread('path/to/your/image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
eq = cv2.equalizeHist(image)

# Show the original and equalized images side by side
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)
```

### Masked Histograms

Calculate histograms for specific regions:

```python
from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")

# Create a mask
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

# Apply the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the Mask", masked)

# Calculate histogram for the masked region
plot_histogram(image, "Histogram for Masked Image", mask=mask)
plt.show()
```

## Image Smoothing

Apply different blurring methods:

```python
import numpy as np
import cv2

image = cv2.imread('path/to/your/image.png')
cv2.imshow("Original", image)

# Average blurring
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# Gaussian blurring (less blur but more natural)
blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)
])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

# Median blurring (great for removing salt-and-pepper noise)
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)
])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

# Bilateral filtering (preserves edges while blurring)
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)
```

## Thresholding

### Simple Thresholding

Apply binary thresholding:

```python
import cv2

image = cv2.imread('path/to/your/image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# Binary thresholding
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# Inverse binary thresholding
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# Apply mask to original image
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
```

### Adaptive Thresholding

Use advanced thresholding algorithms:

```python
import mahotas  # pip install mahotas
import cv2

image = cv2.imread('path/to/your/image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# Otsu's method (automatically determines optimal threshold)
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

# Riddler-Calvard method
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
```

## Edge Detection

### Gradients (Sobel & Laplacian)

Detect edges using gradients:

```python
import numpy as np
import cv2

image = cv2.imread('path/to/your/image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Laplacian gradient
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

# Sobel gradient (x and y direction)
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)  # x direction
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)  # y direction

# Take absolute value and convert to 8-bit
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Combine both directions
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)
```

### Canny Edge Detector

Use the Canny edge detector:

```python
import cv2

image = cv2.imread('path/to/your/image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

# Apply Canny edge detector (minVal=30, maxVal=150)
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
```

## Contour Detection

Detect and process contours:

```python
import numpy as np
import cv2

image = cv2.imread('path/to/your/image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

# Detect edges
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

# Find contours
# Note: In OpenCV 4.x, the function returns only contours and hierarchy
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} objects in this image".format(len(contours)))

# Draw all contours
coins = image.copy()
cv2.drawContours(coins, contours, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

# Process each contour separately
for (i, c) in enumerate(contours):
    # Get bounding rectangle
    (x, y, w, h) = cv2.boundingRect(c)
    print("Object #{}".format(i + 1))
    
    # Extract the object
    obj = image[y:y + h, x:x + w]
    cv2.imshow("Object", obj)
    
    # Create a circular mask
    mask = np.zeros(image.shape[:2], dtype="uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    
    # Apply the mask
    cv2.imshow("Masked Object", cv2.bitwise_and(obj, obj, mask=mask))
    cv2.waitKey(0)
```

## Troubleshooting Common Issues

Here are solutions to common problems you might encounter:

### 1. Image Not Loading

If your image isn't loading, check:

- File path is correct
- File exists
- File permissions are appropriate
- File is a valid image format

Try using the full path instead of a relative path:

```python
img = cv2.imread('/full/path/to/your/image.png')
if img is None:
    print("Error: Could not load image")
```

### 2. OpenCV Version Compatibility

OpenCV 4.x changed some function signatures:

**Old (OpenCV 3.x):**

```python
_, contours, hierarchy = cv2.findContours(...)
```

**New (OpenCV 4.x):**

```python
contours, hierarchy = cv2.findContours(...)
```

Check your OpenCV version with:

```python
print(cv2.__version__)
```

### 3. Memory Errors with Large Images

For large images, consider:

- Resizing the image first
- Processing in smaller chunks
- Using 64-bit Python
- Increasing system swap space

### 4. Windows Not Closing

If windows aren't closing properly:

- Use `cv2.destroyAllWindows()` to close all windows
- Ensure all `cv2.waitKey()` calls are being processed
- Check for infinite loops in your code

### 5. Slow Performance

If operations are slow:

- Use NumPy vectorized operations instead of loops when possible
- Resize large images to a smaller size
- Use more efficient algorithms (e.g., `CHAIN_APPROX_SIMPLE` instead of `CHAIN_APPROX_NONE`)
- Pre-allocate arrays instead of growing them dynamically

### 6. Video Capture Issues

If you're having trouble with video:

```python
cap = cv2.VideoCapture(0)  # 0 for default camera
if not cap.isOpened():
    print("Error: Could not open video source")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame")
        break
        
    cv2.imshow('Video', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
```

### 7. Color Space Conversion Errors

If you encounter errors in color space conversion:

- Make sure the image has the correct number of channels for the conversion
- Check that you're using a valid conversion code

```python
# Convert BGR to HSV (correct)
hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)

# This will fail if image is already grayscale
# First check number of channels
if len(image.shape) == 3:  # Color image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    gray = image  # Already grayscale
```

## Conclusion

This guide covers the essential operations in OpenCV for Python. The library offers many more advanced features for specific applications like face detection, object tracking, and machine learning integration.

For more advanced topics, check out the official OpenCV documentation and tutorials at https://docs.opencv.org/

Remember that computer vision applications often require experimenting with parameters to get the best results for your specific use case. Don't be afraid to try different approaches and adjust settings as needed.