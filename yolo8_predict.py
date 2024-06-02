from ultralytics import YOLO

# Load a model
model = YOLO('runs/detect/train3/weights/best.pt')  # load a custom model

# Predict with the model
results = model('test/')  # predict on an image