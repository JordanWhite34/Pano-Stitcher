import numpy as np
import cv2
import glob
import imutils

# Use raw string for Windows paths
image_paths = glob.glob("Images/*.png")
print(image_paths)
images = []

for image in image_paths:
    img = cv2.imread(image)
    if img is None:
        print(f"Error: Image not loaded correctly. Check the file path: {image}")
    else:
        # Resize image to a smaller size if they're too large
        # img = imutils.resize(img, width=800)
        images.append(img)

# Check if images were actually loaded
if not images:
    print("No images were loaded. Check your image directory.")
    exit()

# Create stitcher object
stitcher = cv2.Stitcher.create()

# Attempt stitching
status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    # Stitching was successful
    cv2.imwrite("stitchedOutput.png", stitched)
    cv2.imshow("Stitched Image", stitched)
    cv2.waitKey(0)
else:
    print(f"Error during stitching: {status}")
