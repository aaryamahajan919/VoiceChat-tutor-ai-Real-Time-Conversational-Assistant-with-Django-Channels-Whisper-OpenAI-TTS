# voicechat/my_tts_module.py

from elevenlabs import generate, set_api_key

# Set your ElevenLabs API key here
set_api_key("YOUR_ELEVENLABS_API_KEY")

def text_to_speech(text):
    """Generate speech audio from text using ElevenLabs and return raw audio bytes."""
    audio = generate(
        text=text,
        voice="Rachel",  # Change to your preferred voice
        model="eleven_monolingual_v1"
    )
    return audio  # This is in bytes