# Curling Trajectory Detection Dataset

This repository contains a large-scale, comprehensive dataset designed for various computer vision tasks in curling trajectory detection. The dataset includes data for **object detection**, **OBB detection**, **semantic segmentation**, and **object tracking**, all based on high-level curling competition broadcast videos from the Winter Olympics.

## Dataset Overview

The dataset is the result of a post-processing pipeline that includes video cropping, image processing, and data annotation. It is designed to provide systematized support for research in curling trajectory detection using computer vision techniques.

### 1. Object Detection
- **Images**: 5000 frames of curling broadcast videos, each of size 1080x1920.
- **Annotations**: Each image is annotated with bounding boxes in the format `[<class-index> <x> <y> <width> <height>]`, where:
  - `class-index`: 0 (red) or 1 (yellow).
  - `(x, y)`: Normalized center coordinates.
  - `(width, height)`: Normalized width and height of the bounding box.
- **Paths**:
  - Images: `./curling_detect_dataset/images`
  - Labels: `./curling_detect_dataset/labels`
- **Dataset Partitioning**: The dataset can be split automatically into training, validation, and test sets (0.7:0.1:0.2) by running the `Partition_dataset.py` script.

### 2. OBB (Oriented Bounding Box) Detection
- **Images**: 5000 cropped curling images of size 500x500, each containing a single curling stone.
- **Annotations**: Each image is annotated with the four corner points of the oriented bounding box in the format `[<class-index> <x1> <y1> <x2> <y2> <x3> <y3> <x4> <y4>]`, where:
  - `class-index`: 0 (red) or 1 (yellow).
  - `(x1, y1), (x2, y2), (x3, y3), (x4, y4)`: Normalized coordinates of the four corners of the rotated bounding box.
- **Paths**:
  - Images: `./curling_obb_dataset/images`
  - Labels: `./curling_obb_dataset/labels`
- **Dataset Partitioning**: Similar to the object detection task, the dataset can be partitioned by running the `Partition_dataset.py` script.

### 3. Semantic Segmentation
- **Images**: 5000 cropped curling images, each of size 500x500.
- **Annotations**: Segmentation masks (in PNG format) representing the contour of the curling stone.
  - Paths:
    - Original images: `./curling_mask_dataset/images`
    - Segmentation masks: `./curling_mask_dataset/masks`
    - Background-removed images (containing only the curling stone): `./curling_mask_dataset/images_without_background`

### 4. Object Tracking
- **Videos**: 112 video clips of curling matches, each capturing the movement of curling stones from throw to stop, including interactions between multiple stones.
- **Annotations**: Each frame is annotated with `[<class-index> <x> <y> <width> <height> <track-id>]`, where:
  - `class-index`: 0 (red) or 1 (yellow).
  - `(x, y)`: Normalized center coordinates.
  - `(width, height)`: Normalized width and height of the bounding box.
  - `track-id`: Unique identifier for each stone’s movement across frames.
- **Paths**:
  - Videos: `./curling_tracking_dataset/videos`
  - Labels: `./curling_tracking_dataset/labels`

## Usage

This dataset is designed for training and evaluating algorithms for object detection, OBB detection, semantic segmentation, and object tracking. The corresponding scripts and dataset partitioning tools can be used for each task.

## Files

- **Object Detection Dataset**:
  - Images: Located in `./curling_detect_dataset/images`.
  - Labels: Located in `./curling_detect_dataset/labels`.
  
- **OBB Detection Dataset**:
  - Images: Located in `./curling_obb_dataset/images`.
  - Labels: Located in `./curling_obb_dataset/labels`.
  
- **Semantic Segmentation Dataset**:
  - Images: Located in `./curling_mask_dataset/images`.
  - Masks: Located in `./curling_mask_dataset/masks`.
  - Background-removed images: Located in `./curling_mask_dataset/images_without_background`.

- **Object Tracking Dataset**:
  - Videos: Located in `./curling_tracking_dataset/videos`.
  - Labels: Located in `./curling_tracking_dataset/labels`.

## License

This dataset is open-source and available for research purposes. Please cite the dataset if you use it in your work.
