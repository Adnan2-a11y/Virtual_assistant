import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia  # Added import for Wikipedia

r = sr.Recognizer()  # recognizer

def listen():
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing....")
        command = r.recognize_google(audio).lower()  # Convert command to lower case
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Unable to access!")
        return ""
    except sr.RequestError:
        print("Request error!")
        return ""

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Initializing One....")

    while True:
        command = listen()

        if command == "hey one" or command == "hello one":
            speak("Hello sir, how can I help you?")

        elif command == "what is the current time":
            time = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"The current time is: {time}")

        elif command == "open youtube":
            webbrowser.open("https://www.youtube.com/")

        elif command == "open facebook":
            webbrowser.open("https://www.facebook.com/")

        elif command == "play music":
            webbrowser.open("https://www.youtube.com/watch?v=CHAAfC6gjnw")
        
        elif command == "play unless":
           webbrowser.open("https://www.youtube.com/watch?v=Aknd1dORG9Q")

        elif command == "search":
            print("Search Wikipedia")

            topic = input("Enter topic to search on Wikipedia: ")
            search = input("Press Enter to search...")

            if search == "":
                print("Searching...")
                try:
                    result = wikipedia.summary(topic, sentences=10)
                    speak(result)

                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"Multiple matches found for '{topic}'. Please be more specific.")
                    #speak(f"Multiple matches found for '{topic}'. Please be more specific.")
                    
                except wikipedia.exceptions.PageError as e:
                    print(f"No page found for '{topic}'.")
                    #speak(f"No page found for '{topic}'.")
        
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
