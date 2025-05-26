VISION-BASED DETECTION OF ROAD ANOMALIES
A lightweight, real-time road anomaly detection system using classical image processing techniques.
Built with Flask (Python), OpenCV, and HTML/CSS.

🔍 SYSTEM FEATURES

👤 USER INTERFACE
• Responsive homepage with title and navigation
• "How to Use" guide with visual examples
• Real-time anomaly scan page with video processing feed
• Mobile-optimized UI with fullscreen toggle and rotate icon

🛠 BACKEND FUNCTIONALITY
• Flask-based web server for routing and rendering
• Live video feed streaming with real-time frame processing
• IP camera integration via /shot.jpg for mobile scanning
• OpenCV-based grayscale conversion, intensity slicing, and binary masking
• Morphological filtering and timestamp overlays

🛠 TECHNOLOGY STACK
Backend:     Python (Flask), OpenCV
Frontend:    HTML5, CSS3 (responsive design)
Streaming:   IP Camera (mobile app or USB webcam)
Framework:   Functional Flask (no blueprint architecture)

📁 PROJECT STRUCTURE

Key Files & Folders:
• app.py                  - Main Flask app with OpenCV video processing
• templates/              - HTML templates for each page
• static/                 - CSS files and images used in frontend
• static/images/          - Road anomaly sample images (e.g., humps, potholes)
• .vscode/                - Editor settings (optional)

⚙️ SETUP & RUN

Python version required: 3.7+

1. Install dependencies:
   pip install flask opencv-python

2. Ensure you have a mobile camera/IP Webcam app installed and running. Set the stream mode to /shot.jpg.

3. Run the application:
   python app.py

4. Visit in your browser:
   http://127.0.0.1:5000

5. Access live scan from any device on the same Wi-Fi network using the host's local IP.

⚠️ LIMITATIONS
• Not optimized for low-light or nighttime detection
• No database or result logging
• Detection depends on camera resolution and lighting
• Detection is based purely on classical image processing (no ML)

🚀 FUTURE IMPROVEMENTS
• Add dynamic lighting compensation
• Include detection result logging and classification
• Introduce sensor fusion (GPS, gyroscope, etc.)
• Upgrade to real-time object detection using ML (YOLO, etc.)

👨‍💻 DEVELOPER
John Carlo E. Nas
📧 johncarlonas@gmail.com
