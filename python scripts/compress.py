import os
from PIL import Image

def compress_image(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        # Convert to RGB if the image mode is RGBA
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(output_path, optimize=True, quality=quality)

def compress_images_in_folder(input_folder, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)

                output_dir = os.path.dirname(output_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                compress_image(input_path, output_path, quality)

input_folder = '/Users/macbookpro/Desktop/web/images'
output_folder = '/Users/macbookpro/Desktop/web/compressed images'

compress_images_in_folder(input_folder, output_folder, quality=85)
