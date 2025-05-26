from flask import Flask, render_template, Response
import cv2
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Initialize camera
camera = cv2.VideoCapture("http://192.168.8.138:8080/video")
# camera = cv2.VideoCapture(0) 


# --- Digital Image Processing Techinques --- #
def process_frame(frame):
    # Resize to max 640px
    height, width = frame.shape[:2]
    max_dim = 640
    scale = max_dim / max(height, width)
    new_size = (int(width * scale), int(height * scale))
    frame = cv2.resize(frame, new_size)

    # Grayscale and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Intensity slicing
    lower, upper = 90, 200
    mask_sliced = cv2.inRange(blurred, lower, upper)

    # Morphological cleanup
    kernel = np.ones((3, 3), np.uint8)
    cleaned = cv2.morphologyEx(mask_sliced, cv2.MORPH_OPEN, kernel)

    # Invert
    result = cv2.bitwise_not(cleaned)

    # Add timestamp
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    x, y = 10, 25
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5 
    thickness = 1

    cv2.putText(result, timestamp, (x, y), font, font_scale, (0, 0, 0), thickness + 2, cv2.LINE_AA)
    cv2.putText(result, timestamp, (x, y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
    
    return result

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        processed = process_frame(frame)

        # Convert to JPEG
        ret, buffer = cv2.imencode('.jpg', processed)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Flask app routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/how_to_use')
def how_to_use():
    return render_template('how_to_use.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)