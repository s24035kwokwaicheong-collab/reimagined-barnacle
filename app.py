import streamlit as st
import google.generativeai as genai

# Website Setup
st.set_page_config(page_title="Numi AI - Music Studio", page_icon="🎵")

# Header
st.title("🎵 Welcome to Numi AI")
st.write("Your personal AI Songwriter and Music Concept Generator!")

# Sidebar for API Key
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")
st.sidebar.markdown("[Get a free API key here](https://aistudio.google.com/app/apikey)")

if api_key:
    # Connect to the AI
    genai.configure(api_key=api_key)
    
    # User Inputs
    st.subheader("Let's make a track")
    genre = st.selectbox("Select a Genre:", ["Pop", "Hip-Hop", "Rock", "Lo-Fi", "Classical", "R&B", "EDM"])
    theme = st.text_input("What is the song about?", "A late night drive through the neon city")
    
    # Generate Button
    if st.button("Generate Song"):
        with st.spinner("Numi AI is hitting the studio..."):
            try:
                # Ask the AI to write the music
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Breaking the long string into multiple lines for readability
                prompt = (
                    f"Write a hit {genre} song about {theme}. "
                    "Include a catchy song title, a brief description of "
                    "how the instruments should sound, and write the lyrics "
                    "(Verse 1, Chorus, Verse 2, Chorus, Outro)."
                )
                
                response = model.generate_content(prompt)
                
                st.success("Track Complete!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("👈 Please enter your Gemini API key in the sidebar to start creating music!")