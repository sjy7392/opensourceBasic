import tkinter as tk
from PIL import Image, ImageTk


class VideoApp:
    def __init__(self, window, window_title, video_source=0, face_net=None, age_net=None, gender_net=None):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = cv2.VideoCapture(video_source)
        self.window.protocol('WM_DELETE_WINDOW', self.destroy)

        self.canvas = tk.Canvas(window, width=self.vid.get(
            cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
