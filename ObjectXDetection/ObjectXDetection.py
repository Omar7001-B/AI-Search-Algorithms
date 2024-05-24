import cv2
import os
import numpy as np

# Paths to the model files
model_weights = 'MobileNetSSD_deploy.caffemodel'
model_config = 'MobileNetSSD_deploy.prototxt'

# Load the pre-trained model
net = cv2.dnn.readNetFromCaffe(model_config, model_weights)

# List of class labels MobileNet SSD was trained to detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

def detect_objects(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]

    # Preprocess the image: resize and normalize
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    # Set the input to the pre-trained model
    net.setInput(blob)

    # Run forward pass to get the detections
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Only consider detections with confidence above a threshold
        if confidence > 0.2:
            # Get the class label
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            # Compute the bounding box coordinates
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Draw the bounding box and label on the image
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, f"{label}: {confidence:.2f}", (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the output image
    cv2.imwrite(output_path, image)

# Directory paths
input_folder = 'Input'
output_folder = 'Output'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, filename)
        detect_objects(input_image_path, output_image_path)
        print(f"Processed {filename}")
