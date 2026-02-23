🚗 Automatic Number Plate Detection & Recognition (ANPR)

This project is an AI-powered Automatic Number Plate Detection & Recognition system that detects vehicle number plates from images, extracts the plate number using OCR, and fetches the corresponding vehicle owner details from a database.
It demonstrates how Computer Vision and Deep Learning can be applied to real-world traffic monitoring and vehicle identification systems.

🚀 Overview

Automatic Number Plate Recognition (ANPR) systems are widely used in:

Traffic monitoring
Parking management
Toll collection systems
Security and surveillance
Vehicle tracking

This project detects number plates using a trained YOLO model, reads the plate text using OCR, and matches it with stored vehicle records.

🧠 Key Features

✅ Number plate detection using YOLO
✅ Text extraction using OCR (EasyOCR)
✅ Vehicle owner lookup from database
✅ Bounding box and label visualization
✅ Automatic result saving
✅ Modular and scalable project structure

🛠 Tech Stack

Python
YOLO (Ultralytics)
OpenCV
EasyOCR
Pandas
NumPy

1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Add YOLO model
Place your trained .pt file inside:
models/yolo_weight/

3️⃣ Add test images
Put vehicle images in:
input_images/

4️⃣ Run the system
python -m src.main
