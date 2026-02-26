import time
import os
from datetime import datetime
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput

# ===== Create capture folder =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAPTURE_DIR = os.path.join(BASE_DIR, "captures")
os.makedirs(CAPTURE_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

IMAGE1 = os.path.join(CAPTURE_DIR, f"{timestamp}_image1.jpg")
IMAGE2 = os.path.join(CAPTURE_DIR, f"{timestamp}_image2.jpg")
VIDEO_FILE = os.path.join(CAPTURE_DIR, f"{timestamp}_video.h264")

picam2 = Picamera2()

# ===== STILL MODE =====
photo_config = picam2.create_still_configuration()
picam2.configure(photo_config)
picam2.start()

print("Capturing first image...")
picam2.capture_file(IMAGE1)
time.sleep(2)

print("Capturing second image...")
picam2.capture_file(IMAGE2)
time.sleep(2)

picam2.stop()

# ===== VIDEO MODE =====
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
picam2.start()

print("Recording 10-second video...")

encoder = H264Encoder()
output = FileOutput(VIDEO_FILE)

picam2.start_recording(encoder, output)
time.sleep(10)
picam2.stop_recording()

picam2.stop()

print("✅ Capture Complete!")
print("Saved in:", CAPTURE_DIR)
