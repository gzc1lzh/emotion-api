# Emotion Recognition API (Clean Version)

This project extracts frames from a video every 3 seconds and analyzes facial emotions using a lightweight FER model.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Deploy on Railway

1. Push this folder to GitHub
2. Go to https://railway.app
3. Create a new project, connect to the repo
4. Use the following start command:

```
uvicorn main:app --host 0.0.0.0 --port 8000
```
