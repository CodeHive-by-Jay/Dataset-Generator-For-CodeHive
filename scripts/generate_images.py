# generate_images.py

import numpy as np
import cv2
import os

# Generate synthetic images
def generate_images(num_images=10, image_size=(100, 100)):
    # Create the image output directory
    image_dir = os.path.join("data", "synthetic_images")
    os.makedirs(image_dir, exist_ok=True)

    for i in range(num_images):
        # Create a blank image with random colors
        image = np.random.randint(0, 256, (*image_size, 3), dtype=np.uint8)
        
        # Draw random shapes on the image
        for _ in range(5):
            x1, y1 = np.random.randint(0, image_size[0] // 2, size=2)
            x2, y2 = np.random.randint(image_size[0] // 2, image_size[0], size=2)
            color = tuple(np.random.randint(0, 256, size=3).tolist())
            thickness = np.random.randint(1, 5)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        
        # Save the image
        image_path = os.path.join(image_dir, f"image_{i + 1}.png")
        cv2.imwrite(image_path, image)

    print(f"{num_images} synthetic images saved to {image_dir}")
