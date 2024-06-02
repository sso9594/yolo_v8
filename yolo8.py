from ultralytics import YOLO

# Load a model
model = YOLO("custom.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="custom.yaml", epochs = 1)  # train the model
