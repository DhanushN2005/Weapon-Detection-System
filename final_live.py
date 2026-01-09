import torch
import cv2
import time
from pathlib import WindowsPath, PosixPath
import pathlib

# Ensure compatibility with Windows paths
pathlib.PosixPath = WindowsPath

# Load custom YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best_weapon.pt', force_reload=True)
model.eval()

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("🎥 Live weapon recognition started... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to grab frame.")
        break

    # Run YOLOv5 detection on every frame
    results = model(frame)
    detections = results.pandas().xyxy[0]

    if not detections.empty:
        print("🚨 Weapon Detected!")
        for _, row in detections.iterrows():
            x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
            label = f"{row['name']} {row['confidence']:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255), 2, cv2.LINE_AA)
    else:
        print("✅ No weapon detected.")

    # Show the live feed with or without boxes
    cv2.imshow("Live Weapon Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
