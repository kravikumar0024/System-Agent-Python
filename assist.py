import pyttsx3 as p  # This package we'll Convert Speech To text
import speech_recognition as sr  # This We'll access the Speaker
from Salaar import infow  # class import
import webbrowser

# Initialize the text-to-speech engine
engine = p.init()
engine.setProperty('rate', 130)  # Set the speed of voice
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[1].id)  # Set the voice

def speak(text):
    engine.say(text)
    engine.runAndWait()
def main():
    r = sr.Recognizer()
    speak("hi, how can i help you!")
    print("hi, how can i help you!")
    
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, 1.2)  # Adjust for ambient noise
            try:
                audio = r.listen(source)
                text2 = r.recognize_google(audio)
                print(text2)
            except sr.UnknownValueError:
                speak("Sorry, I did not understand that.")
                continue
            except sr.RequestError as e:
                speak(f"Could not request results from Google Speech Recognition service; {e}")
                continue
        if  "open" and "Google" in text2:
            url = "https://www.google.com"
            webbrowser.open(url)
        elif "open" and "WhatsApp" in text2:
            url = "https://wa.me/917013634297?"
            webbrowser.open(url)
        elif "open" and "YouTube" in text2:
            url = "https://www.youtube.com/"
            webbrowser.open(url) 
        elif "open" and "Instagram" in text2:
            url="https://www.instagram.com/bheemsen_ravi/"
            webbrowser.open(url)
        elif "play" in text2 or "video" in text2:
            obj = infow()
            obj.play_video(text2)
        elif "information" in text2:
            speak("Searching in Wikipedia...")
            obj = infow()
            obj.get_info(text2)
        elif "question" in text2 or "answer" in text2:
            speak("Which question you want to ask")
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, 1.2)
                try:
                    audio = r.listen(source)
                    topic = r.recognize_google(audio)
                    print(topic)
                except sr.UnknownValueError:
                    speak("Sorry, I did not understand that.")
                    continue
                except sr.RequestError as e:
                    speak(f"Could not request results from Google Speech Recognition service; {e}")
                    continue
            speak(f"Searching {topic} in Chatgpt...")
            obj = infow()
            obj.get_data(topic)
        elif "exit" in text2:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()