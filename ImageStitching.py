from cv2.gapi import threshold
import numpy as np
import cv2
import glob
import imutils

# Use raw string for Windows paths
image_paths = glob.glob("Images/*.jpeg")
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

    stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    grey = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY)[1]

    cv2.imshow("Threshold", threshold)
    cv2.waitKey(0)

    contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)

    mask = np.zeros(threshold.shape, dtype="uint8")
    x, y, w, h = cv2.boundingRect(areaOI)
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    minRectangle = mask.copy()
    sub = mask.copy()

    while cv2.countNonZero(sub) > 0:
        minRectangle = cv2.erode(minRectangle, np.ones((3, 3), np.uint8))
        sub = cv2.subtract(minRectangle, threshold)

    contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)

    cv2.imshow("min rectangle", minRectangle)
    cv2.waitKey(0)

    x, y, w, h = cv2.boundingRect(areaOI)

    stitchedOutput = stitched[y:y+h, x:x+w]

    cv2.imwrite("stitchedOutputProcessed.png", stitchedOutput)
    cv2.imshow("Stitched Image Processed", stitchedOutput)
    cv2.waitKey(0)

else:
    print(f"Error during stitching: {status}")
