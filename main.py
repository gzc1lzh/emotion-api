
from fastapi import FastAPI, UploadFile, File
from utils import process_video
import shutil
import os

app = FastAPI()

@app.post("/analyze")
async def analyze_emotions(file: UploadFile = File(...)):
    temp_video_path = f"temp_{file.filename}"
    with open(temp_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = process_video(temp_video_path)
    os.remove(temp_video_path)
    return {"results": results}
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
