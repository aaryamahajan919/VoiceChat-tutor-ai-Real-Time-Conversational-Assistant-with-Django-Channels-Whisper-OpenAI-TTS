# 🎙️ VoiceChat Tutor – Real-Time AI Speaking Assistant

> A real-time voice assistant web app that listens to your speech, understands it using GPT, and responds back with a natural voice — powered by Django Channels, Whisper, OpenAI, and ElevenLabs.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Django](https://img.shields.io/badge/Django-REST%20API-green?logo=django)
![WebSockets](https://img.shields.io/badge/WebSockets-Realtime-orange?logo=websocket)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT3.5/4-black?logo=openai)
![TTS](https://img.shields.io/badge/Text--to--Speech-ElevenLabs-purple)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 🚀 Demo

```
#demo-link yet to build 
```
🔊 Talk into your mic → 🎧 Hear AI speak back in real-time!

---

## 🧠 What It Does

- 🎤 Takes live voice input via browser microphone
- 🧾 Transcribes audio using [OpenAI Whisper](https://github.com/openai/whisper)
- 💬 Sends transcribed text to [OpenAI GPT-3.5/4](https://platform.openai.com/)
- 🗣️ Converts GPT response into audio using [ElevenLabs TTS](https://www.elevenlabs.io/)
- 🔄 Returns audio over WebSocket in real time

---

## 📦 Tech Stack

| Component | Technology |
|----------|-------------|
| Backend  | Django, Django Channels, Django REST Framework |
| Realtime | WebSockets, Redis |
| STT      | OpenAI Whisper (or local `whisper` model) |
| NLP      | OpenAI GPT-3.5/4 |
| TTS      | ElevenLabs API (or pyttsx3 for offline fallback) |
| Infra    | Redis, Render / AWS EC2 / ngrok (for testing) |

---

## 🗂️ Project Structure

```
voicechat_tutor/
├── backend/                 # Django backend with WebSocket consumers
│   ├── voicechat/           # STT, LLM, TTS processing logic
│   ├── backend/             # Django settings and routing
├── frontend/                # HTML/JS frontend to record voice and play reply
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/voicechat-tutor.git
cd voicechat-tutor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Redis
- On Ubuntu: `sudo apt install redis`
- On Mac: `brew install redis`

### 4. Start Redis
```bash
redis-server
```

### 5. Run Django Dev Server
```bash
python manage.py runserver
```

### 6. Open Frontend
Open `frontend/index.html` in a browser (use Live Server in VS Code or deploy to Netlify).

---

## 📡 WebSocket Flow

```plaintext
Browser Mic 🎙️
     ↓ (binary)
 Django Channels (WebSocket)
     ↓
  Whisper STT
     ↓
OpenAI GPT-3.5
     ↓
ElevenLabs TTS
     ↓
Back to Browser 🔁 (base64 audio)
```

---

## ⚙️ Environment Variables

Create a `.env` file or use system env vars:
```
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
VOICE_ID=your_elevenlabs_voice_id
```

---

## ✅ Features

- ⏱️ Real-time STT and TTS
- 🧠 GPT-4 conversation logic
- 🌐 WebSocket bidirectional flow
- 🐳 Optional Docker deployment
- 📤 Deployable on Render, EC2, or localhost

---

## 🧪 Future Ideas

- Multi-language support
- Emotion-aware voice tone
- Voice-based interview simulator
- Save chat history to S3

---

## 📄 License

MIT License. Feel free to fork and remix.

---

## 🙋‍♂️ About Me

Built with ❤️ by [Aarya Mahajan]
📫 Connect on [LinkedIn](https://www.linkedin.com/in/aarya-mahajan-034191231/)

---

## ⭐️ Support the Project

If you find this helpful, give a ⭐ on GitHub and share it!
