from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils import convert_dcm_to_jpg
import requests
import openai
import base64

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

ROBOFLOW_URL = "https://detect.roboflow.com/adr/6"
ROBOFLOW_API_KEY = "your_roboflow_api_key"
OPENAI_API_KEY = "your_openai_api_key"

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    img_buffer = convert_dcm_to_jpg(file.file)

    response = requests.post(
        f"{ROBOFLOW_URL}?api_key={ROBOFLOW_API_KEY}&confidence=30&overlap=50",
        files={"file": ("image.jpg", img_buffer, "image/jpeg")},
    )
    prediction = response.json()

    prompt = f"""
You are a dental radiologist. Based on the image annotations below, write a concise diagnostic report:
{prediction}
"""
    openai.api_key = OPENAI_API_KEY
    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )

    return {
        "prediction": prediction,
        "report": gpt_response["choices"][0]["message"]["content"]
    }
