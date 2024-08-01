import os
import numpy as np
import cv2

def film_strippers(path):
    images = []
    allowed_extensions = (".png", ".jpg", ".jpeg", ".bmp")
    for filename in sorted(os.listdir(path)):
        if filename.lower().endswith(allowed_extensions):
            img = cv2.imread(os.path.join(path, filename))
            images.append(img)

    if not images:
        print("No valid image files found in the specified directory.")
        return

    # Resize images to match the size of the first image
    base_shape = images[0].shape[:2]  # height, width
    resized_images = [cv2.resize(img, (base_shape[1], base_shape[0])) for img in images]

    output_image = resized_images[0]
    try:
        for img in resized_images[1:]:
            output_image = np.concatenate((output_image, img), axis=0)
        out_path = os.path.join(path, "film_strippers.png")
        cv2.imwrite(out_path, output_image)
    except ValueError as e:
        print(f"Error concatenating images: {e}")

print("This script merges all image files in the selected folder into a single image.")
print("If the images differ in size, they will be resized to match the dimensions of the first image. \n")
film_strippers(input("Enter the full path to the folder:"))
print("Done! Filmstrip Generated.")