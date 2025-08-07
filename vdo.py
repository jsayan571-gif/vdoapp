import streamlit as st
from PIL import Image
import re
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

# Streamlit page configuration
st.set_page_config(page_title="Video Calling App", layout="centered")
st.title(" Video Calling App using Phone Number")

# Input: Mobile Number (10-digit, India format)
mobile = st.text_input("Enter your mobile number (10 digits):", max_chars=10)

# Function to validate mobile number
def is_valid_mobile(number):
    return re.fullmatch(r"(0|\+91)?[6-9]\d{9}", number)

# Check and proceed if valid
if mobile:
    if is_valid_mobile(mobile):
        st.success(" Mobile number accepted")
        st.subheader(" Start Your Video Call")

        # WebRTC video call setup
        webrtc_streamer(
            key="video_call_with_mobile",
            mode=WebRtcMode.SENDRECV,
            client_settings=ClientSettings(
                media_stream_constraints={"video": True, "audio": True},
                rtc_configuration={
                    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                },
            ),
        )
    else:
        st.error("❌ Invalid number. Please enter a 10-digit number starting with 6-9.")
else:
    st.info("ℹ Enter your mobile number to start the call.")

# Safely load and display image
try:
    image = Image.open("your_image.jpg")
    st.image(image, caption='This is an image', use_column_width=True)
except FileNotFoundError:
    st.warning("⚠ Image file not found. Please make sure 'your_image.jpg' is in the app directory.")
import streamlit as st
from PIL import Image
import re
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

# Streamlit page configuration
st.set_page_config(page_title="Video Calling App", layout="centered")
st.title("📞 Video Calling App using Phone Number")

# Input: Mobile Number (10-digit, India format)
mobile = st.text_input("Enter your mobile number (10 digits):", max_chars=10)

# Function to validate mobile number
def is_valid_mobile(number):
    return re.fullmatch(r"[6-9]\d{9}", number)

# Check and proceed if valid
if mobile:
    if is_valid_mobile(mobile):
        st.success("✅ Mobile number accepted")
        st.subheader("📹 Start Your Video Call")

        # WebRTC video call setup
        webrtc_streamer(
            key="video_call_with_mobile",
            mode=WebRtcMode.SENDRECV,
            client_settings=ClientSettings(
                media_stream_constraints={"video": True, "audio": True},
                rtc_configuration={
                    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                },
            ),
        )
    else:
        st.error("❌ Invalid number. Please enter a 10-digit number starting with 6-9.")
else:
    st.info("ℹ Enter your mobile number to start the call.")

# Safely load and display image
try:
    image = Image.open("your_image.jpg")
    st.image(image, caption='This is an image', use_column_width=True)
except FileNotFoundError:
    st.warning("⚠ Image file not found. Please make sure 'your_image.jpg' is in the app directory.")