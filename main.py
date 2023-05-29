import threading
import argparse
import cv2
import tkinter as tk


def main():
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
