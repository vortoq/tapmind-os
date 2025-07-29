# VoiceGPT Microapp
import speech_recognition as sr
import openai
from gtts import gTTS
import os

openai.api_key = "your-openai-api-key"

def ask_gpt(prompt):
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']

def speak(text):
    tts = gTTS(text)
    tts.save("reply.mp3")
    os.system("mpg123 reply.mp3")

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

try:
    query = r.recognize_google(audio)
    print("You said:", query)
    reply = ask_gpt(query)
    print("GPT:", reply)
    speak(reply)
except Exception as e:
    print("Error:", e)
