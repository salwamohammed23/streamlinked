import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import streamlit as st

# Apply background styles
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://img.freepik.com/free-vector/abstract-background_53876-43364.jpg?w=1060&t=st=1685685448~exp=1685686048~hmac=bf06f2136962f77d8fb9a95948390114a68a61622da7713a357e1e359c89618c");
    background-size: cover;
    opacity: 0.9;
}}
[data-testid="stSidebar"] {{
    background-image: url("https://img.freepik.com/free-vector/multicolor-abstract-background_1123-53.jpg?w=740&t=st=1685685659~exp=1685686259~hmac=d3e48585afea7ba2d11c59452ad8edb5c216e26638437d1de8bbe0dec0188f72");
    background-size: cover;
    opacity: 1;
    filter: blur(0.2px);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# إعداد واجهة المستخدم
st.title("Image Resizer and Grayscale Converter")

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
    if st.button("Resize and Convert to Grayscale"):
        # تغيير حجم الصورة
        resized_img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_CUBIC)
        
        # تحويل الصورة إلى اللون الرمادي
        gray_img = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)

        # عرض الصورة المعدلة
        st.image(gray_img, caption="Resized Grayscale Image", channels="GRAY", use_column_width=True)

# عرض تعليمات الاستخدام
st.markdown("""
### Instructions:
1. Upload an image file (JPG or PNG).
2. Enter the new dimensions for the image.
3. Click the "Resize and Convert to Grayscale" button to see the resized grayscale image.
""")
