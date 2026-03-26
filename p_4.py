import cv2
import mediapipe as mp
import pyautogui
import winsound
x1 = x2 = y1 = y2 = 0
dist_list = []
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
camera = cv2.VideoCapture(0)
while True:
    _, image = camera.read()
    image = cv2.flip(image , 1) #1 flip through the y-axis; 0 x-axis
    fh , fw , _ = image.shape
    rgb_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_image)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark #capturing the first face landmark(capture all the points in the particular face)
        for id , landmark in enumerate(landmarks):
            x = int(landmark.x * fw)
            y = int(landmark.y * fh)
            if id == 43:
                x1 = x
                y1 = y
            if id == 287:
                x2 = x
                y2 = y
            dist = int(((x2-x1)**(2)+(y2-y1)**(2))**(0.5))
            dist_list.append(dist)
            '''if dist > 99:
                cv2.imwrite("D:\image_processing_resume\Selfie.png",image)
                winsound.PlaySound("sound.wav" , winsound.SND_FILENAME)
                cv2.waitKey(100)'''
            
    cv2.imshow("Auto selfi for smiling face", image)
    key = cv2.waitKey(100)
    if  key == 27:
        break
camera.release()
cv2.destroyAllWindows()
print(dist_list[:1000])