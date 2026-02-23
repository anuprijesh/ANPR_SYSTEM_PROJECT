from ultralytics import YOLO
import cv2
from .config import MODEL_PATH 


class PlateDetector:
    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def detect(self, image):
        results = self.model(image)[0]
        plates = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            plate = image[y1:y2, x1:x2]
            plates.append((plate, (x1, y1, x2, y2)))

        return plates