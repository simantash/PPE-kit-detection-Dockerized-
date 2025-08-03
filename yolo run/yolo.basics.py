from ultralytics import YOLO
import cv2

model=YOLO('../Yolo-weights/yolov8l.pt')
results = model("images/1.png", show=True)
cv2.waitkey(2000)
