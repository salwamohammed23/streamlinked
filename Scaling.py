#Scaling
%%writefile app.py
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import streamlit as st

# إعداد واجهة المستخدم
st.title("Image Resizer and Grayscale Converter")

# تحميل الصورة
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # قراءة الصورة من الملف المرفوع
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv.imdecode(file_bytes, 1)

    # عرض الصورة الأصلية
    st.image(img, channels="BGR", caption="Original Image")

    # إدخال الأبعاد الجديدة
    new_width = st.number_input("Enter New Width:", min_value=1, value=img.shape[1])
    new_height = st.number_input("Enter New Height:", min_value=1, value=img.shape[0])

    # تعديل حجم الصورة
    if st.button("Resize and Convert to Grayscale"):
        # تغيير حجم الصورة
        resized_img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_CUBIC)
        
        # تحويل الصورة إلى اللون الرمادي
        gray_img = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)

        # عرض الصورة المعدلة
        st.image(gray_img, caption="Resized Grayscale Image", use_column_width=True)
        
        # إذا أردت عرض الصورة الملونة المعدلة أيضًا
        # st.image(resized_img, channels="BGR", caption="Resized Color Image")

# عرض تعليمات الاستخدام
st.markdown("""
### Instructions:
1. Upload an image file.
2. Enter the new dimensions for the image.
3. Click the "Resize and Convert to Grayscale" button to see the resized grayscale image.
""")
