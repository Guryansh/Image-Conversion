import cv2

import os

image_folder = "images"
output_folder = "output_images"
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
os.makedirs(output_folder, exist_ok=True)
for image_file in image_files:
    image = cv2.imread(os.path.join(image_folder, image_file))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(output_folder, image_file), image)
