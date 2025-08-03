
# Emotion API

This API extracts frames from uploaded videos every 3 seconds and analyzes the dominant emotion on detected faces using the FER library.

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoint

`POST /analyze` - Upload a video and get timestamped emotion analysis.

## Deploy to Railway

1. Create a new project on [Railway](https://railway.app) and link this repository.
2. Railway installs dependencies from `requirements.txt` automatically.
3. The provided `Procfile` starts the server using `uvicorn` on the port specified by the `PORT` environment variable.
4. Once deployed, send HTTP requests (e.g. from Dify) to `https://<your-railway-url>/analyze`.
