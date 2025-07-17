import numpy as np 
import os
import pandas as pd
import tensorflow as tf
import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils

mp_face = mp.solutions.face_mesh
cap=cv2.VideoCapture(0)
with mp_face.FaceMesh(min_detection_confidence=0.7,min_tracking_confidence=0.7,max_num_faces=2) as face:
    while True:
        ret,frame=cap.read()
    
        
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame.flags.writeable=False  
        result=face.process(image)
        frame.flags.writeable=True
        image=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.DrawingSpec(
                        color=(255, 255, 255), thickness=1, circle_radius=1
                    )
                )
        

        cv2.imshow("webcam",image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()