import json
import openai
import base64
import whisper
from channels.generic.websocket import AsyncWebsocketConsumer
from backend.voicechat.my_tts_module import text_to_speech  # Make sure this import works correctly

openai.api_key = "YOUR_OPENAI_API_KEY"

class VoiceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            # Save input audio to file
            with open("input.wav", "wb") as f:
                f.write(bytes_data)

            # Transcribe with Whisper
            model = whisper.load_model("base")
            result = model.transcribe("input.wav")
            transcript = result["text"]

            # Get GPT reply
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": transcript}]
            )
            reply_text = response["choices"][0]["message"]["content"]

            # Convert reply to speech (ElevenLabs)
            audio_bytes = text_to_speech(reply_text)
            b64_audio = base64.b64encode(audio_bytes).decode("utf-8")

            # Send result to client
            await self.send(text_data=json.dumps({
                "transcript": transcript,
                "reply": reply_text,
                "audio": b64_audio
            }))