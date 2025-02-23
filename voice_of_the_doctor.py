import os
import subprocess
import platform
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

# Directly using the API key for ElevenLabs
ELEVENLABS_API_KEY = "sk_d0196edad92ba5859537302301e806959eae754773371c67"  # Replace with your API key

# Function to play the .mp3 file
def play_mp3_file(mp3_filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', mp3_filepath])
        elif os_name == "Windows":  # Windows
            # Use a different command to play mp3 files on Windows
            subprocess.run(['start', '', mp3_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', mp3_filepath])  # Or 'ffplay' as an alternative
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# gTTS text-to-speech
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    play_mp3_file(output_filepath)

# ElevenLabs text-to-speech
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    play_mp3_file(output_filepath)

# Test the functions
#input_text = "Hi this is Ai with Hassan, autoplay testing!"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")
#text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
