# 🎵 Numi AI - Music Studio

Your personal AI Songwriter and Music Concept Generator powered by Google's Gemini API and Streamlit!

## 📋 Features

- **AI-Powered Song Generation** - Generate original songs using Google's Gemini AI
- **Genre Selection** - Choose from multiple genres: Pop, Hip-Hop, Rock, Lo-Fi, Classical, R&B, and EDM
- **Custom Themes** - Specify what your song is about
- **Complete Output** - Get song titles, instrumentation descriptions, and full lyrics
- **User-Friendly Interface** - Beautiful Streamlit web interface
- **Secure API Key Management** - Password-protected API key input

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Gemini API Key (get one free at [aistudio.google.com](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/s24035kwokwaicheong-collab/reimagined-barnacle.git
   cd reimagined-barnacle
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in your browser**
   - The app will automatically open at `http://localhost:8501`

## 🔧 Usage

1. **Enter your Gemini API Key** in the sidebar (Settings)
2. **Select a Genre** from the dropdown menu
3. **Describe your song theme** - what should the song be about?
4. **Click "Generate Song"** and wait for Numi AI to create your track
5. **View the generated lyrics and instrumentation details**

## 📁 Project Structure

```
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## 📦 Dependencies

- **streamlit** - Web application framework
- **google-generativeai** - Google's Generative AI Python SDK

See `requirements.txt` for complete list with versions.

## 🎯 Example

**Input:**
- Genre: Pop
- Theme: A girl's journey to find herself

**Output:**
- Song Title (Generated)
- Instrumentation description
- Full lyrics with Verse 1, Chorus, Verse 2, Chorus, and Outro

## 🔐 Security

- API key is entered via secure password input field
- Keys are not stored in code or version control
- Add `.env` to `.gitignore` if using environment variables

## 🛣️ Roadmap

- [ ] Add mood/emotion selection
- [ ] Configurable song structure (number of verses, bridge sections)
- [ ] Song history/favorites tracking
- [ ] Export to multiple formats (TXT, PDF)
- [ ] Model selection (Gemini Flash vs Pro)
- [ ] Batch song generation
- [ ] User accounts and settings persistence

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🐛 Troubleshooting

**"API Key invalid"**
- Double-check your Gemini API key from [aistudio.google.com](https://aistudio.google.com/app/apikey)
- Ensure you have internet connectivity

**"An error occurred"**
- Check your API rate limits at Google AI Studio
- Verify the API key has proper permissions

**Streamlit not starting**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Try clearing cache: `streamlit cache clear`

## 📧 Support

For issues, questions, or suggestions, please open an [issue](https://github.com/s24035kwokwaicheong-collab/reimagined-barnacle/issues) on GitHub.

## ✨ Credits

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://ai.google.dev/)

---

**Happy Music Making! 🎶**