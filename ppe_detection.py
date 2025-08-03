from ultralytics import YOLO
import cv2
import cvzone
import math
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# ======================================
# 🔧 CONFIGURATION
# ======================================
use_webcam = False              # True = webcam, False = single image
image_source = "test.jpg"       # Path to input picture if webcam is False

# Gmail SMTP configuration (use YOUR Gmail App Password here)
sender_email = "simantahzarikaoff@gmail.com"
receiver_email = "simantahzarikaoff@gmail.com"
password = "bzda artr nque jzgy"            # Gmail App Password (16 chars)
smtp_server = "smtp.gmail.com"
smtp_port = 587
subject = "🚨 Security Alert: PPE Violation Detected"

# ======================================
# 📤 EMAIL SENDING FUNCTION
# ======================================
def send_email_alert(message, image_path="output.jpg"):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Attach image
    if os.path.exists(image_path):
        with open(image_path, "rb") as file:
            mime = MIMEBase("image", "jpg", filename=os.path.basename(image_path))
            mime.add_header("Content-Disposition", "attachment", filename=os.path.basename(image_path))
            mime.set_payload(file.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        print("🖼️ Attached", image_path)
    else:
        print("⚠️ No image file found to attach.")

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully with image!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# ======================================
# 🎥 INPUT SOURCE SETUP
# ======================================
if use_webcam:
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
else:
    cap = cv2.VideoCapture(image_source)

if not cap.isOpened():
    print("❌ Failed to open input source. Exiting.")
    exit()

# ======================================
# 🧠 LOAD YOLO MODEL
# ======================================
model = YOLO("best.pt")
classNames = ['helmet', 'no-helmet', 'no-vest', 'person', 'vest']
alert_sent = False

# ======================================
# 🔍 DETECTION LOOP
# ======================================
while True:
    success, img = cap.read()
    if not success:
        print("❌ Failed to read input. Exiting.")
        break

    results = model(img, stream=True)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = round(float(box.conf[0]), 2)
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if conf > 0.5:
                # 🚨 Violation Classes
                if currentClass in ['no-helmet', 'no-vest']:
                    color = (0, 0, 255)
                    if not alert_sent:
                        alert_sent = True
                        message = f"⚠️ Alert! A person without {currentClass.replace('no-', '')} was detected."
                        cv2.imwrite("output.jpg", img)
                        print("🖼️ Image saved to output.jpg")
                        send_email_alert(message, "output.jpg")
                else:
                    color = (0, 255, 0)

                cvzone.putTextRect(
                    img, f"{currentClass} {conf}", (x1, max(35, y1)),
                    scale=1, thickness=1,
                    colorB=color, colorT=(255, 255, 255), colorR=color, offset=5
                )
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)

    cv2.imwrite("output.jpg", img)

    # If not webcam mode → process only one frame and exit
    if not use_webcam:
        break

    cv2.waitKey(1)
