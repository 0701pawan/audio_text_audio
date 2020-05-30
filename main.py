import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
r=sr.Recognizer()
with sr.AudioFile("Input2.wav") as source:
    audio = r.record(source)
    try:
        text1=r.recognize_google(audio)
        # print("working on....")
        # print(text)
        au='speech.mp3'
        language='en'
        sp=gTTS(text=text1,lang=language,slow=False)
        sp.save(au)
        playsound(au)
    except Exception as e:
        print(e)