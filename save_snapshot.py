import cv2
import csv
import time


def save_snapshot(result_img, data):
    cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") +
                ".jpg", cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR))
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Gender", "Age"])
        writer.writerows(data)
