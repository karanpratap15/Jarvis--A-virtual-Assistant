import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import time
from google import genai

# recognizer=sr.Recognizer()

def speak(text):
    engine=pyttsx3.init()  
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = genai.Client()

    response = client.models.generate_content(
    model="gemini-2.5-flash", # Highly recommended: incredibly fast, smart, and completely free-tier eligible
    contents=command
)

# Extract just the text from the response object
    return response.text


def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        try:
            song=c.lower().split(" ")[1]
            link= musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        except(IndexError,KeyError):
            print("Song is not present in your Library")
            speak("Song not found")

    else:
        output=aiProcess(c)
        speak(output)
    


if __name__=="__main__":
    speak("Initializing Jarvis....")
    print("Jarvis is active. Say 'Jarvis' to wake me up!")



    while True:
        #listen for wake word "Jarvis"
        #obtain audio from microphone
        r=sr.Recognizer()

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("\nListening for Wake word...")
                audio=r.listen(source, timeout=3,phrase_time_limit=2)

            word=r.recognize_google(audio)
            if "jarvis" in word.lower():
                # print("Wake word Detected")
                speak("How can I help you?")

                
              
                #listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print("Jarvis Activated! Listenig  for command...")
                    audio=r.listen(source,timeout=5,phrase_time_limit=5)
                    command=r.recognize_google(audio)
                    
                    processCommand(command)


        except sr.UnknownValueError:
            pass  # Ignore unintelligible noise silently
        except sr.WaitTimeoutError:
            pass  # Keep looping silently if no one talks
        except Exception as e:
            print(f"An unexpected error occurred: {e}")