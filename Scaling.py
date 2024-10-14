#Scaling

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import streamlit as st

# Add custom CSS to hide the footer, header
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
# إعداد واجهة المستخدم
st.title("Image Resizer")

# تحميل الصورة
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # قراءة الصورة من الملف المرفوع
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)

    # عرض الصورة الأصلية
    st.image(img, channels="BGR", caption="Original Image")

    # إدخال الأبعاد الجديدة
    new_width = st.number_input("Enter New Width:", min_value=1, value=img.shape[1])
    new_height = st.number_input("Enter New Height:", min_value=1, value=img.shape[0])

    # تعديل حجم الصورة
    if st.button("Resize"):
        # تغيير حجم الصورة
        resized_img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_CUBIC)

        # عرض الصورة المعدلة
        st.image(resized_img, channels="BGR", caption="Resized Color Image", use_column_width=True)

# عرض تعليمات الاستخدام
st.markdown("""
### Instructions:
1. Upload an image file (JPG or PNG).
2. Enter the new dimensions for the image.
3. Click the "Resize" button to see the resized image.
""")
