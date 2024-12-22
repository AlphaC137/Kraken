# Kraken - A Data Exfiltration Tool

Kraken is a Python-based data exfiltration tool that captures user input, screenshots, and audio, encrypts the data, and sends it to a remote server. It includes features like keylogging, screen capturing, and audio recording. This tool is intended for educational purposes and should only be used with explicit consent.

## Features

- **Keylogging**: Captures all keystrokes typed by the user and logs them in a file.
- **Screenshot Capturing**: Takes screenshots of the screen at regular intervals and saves them locally.
- **Audio Recording**: Records system audio and saves the files locally.
- **Persistence**: Makes the script persistent by copying itself to the startup folder, ensuring it runs automatically on system boot.
- **Data Encryption and Exfiltration**: Encrypts captured data using symmetric encryption and sends it to a remote server.

## Dependencies

Before running Kraken, you need to install the following Python packages:

```
pip install pyautogui pyaudio cryptography pynput requests
```
```
pyautogui
```
For screenshot capturing.
```
pyaudio 
```
For audio recording.
```
cryptography 
```
For encrypting captured data.
```
pynput 
```
For keylogging.

requests for sending data to the remote server.

# Usage

**Keylogging**: The tool will capture all typed keys, including alphanumeric keys and special keys (like Enter, Space, etc.).
**Screenshot Capturing**: Screenshots will be taken every 60 seconds and saved as screenshot_TIMESTAMP.png.
**Audio Recording**: Audio will be recorded for 10 seconds and saved as audio_TIMESTAMP.wav.
**Data Exfiltration**: Every minute, the keylogged data will be encrypted and sent to a remote server (you need to replace the URL with your own server URL).

# Running the Script
To start the Kraken tool, simply run the Python script:

```
python kraken.py
```

# Making the Script Persistent

The script will automatically copy itself to the startup folder of the system, making it run every time the system is restarted.

# Data Encryption

Captured keylogs are encrypted using a symmetric key (Fernet encryption). The encrypted data is then exfiltrated to the remote server.

# Security Warning

This tool is designed for educational purposes and should not be used maliciously. Unauthorized use of keylogging or data exfiltration tools is illegal and unethical. Always ensure you have explicit permission before using this script.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
