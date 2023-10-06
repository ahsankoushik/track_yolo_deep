import cv2 
import os
import time 

cap = cv2.VideoCapture("/home/koushik/Downloads/20231002_114434.mp4")
ret, frame = cap.read()
shape = frame.shape
print(shape)
frame = cv2.resize(frame,(400,800))
# frame = cv2.resize(frame,(int(shape[1]*.75),int(shape[0]*0.75)))
video_out_path = os.path.join('.', 'out.mp4')
cap_out = cv2.VideoWriter(video_out_path, cv2.VideoWriter_fourcc(*'MP4V'), cap.get(cv2.CAP_PROP_FPS),
                          (frame.shape[1], frame.shape[0]))

# win = cv2.imshow("image",frame)
start = time.time()
f = 0 
while ret:
    frame = cv2.resize(frame,(400,800))
    cv2.imshow("video",frame)
    if(cv2.waitKey(1)==27):
        break
    f+=1
    ret, frame = cap.read()

print("frames:",f,"time:",time.time()-start)
    

cv2.destroyAllWindows()