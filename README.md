
# Image Stitching in Python with OpenCV

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
  - [Input Images](#input-images)
  - [Stitched Output](#stitched-output)
  - [Processed Output](#processed-output)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Image stitching is a technique that combines multiple images with overlapping fields of view to produce a panoramic or high-resolution image. This project leverages Python's OpenCV library to perform seamless image stitching, making it accessible for photographers, developers, and hobbyists to create stunning panoramas effortlessly.

## Features

- **Automatic Image Stitching**: Combines multiple images into a single panoramic image with minimal user intervention.
- **Post-processing Enhancements**: Refines the stitched image with borders, thresholding, and contour detection to ensure a polished output.
- **Interactive Image Display**: Allows users to visualize each step of the stitching process.
- **Error Handling**: Provides informative error messages to guide users in case of issues.

## Prerequisites

Ensure familiarity with:
- Python programming
- Image processing concepts
- Installing Python packages

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/image-stitching-python.git
   cd image-stitching-python
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies:**
   - OpenCV (`opencv-python`)
   - imutils
   - NumPy
   - glob (Standard Library)

## Usage

1. **Prepare Your Images**
   - Create a directory named `Images` in the project root.
   - Place all `.jpeg` images you want to stitch inside the `Images` folder.
   - Ensure consecutive images have overlapping regions for effective stitching.

   Directory structure:
   ```plaintext
   image-stitching-python/
   ├── Images/
   │   ├── image1.jpeg
   │   ├── image2.jpeg
   │   └── image3.jpeg
   ├── image_stitching.py
   └── README.md
   ```

2. **Run the Stitching Script**

   ```bash
   python image_stitching.py
   ```

   - The script processes and stitches images, displaying intermediate results.
   - Press any key to proceed to the next image window.
   - Press `q` to exit the script early.

3. **Output**
   - The final stitched image is saved as `stitchedOutputProcessed.png` in the project root.
   - Intermediate outputs, such as `stitchedOutput.png` and processed images, are also saved for reference.

## Example

### Input Images

Place your input images in the `Images` folder.

### Stitched Output

The script generates a stitched panorama after successful stitching.

### Processed Output

Post-processing refines the stitched image by cropping and enhancing the panorama.

*Note*: Replace `path/to/...` with actual paths to your example images.

## Troubleshooting

Common issues and solutions:

1. **No Images Loaded**
   - **Issue**: "No images were loaded. Check your image directory."
   - **Solution**: Ensure the `Images` folder contains `.jpeg` images. Verify file paths and image formats.

2. **Stitching Errors**
   - **Issue**: Error status code during stitching.
   - **Solution**:
     - Verify all images have overlapping regions.
     - Ensure images are clear, with minimal repetitive patterns.
     - Check OpenCV’s stitcher documentation for status codes.

3. **Poorly Aligned Panoramas**
   - **Issue**: Visible seams or misalignments in the panorama.
   - **Solution**:
     - Ensure consistent lighting and exposure.
     - Capture images from the same viewpoint with minimal parallax.
     - Resize large images to reduce processing time and memory usage.

4. **High Memory Usage with Large Images**
   - **Issue**: Large images consume significant memory.
   - **Solution**: Uncomment and adjust the resizing line in the script:

     ```python
     img = imutils.resize(img, width=800)
     ```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

1. **Fork the Repository**
2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the MIT License.

*Disclaimer*: This project is intended for educational purposes. Ensure you have the right to use and modify the images you process with this script.
