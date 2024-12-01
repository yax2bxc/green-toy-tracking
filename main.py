from ultralytics import YOLO
import ultralytics
import os

def main():
    model = YOLO('yolov8n.pt')
    # Training here
    # results = model.train(data='./smiski_all/data.yaml',epochs=400,degrees=90,flipud=0.05,project='train',name='smiski_all',scale=.7,save_period=25,lr0=0.001)
    
    # Best trained model so far 
    model = YOLO(r'runs\detect\train65\weights\last.pt')
    model.to('cuda')
    model.predict('./predict_images',save=True, imgsz=640,name='train')

if __name__ == "__main__":
    main()