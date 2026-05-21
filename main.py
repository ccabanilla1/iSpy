import cv2
import random
from ultralytics import YOLO

def crop_object(frame, box):
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    crop = frame[y1:y2, x1:x2]
    return crop

def get_average_color(crop):
    average_color = crop.mean(axis=0).mean(axis=0)
    return average_color

def is_pink(average_color):
    blue, green, red = average_color

    if red > blue + 15 and red > green + 15:
        return True
    return False

model = YOLO("yolov8n.pt")
cam = cv2.VideoCapture(0)
cv2.namedWindow("iSpy", cv2.WINDOW_NORMAL)

userprompt = input("What do you spy?")
print("User said:", userprompt)

while True:
    ret, frame = cam.read()
    
    

    if not ret:
        print("Could not read Camera frame")
        break
    
    results = model(frame, verbose=False)
    result = results[0]

    annotated_frame = result.plot()
    cv2.imshow("iSpy", annotated_frame)
     
    key = cv2.waitKey(20) & 0xFF

    if key == ord("s"):
        for box in result.boxes:
            crop = crop_object(frame, box)
            cv2.imshow("Object Crop", crop)
            class_id = int(box.cls[0])
            object_name = result.names[class_id]
            
            if object_name == "person":
                continue
            cv2.imwrite(f"sticker_{object_name}.png", crop)
            
            average_color = get_average_color(crop)
            if is_pink(average_color):
                print("This might be pink!")
            else:
                print("Probably not pink.")
            break

    if key == ord("q"):
        break


cam.release()
cv2.destroyAllWindows()