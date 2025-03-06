import cv2
import numpy as np
import serial
import time

# Start serial communication
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=1)
time.sleep(2)  # Allow for starting the ardiuno

# Start camera(Webcam)
cap = cv2.VideoCapture(0)

def write_read(coords):
    try:
        arduino.write(bytes(coords + '\n', 'utf-8'))  # Send coordinates
        time.sleep(0.1)  # Wait for response the ardiuno
        data = arduino.readline().decode('utf-8').strip()  # Read the response
        return data
    except Exception as e:
        print(f"Error serial communication: {e}")
        return None

while True:
    ret, frame = cap.read()
    if not ret:
        break



    # Convert the image from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the HSV range for the red color
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine the two masks
    mask = mask1 + mask2

    # Find contour
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find largest contour and calculate center of gravity of frame
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # Mark center of gravity
            cv2.circle(frame, (cX, cY), 5, (0, 255, 0), -1)
            cv2.putText(frame, f"Centroid ({cX}, {cY})", (cX - 25, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Send coordinates to the Ardiuno
            coords = f"{cX},{cY}"
            response = write_read(coords)
            print(f"Sent: {coords}, Received: {response}")

    # Show the image
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # If press the 'q',the program will finish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
