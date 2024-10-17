from streamlit_webrtc import webrtc_streamer
import cv2

# دالة بسيطة لمعالجة الفيديو
def process_frame(frame):
    img = frame.to_ndarray(format="bgr")
    
    # يمكن هنا تطبيق أي معالجة على الصورة
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    return img  # إرجاع الصورة المعالجة (في هذه الحالة، نعيد الصورة الأصلية)

# بدء البث مع استدعاء دالة المعالجة
webrtc_streamer(key="sample", video_frame_callback=process_frame)
