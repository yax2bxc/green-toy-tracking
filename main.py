from ultralytics import YOLO
import ultralytics
import os

def main():
    model = YOLO('yolov8n.pt')
    # Training here
    # results = model.train(data='./smiski_all/data.yaml',epochs=400,degrees=90,flipud=0.05,project='train',name='smiski_all',scale=.7,save_period=25,lr0=0.001)
    
    # Best trained model so far 
    model = YOLO(r'./runs/detect/train/weights/best.pt')
    model.to('mps')
    results = model.predict('./predict_images',save=False, imgsz=640,name='train')
    for result in results[:5]:
        result.show()
if __name__ == "__main__":
    main()