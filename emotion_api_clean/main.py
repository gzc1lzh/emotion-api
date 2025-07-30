from fastapi import FastAPI, UploadFile, File
import shutil
import os
from utils import process_video

app = FastAPI()

@app.post("/analyze")
async def analyze_emotion(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_video(temp_path)
    os.remove(temp_path)
    return {"result": result}
