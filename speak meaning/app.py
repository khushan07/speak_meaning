import pyttsx3
from PyDictionary import PyDictionary


class Speaking:
    def speak(self, audio):
        # Initialize pyttsx3 engine with 'sapi5'
        engine = pyttsx3.init('sapi5')
        
        # Get and set the voice property
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        
        # Speak the audio
        engine.say(audio)
        engine.runAndWait()


class GFG:
    def dictionary(self):
        speak = Speaking()
        dic = PyDictionary()
        
        speak.speak("Which word do you want to find the meaning of?")
        
        # Take the input word
        query = input("Enter the word: ")
        word = dic.meaning(query)
        
        if word:
            for state, meanings in word.items():
                print(f"{state}:")
                for meaning in meanings:
                    print(f"  - {meaning}")
                    speak.speak(f"The meaning of {query} in {state} is {meaning}.")
        else:
            print("Sorry, the word was not found.")
            speak.speak("Sorry, the word was not found.")


if __name__ == '__main__':
    gfg_instance = GFG()
    gfg_instance.dictionary()
