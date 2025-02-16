# -*- coding: utf-8 -*-

import os
import random

# Set the number of images for training, validation, and testing sets
num_train = 3464
num_val = 512
num_test = 1024

# Specify the path to the images directory
images_dir = './images'

# Read image filenames and shuffle them
image_files = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith('.jpg')]
random.shuffle(image_files)

# Split into training, validation, and testing sets
train_files = image_files[:num_train]
val_files = image_files[num_train:num_train + num_val]
test_files = image_files[num_train + num_val:num_train + num_val + num_test]

# Get the current script's absolute path
base_path = os.path.abspath('.')

# Function to write absolute paths to a txt file
def write_to_txt(file_list, file_name):
    with open(file_name, 'w') as file:
        for path in file_list:
            # Replace backslashes with forward slashes for consistency and remove './'
            formatted_path = f"{base_path}/{path}".replace('\\', '/').replace('/./', '/')
            file.write(f"{formatted_path}\n")

# Write paths to txt files
write_to_txt(train_files, 'train.txt')
write_to_txt(val_files, 'val.txt')
write_to_txt(test_files, 'test.txt')

# Generate a YAML configuration file
yaml_content = f"""path: {base_path}  # Dataset root directory
train: train.txt  # Train images (relative to 'path')
val: val.txt  # Validation images (relative to 'path')
test: test.txt  # Test images (relative to 'path')

# Number of classes
nc: 2

# Class names
names:
  0: red
  1: yellow
"""

with open('curling_detect.yaml', 'w') as yaml_file:
    yaml_file.write(yaml_content)

print("Files have been generated successfully.")
