from ultralytics import YOLO
import ultralytics
import requests
import os
import datetime

before = datetime.datetime.now()
model = YOLO("yolov8n.pt")
after = datetime.datetime.now()
print(after-before)