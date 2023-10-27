import os
import random
import time
import cv2
from ultralytics import YOLO
from meter import Meter
from tracker import Tracker

# change area of interest 
y_start = 380 
y_end = 430

# Change output file name here 
video_out_path = os.path.join('.', 'speed_clac.mp4')

# Change input file name here 
cap = cv2.VideoCapture("/home/koushik/Downloads/20231021_163317.mp4") 

# resize 
size = (400,800)

ret, frame = cap.read()
cap_out = cv2.VideoWriter(video_out_path, cv2.VideoWriter_fourcc(*'MP4V'), cap.get(cv2.CAP_PROP_FPS),
                          size)


# change model here 
model = YOLO("yolov8s.pt")


tracker = Tracker()

colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(20)]

conf = 0.5
start_time = time.time()
while ret:
    start = time.perf_counter()
    frame = cv2.resize(frame,(400,800))
    results = model(frame,verbose=False)

    meter = Meter()
    # frame wise iteration 
    for result in results:
        detections = []
        for r in result.boxes.data.tolist():
            x1, y1, x2, y2  = map(int,r[:4])
            score = r[4]
            if score > conf:
                detections.append([x1, y1, x2, y2, score])

        tracker.update(frame, detections)


        for track in tracker.tracks:
            bbox = track.bbox
            x1, y1, x2, y2 = map(int,bbox)
            track_id = track.track_id
            distance = meter.enter(track_id,x1,y1,x2,y2)
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (colors[track_id % len(colors)]), 3)
            cv2.putText(frame,f"{distance}",(x1,y1-2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)

    end = time.perf_counter()
    fps = int(1/(end-start))
    cv2.line(frame,(0,y_start),(size[0],y_start),(0,255,0),1)
    cv2.line(frame,(0,y_end),(size[0],y_end),(0,255,0),1)
    cv2.putText(frame,str(fps),(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
        
    cv2.imshow("video",frame)
    if(cv2.waitKey(1)==27):
        break
    cap_out.write(frame)
    ret, frame = cap.read()


print("Total time for detection and tracking:",round(time.time()-start_time,2))

cap.release()
cap_out.release()
cv2.destroyAllWindows()