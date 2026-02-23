import cv2
import os
from .plate_detector import PlateDetector
from .text_extractor import TextExtractor
from .database_manager import DatabaseManager
from .config import INPUT_FOLDER, OUTPUT_FOLDER

detector = PlateDetector()
ocr = TextExtractor()
db = DatabaseManager()

for img_name in os.listdir(INPUT_FOLDER):

    img_path = os.path.join(INPUT_FOLDER, img_name)
    image = cv2.imread(img_path)

    plates = detector.detect(image)

    for plate_img, (x1,y1,x2,y2) in plates:
        plate_number = ocr.extract(plate_img)

        if plate_number:
            vehicle = db.get_vehicle_info(plate_number)

            if vehicle:
                label = f"{plate_number} | {vehicle['owner_name']}"
            else:
                label = f"{plate_number} | Not Found"

            cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(image,label,(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    save_path = os.path.join(OUTPUT_FOLDER, img_name)
    cv2.imwrite(save_path, image)
    print("Processed:", img_name)