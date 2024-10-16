import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer

# تحميل المصنفات المدربة
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# إعداد Streamlit
st.title("Face and Eye Detection App")
st.text("OpenCV with Streamlit")

# دالة لمعالجة الإطارات
def detect_faces_and_eyes(frame):
    img = frame.to_ndarray(format="bgr")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # اكتشاف الوجوه
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # رسم المستطيلات حول الوجوه
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # اكتشاف العيون
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

    return img

# بدء البث من الكاميرا
webrtc_streamer(key="example", video_frame_callback=detect_faces_and_eyes)
