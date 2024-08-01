## Usage:

1. Install dependencies:
   ```bash
   pip install numpy
   pip install opencv-python
   ```
    **Note:** Python 3 does not support the `CV2` library. You must use `opencv-python`.

2. Ensure your images are sorted alphanumerically in one folder. The supported file formats are `.png`, `.jpg`, `.jpeg`, or `.bmp`.

3. Run the script.

## Purpose:
The `film_strippers` script merges all image files into a single image, stacked vertically. This is useful for creating UI filmstrips. If the images differ in size, they will all be resized to match the dimensions of the first image.