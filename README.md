# Sign Language Recognition with OpenCV

This project uses Python and OpenCV to recognize hand gestures from a webcam and translate them into sign language (ASL) text. When a hand gesture is detected, the recognized sign is displayed on the screen with a label 'Made by Tuba'.

## Features
- Real-time hand gesture detection using webcam
- Recognition of basic sign language gestures (A-Z or a subset)
- Display of recognized sign on the video feed
- Watermark: 'Made by Tuba'

## Requirements
- Python 3.7+
- OpenCV
- Mediapipe (for hand tracking)
- Numpy

## How to Run
1. Install dependencies:
   ```bash
   pip install opencv-python mediapipe numpy
   ```
2. Run the main script:
   ```bash
   python main.py
   ```

## Note
- This is a basic demo. For best results, use a plain background and good lighting.
- The model can be extended to recognize more gestures or use a trained classifier for full ASL alphabet/words.

---
Made by Tuba
