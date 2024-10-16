import cv2
import streamlit as st
import numpy as np

# تحميل المصنفات المدربة
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# إعداد Streamlit
st.title("Face and Eye Detection App")
st.text("OpenCV with Streamlit")

# اختيار الكاميرا
run = st.checkbox('Run')

# إعداد منطقة الفيديو في Streamlit
FRAME_WINDOW = st.image([])

# فتح الكاميرا
cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        st.write("Error: Could not access the camera.")
        break
    
    # تحويل الصورة إلى درجات الرمادي
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # اكتشاف الوجوه
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # رسم المستطيلات حول الوجوه
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # اكتشاف العيون
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

    # عرض الإطار المعالج في Streamlit
    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

else:
    cap.release()
