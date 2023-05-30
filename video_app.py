import tkinter as tk
import cv2
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

        self.btn_snapshot = tk.Button(
            window, text="Snapshot/CSV", width=50, command=self.snapshot, relief="flat")
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.delay = 15
        self.update()

        self.window.resizable(False, False)
        self.window.mainloop()
