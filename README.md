# Vision-Based Detection of Road Anomalies

A lightweight, real-time road anomaly detection system using classical image processing techniques. Built with Flask (Python), OpenCV, and HTML/CSS.

---

## System Features

### User Interface
* **Responsive Layout:** Clean homepage with modular title elements and intuitive navigation headers.
* **Instructional Guide:** Includes a "How to Use" section with visual examples to guide end users.
* **Live Video Stream:** Features a dedicated anomaly scanning interface displaying a live processed video feed.
* **Mobile Optimization:** Mobile-friendly UI design featuring a fullscreen layout toggle and explicit camera rotation controls.

### Backend Functionality
* **Flask Server:** Acts as the primary web application framework handling routing and template rendering.
* **Live Frame Processing:** Streams live video feeds while simultaneously running real-time frame processing pipelines.
* **IP Camera Integration:** Fully supports fetching live mobile camera feeds via standard network streams (e.g., `/shot.jpg`).
* **Computer Vision Pipeline:** Implements OpenCV-based grayscale conversion, intensity slicing, and binary threshold masking.
* **Post-Processing Filters:** Applies morphological filtering algorithms and appends real-time data overlays (such as timestamps) onto frames.

---

## Technology Stack

| Component | Technology Used |
| :--- | :--- |
| **Backend Framework** | Python (Flask) |
| **Computer Vision** | OpenCV (`opencv-python`) |
| **Frontend** | HTML5, Responsive CSS3 |
| **Streaming Protocol** | IP Camera Network Streaming / Standard USB Webcam |
| **Architecture** | Monolithic / Functional Flask application structure |

---

## Project Structure

```text
├── app.py              # Main Flask server containing OpenCV video processing pipelines
├── templates/          # HTML templates for rendering each application page
├── static/             # Static frontend assets (compiled CSS sheets and graphics)
│   └── images/         # Storage for baseline road anomaly samples (humps, potholes, etc.)
└── .vscode/            # Visual Studio Code editor configuration configurations (Optional)
