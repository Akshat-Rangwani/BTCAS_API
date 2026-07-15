"""
YOLO Detection Module
"""

from ultralytics import YOLO
from config import MODEL_PATH


class BTCASDetector:

    def __init__(self):

        print("Loading BTCAS Model...")

        self.model = YOLO(str(MODEL_PATH))

        print("Model Loaded Successfully")


    def detect(self, video_path):

        results = self.model.track(

             source=video_path,

            conf=0.40,

            imgsz=640,

            persist=True,

            tracker="bytetrack.yaml",

            stream=True,

            save=False

        )

        return results