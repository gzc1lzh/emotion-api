import cv2
from fer import FER
from datetime import timedelta

def process_video(video_path):
    detector = FER()  # 使用轻量 FER 模型，不使用 mtcnn
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = 3  # seconds
    frame_count = 0
    result = []

    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count * fps * interval)
        ret, frame = cap.read()
        if not ret:
            break

        emotions = detector.detect_emotions(frame)
        if emotions:
            top_emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)
            time_str = str(timedelta(seconds=int(frame_count * interval)))
            result.append(f"{time_str} - {top_emotion}")
        frame_count += 1

    cap.release()
    return result
