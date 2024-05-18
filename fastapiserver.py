import time
import cv2
import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ultralytics import YOLO
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

video_cap = cv2.VideoCapture("videos/video.mp4")
model = YOLO("yolov8s.pt")

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture("videos/video.mp4")

    def __del__(self):
        self.video.release()

    def open_video(self):
        self.video = cv2.VideoCapture("videos/video.mp4")

    def processing_frame(self, frame):
        blur_frame = cv2.GaussianBlur(frame, (7, 7), 0)
        detections = model(blur_frame)[0]

        for data in detections.boxes.data.tolist():
            confidence, class_index = data[4:6]

            if float(confidence) < 0.6:
                continue

            if class_index == 0:
                x_min, y_min, x_max, y_max = int(data[0]), int(data[1]), int(data[2]), int(data[3])
                x, y = (x_min + x_max) / 2, (y_min + y_max) / 2
                if -y > ((52 / 77) * x - (75200 / 77)):
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 225, 0), 2)
                else:
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)

        cv2.line(frame, (380, 720), (1150, 200), (0, 0, 255), 3)
        return frame

    def get_frame(self):
        try:
            success, frame = self.video.read()
            if not success:
                self.open_video()
                return self.get_frame()
            processed_frame = self.processing_frame(frame)
            cut_frame = cv2.resize(processed_frame, (1270, 720))
            ret, jpeg = cv2.imencode('.jpg', cut_frame)
            return jpeg.tobytes()
        except Exception as e:
            print(f"Error: {e}")
            self.open_video()
            return self.get_frame()

def gen(camera):
    c = 1
    start = time.time()
    while True:
        start_1 = time.time()
        if c % 20 == 0:
            end = time.time()
            FPS = 20 / (end - start)
            print(f"FPS_avg: {FPS:.6f}")
            start = time.time()
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        end_1 = time.time()
        FPS = 1 / (end_1 - start_1)
        print(f"FPS: {FPS:.6f}")
        c += 1

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.get('/video_feed')
def video_feed():
    return StreamingResponse(gen(VideoCamera()), media_type="multipart/x-mixed-replace;boundary=frame")

if __name__ == '__main__':
    uvicorn.run("fastapiserver:app", port=5050, access_log=False)