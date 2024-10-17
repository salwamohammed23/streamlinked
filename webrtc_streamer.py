import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import asyncio

st.title("My Streamlit App")
st.write("Hello world")

class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

async def send_data(transport, data):
    try:
        if transport is None:
            raise ValueError("Transport is not initialized.")
        transport.sendto(data)
        print("Data sent:", data)
    except Exception as e:
        print(f"Error sending data: {e}")

def custom_exception_handler(loop, context):
    print(f"Exception caught: {context['exception']}")

async def main(transport):
    # هنا يمكنك إضافة أي عمليات غير متزامنة أخرى تحتاجها
    await send_data(transport, b"Hello from Streamlit!")

ctx = webrtc_streamer(key="sample", video_processor_factory=VideoProcessor)

if ctx.video_processor:
    ctx.video_processor.threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
    ctx.video_processor.threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=100)

# إعداد الحلقة الرئيسية لـ asyncio
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(custom_exception_handler)
    
    try:
        # هنا يمكن استبدال None بنقل فعلي إذا كان لديك إعدادات للنقل
        transport = None
        loop.run_until_complete(main(transport))
    finally:
        loop.close()
