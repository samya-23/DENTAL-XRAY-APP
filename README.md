# 🦷 Dental X-ray Diagnostic Web App

This is a full-stack web application built for Dobbe AI's Data Science Internship Assignment. The app allows users to:

1. Upload dental X-ray DICOM (`.dcm`/`.rvg`) images.
2. Convert and visualize the image.
3. Detect dental pathologies (e.g., cavities, lesions) using Roboflow's object detection API.
4. Display annotated images with bounding boxes.
5. Generate a diagnostic report using GPT-4 (or mock).

---

## 📦 Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Backend   | FastAPI (Python)   |
| Frontend  | ReactJS (JavaScript) |
| ML Model  | Roboflow Object Detection API |
| LLM       | OpenAI GPT-4 (or dummy) |
| Format    | DICOM (.dcm, .rvg) |
| Extra     | Docker (optional)  |

---

## 📁 Project Structure

