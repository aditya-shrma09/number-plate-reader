import streamlit as st

st.set_page_config(
    page_title="Number Plate Reader",
    page_icon="🚗",
    layout="wide"
)

st.title("Number Plate Reader")
st.write("Upload a vehicle image and detect its license plate.")

img = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

left, right = st.columns(2)

with left:
    st.subheader("Uploaded Image")

    if img:
        st.image(img, use_container_width=True)
    else:
        st.info("Upload an image to begin.")

with right:
    st.subheader("Detection Result")

    st.empty()

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Detect Plate", use_container_width=True):
        st.success("Detection will appear here.")

with col2:
    st.button("🗑 Clear", use_container_width=True)

st.divider()

st.subheader("Detected Plate")

plate_placeholder = st.empty()

plate_placeholder.info("Detected plate will appear here.")

st.subheader("Extracted Text")

st.code("Waiting for detection...", language="text")

st.progress(0)

st.caption("Built using OpenCV + OCR + Streamlit")