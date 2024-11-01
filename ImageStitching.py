import numpy as np
import cv2
import glob
import imutils

# Helper function to display an image and wait for a keypress
def show_image(window_name, image):
    cv2.imshow(window_name, image)
    key = cv2.waitKey(0)
    if key == ord('q'):  # Optional: Press 'q' to quit early
        cv2.destroyAllWindows()
        exit()
    cv2.destroyWindow(window_name)

# Use glob to find all JPEG images in the 'Images' directory
image_paths = glob.glob("Images/*.jpeg")
print(image_paths)
images = []

# Load each image and add it to the images list
for image in image_paths:
    img = cv2.imread(image)
    if img is None:
        print(f"Error: Image not loaded correctly. Check the file path: {image}")
    else:
        # Resize image to a smaller size if they're too large (commented out)
        # img = imutils.resize(img, width=800)
        images.append(img)

# Check if any images were actually loaded
if not images:
    print("No images were loaded. Check your image directory.")
    exit()

# Create a stitcher object to combine the images
stitcher = cv2.Stitcher.create()

# Attempt to stitch the images together
status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    # Stitching was successful
    cv2.imwrite("stitchedOutput.png", stitched)
    show_image("Stitched Image", stitched)

    # Add a border around the stitched image
    stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    # Convert the image to grayscale and apply thresholding
    grey = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY)

    show_image("Threshold", threshold)

    contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if not contours:
        print("No contours found.")
        exit()
    areaOI = max(contours, key=cv2.contourArea)

    mask = np.zeros(threshold.shape, dtype="uint8")
    x, y, w, h = cv2.boundingRect(areaOI)
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    minRectangle = mask.copy()
    sub = mask.copy()

    while cv2.countNonZero(sub) > 0:
        minRectangle = cv2.erode(minRectangle, np.ones((3, 3), np.uint8), iterations=1)
        sub = cv2.subtract(minRectangle, threshold)
        if cv2.countNonZero(minRectangle) < 0.5 * cv2.countNonZero(mask):  # Stop if area is less than 50% of original
            break

    contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if not contours:
        print("No contours found after erosion.")
        exit()
    areaOI = max(contours, key=cv2.contourArea)

    show_image("Min Rectangle", minRectangle)

    x, y, w, h = cv2.boundingRect(areaOI)

    stitchedOutput = stitched[y:y+h, x:x+w]

    cv2.imwrite("stitchedOutputProcessed.png", stitchedOutput)
    show_image("Stitched Image Processed", stitchedOutput)

    # Optionally, destroy all windows at the end
    cv2.destroyAllWindows()

else:
    print(f"Error during stitching: {status}")
    cv2.destroyAllWindows()
