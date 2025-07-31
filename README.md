
# Emotion API

This API extracts frames from uploaded videos every 3 seconds and analyzes the dominant emotion on detected faces using the FER library.

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoint

`POST /analyze` - Upload a video and get timestamped emotion analysis.
