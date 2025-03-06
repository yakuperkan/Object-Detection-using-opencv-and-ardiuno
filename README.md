# Object-Detection-using-opencv-and-ardiuno
# AI and Servo Control Project for Defense Industry

This repository contains two main projects developed for defense industry applications:
1. **Object Detection and Tracking** (`object_detection.py`)
2. **Servo Motor Control** (`servo2.ino`)

---

## 🎯 Project 1: Object Detection and Tracking

### 📄 **Description:**
This project uses OpenCV to detect red-colored objects in the camera frame and determine their center coordinates. The identified coordinates are sent to an Arduino to control the servo motor accordingly.

### 🚀 **Technologies Used:**
- **Python**
- **OpenCV**
- **Arduino** (Serial communication)
- **Camera** (Webcam usage)

### 📂 **File:**
- `object_detection.py`: Contains image processing and serial communication code.

### ⚙️ **Installation and Usage:**
1. Install the required libraries:
```bash
pip install opencv-python pyserial numpy
```
2. Connect the Arduino to `COM4` port and set up the servo motor connections.
3. Run the `object_detection.py` file:
```bash
python object_detection.py
```
4. Show a red-colored object to the camera and observe the servo motor movement.

---

## 🔧 Project 2: Servo Motor Control

### 📄 **Description:**
This project allows the servo motor on Arduino to move according to specific coordinates. It works in integration with the image processing project, automatically adjusting the servo motor position when an object is detected.

### 🚀 **Technologies Used:**
- **Arduino IDE**
- **Servo Library**
- **Serial Communication**

### 📂 **File:**
- `servo2.ino`: Contains the Arduino code for controlling the servo motor.

### ⚙️ **Installation and Usage:**
1. Open Arduino IDE and upload the `servo2.ino` file.
2. Ensure the Arduino is connected to the `COM4` port.
3. Check the correct connections of the servo motor (connect to PWM pin).

---

## 📧 Contact
- **Developer:** Yakup Erkan Kaymaz
- **Email:** kaymazyakuperkan@gmail.com

If you encounter any issues while using this project or would like to contribute, feel free to contact me!



