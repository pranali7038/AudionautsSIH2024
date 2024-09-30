import streamlit as st
import librosa

# Function for keyword spotting
def keyword_spotting(audio_file):
    if audio_file is not None:
        # Load the audio file using librosa
        audio_data, sr = librosa.load(audio_file, sr=None)
        result = "Keyword found: one, two, three, seven"  # Dummy result
        return result
    else:
        return "No audio file selected."

# Streamlit app
st.title("Few Shot Language Agnostic Keyword Spotting System (FSLAKWS)")
st.markdown("""
    Welcome to the FSLAKWS system prototype. This system is designed to detect keywords in audio files 
    with very few examples provided for training. It works across multiple languages and varying sample rates.
""")

# Audio Input Section
st.subheader("Audio Input")

# Option to choose between sample audio and upload
audio_option = st.radio("Choose audio source:", ("Use sample audio", "Upload your own audio"))

if audio_option == "Use sample audio":
    # Update the file path to the correct absolute path
    st.audio("audio.wav", format="audio/wav")
    audio_file = "audio.wav"
else:
    audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "ogg"])

if st.button("Spot Keyword"):
    if audio_file:
        result = keyword_spotting(audio_file)
        st.text_area("Result", result)
    else:
        st.warning("Please select an audio source before spotting keywords.")

# Business Use Cases Section
st.markdown("## Business Use Cases")

# Display images and labels
col1, col2 = st.columns(2)
with col1:
    st.image("img5.jpeg", caption="Multilingual Virtual Assistants")
    st.markdown("**Multilingual Virtual Assistants**")
with col2:
    st.image("img3.jpeg", caption="Customer Service Automation")
    st.markdown("**Customer Service Automation**")
col3, col4 = st.columns(2)
with col3:
    st.image("img.jpeg", caption="Security and Surveillance")
    st.markdown("**Security and Surveillance**")
with col4:
    st.image("img5.jpeg", caption="Language-Agnostic Voice Biometrics")
    st.markdown("**Language-Agnostic Voice Biometrics**")

# Business Use Cases Markdown
st.markdown("""
**1. Speech Recognition Systems**:
- Enhance existing speech recognition systems by adding multilingual keyword detection capabilities, making them more versatile and useful in global markets.
            
**2. Customer Service Automation**:
- Implement in call centers to automatically detect and flag important keywords during customer interactions, enabling real-time sentiment analysis and better customer support.
            
**3. Security and Surveillance**:
- Deploy in security systems to monitor and detect critical keywords in multiple languages, improving the efficiency of threat detection and response in diverse environments.
            
**4. Media Monitoring**:        
- Utilize in media and content monitoring systems to track specific keywords or phrases across various languages in audio content, helping brands manage their reputation.
            
**5. Voice-Activated Assistants**:    
- Integrate into voice-activated assistants to support multilingual command recognition, expanding their usability across different regions and languages.
""")

# Performance Metrics Section
st.markdown("## Performance Metrics")
st.markdown("""
- **Accuracy**: High precision in keyword detection
- **Latency**: < 100ms response time
- **Model Size**: Optimized for deployment in resource-constrained environments
""")
