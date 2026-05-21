import cv2
import random
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # get the AI brain ready


cam = cv2.VideoCapture(0)
cv2.namedWindow("iSpy", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cam.read()

    if not ret:
        print("Could not read Camera frame")
        break
    
    results = model(frame, verbose=False)
    
    annotated_frame = results[0].plot()
    cv2.imshow("iSpy", annotated_frame)
    
    result = results[0]
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()