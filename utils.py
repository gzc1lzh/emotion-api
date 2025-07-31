
import cv2
import numpy as np
from fer import FER

def process_video(video_path):
    detector = FER(mtcnn=False)
    results = []
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * 3) if fps else 90

    frame_index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_index % frame_interval == 0:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            emotion, score = detector.top_emotion(rgb_frame)
            timestamp = frame_index / fps if fps else frame_index / 30
            minutes = int(timestamp // 60)
            seconds = int(timestamp % 60)
            time_str = f"{minutes:02}:{seconds:02}"
            results.append(f"{time_str} - {emotion if emotion else '未知'}")
        frame_index += 1
    cap.release()
    return results
