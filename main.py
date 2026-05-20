import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("iSpy", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cam.read()

    if not ret:
        print("Could not read Camera frame")
        break

    cv2.imshow("iSpy", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()