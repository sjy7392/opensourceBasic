import threading
import argparse
import cv2
from video_app import VideoApp

# Global variables
face_proto = "opencv_face_detector.pbtxt"
face_model = "opencv_face_detector_uint8.pb"
age_proto = "age_deploy.prototxt"
age_model = "age_net.caffemodel"
gender_proto = "gender_deploy.prototxt"
gender_model = "gender_net.caffemodel"

# Initialize the models
face_net = cv2.dnn.readNet(face_model, face_proto)
age_net = cv2.dnn.readNet(age_model, age_proto)
gender_net = cv2.dnn.readNet(gender_model, gender_proto)

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--image')
args = parser.parse_args()

# If an image file is given, use it as the video source. Otherwise, use the webcam.
video_source = args.image if args.image else 0

# Start the main loop in a separate thread
threading.Thread(target=VideoApp, args=(
    tk.Tk(), "Tkinter and OpenCV", video_source)).start()
