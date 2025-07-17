# face-mesh
👥 Real-Time Multi-Face Landmark Detection with MediaPipe
This project demonstrates real-time facial landmark detection using MediaPipe's Face Mesh on webcam input. The application uses OpenCV and MediaPipe to detect and draw 468 facial landmarks for up to 2 faces simultaneously.

📸 Demo
<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/23bb4951-6ad0-467c-b85c-00f12ca316fd" />


🧰 Requirements
Install the required Python packages:


pip install mediapipe opencv-python tensorflow numpy pandas
Python 3.7 or higher is recommended.

🚀 How to Run
Clone the repository:


git clone https://github.com/yourusername/face-mesh-multi-face.git
cd face-mesh-multi-face
Run the script:


python face_mesh.py
Press q to exit the webcam feed.

📂 Code Overview

with mp_face.FaceMesh(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_faces=2
) as face:
    ...
Detects up to 2 faces in real-time from webcam.

Uses FACEMESH_TESSELATION to draw 3D-like mesh structure.

Draws 468 landmarks per face with customizable styles.

🎯 Features
Real-time face detection with landmark drawing

Supports multi-face tracking (up to 2 faces, configurable)

Lightweight and efficient — runs on CPU or GPU

Easily customizable for:

Storing coordinates

Triggering events based on facial movement

Integration with ML models or Streamlit

📌 TODO / Ideas
 Save landmark coordinates to CSV

 Add head-pose or blink detection

 Integrate with Streamlit/Flask for web interface

 Face recognition with embedding models

📄 License
This project is licensed under the MIT License.

