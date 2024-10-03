from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
with client.audio.speech.with_streaming_response.create(
  model="tts-1",
  voice="echo",
  input="Today is a wonderful day to build something people love!"
) as response:
response.stream_to_file(speech_file_path)
