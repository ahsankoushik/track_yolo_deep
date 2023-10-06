from ultralytics import YOLO

model = YOLO('yolov8l.pt')

result = model(source="/home/koushik/Downloads/20231002_114434.mp4",show=True)
# result = model.track(source="/home/koushik/Downloads/20231002_114434.mp4",show=True,tracker="bytetrack.yaml")