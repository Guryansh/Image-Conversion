import os
import cv2

image_folder = "output_images"
output_folder = "output_scaled_images"
scaling_factor = 0.5
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
os.makedirs(output_folder, exist_ok=True)
for image_file in image_files:
    image = cv2.imread(os.path.join(image_folder, image_file))
    scaled_down_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    cv2.imwrite(os.path.join(output_folder, image_file), scaled_down_image)

