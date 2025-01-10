import streamlit as st
import qrcode
import os
from PIL import Image

# Temporary storage directory for files
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Streamlit App
st.title("File to QR Code Sharing Platform")

# File Upload
uploaded_file = st.file_uploader("Upload a file to share", type=None)

if uploaded_file:
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"File saved: {uploaded_file.name}")

    # Generate QR Code
    file_url = f"http://localhost:8501/{file_path}"  # Replace with your actual domain
    qr = qrcode.make(file_url)
    
    # Save QR Code image
    qr_path = os.path.join(UPLOAD_DIR, f"{uploaded_file.name}_qr.png")
    qr.save(qr_path)
    
    # Display QR Code
    st.image(qr_path, caption="Scan to Download", use_column_width=True)
    st.write("Share the QR code above to allow others to download the file.")
    st.write(f"Direct Download Link: [Download {uploaded_file.name}]({file_url})")

# Clean up old files (optional)
if st.button("Clear all files"):
    for file in os.listdir(UPLOAD_DIR):
        os.remove(os.path.join(UPLOAD_DIR, file))
    st.success("All uploaded files and QR codes cleared!")