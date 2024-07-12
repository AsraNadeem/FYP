import speech_recognition as sr  # Import the speech recognition library

# Function to convert speech to text
def speech_to_text():
    # Initialize the recognizer
    r = sr.Recognizer()

    try:
        # Use the microphone as the source for input
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            # Adjust the recognizer sensitivity to ambient noise
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            # Listen to the speech input from the microphone
            audio = r.listen(source)
            
            print("Recognizing...")
            # Recognize the speech using Google's speech recognition
            text = r.recognize_google(audio)
            # Print the recognized text
            print("You said: " + text)
    except sr.RequestError as e:
        # Handle errors related to the recognition request
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        # Handle errors when the speech is not understood
        print("Speech Recognition could not understand the audio")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Convert speech to text by calling the function
    speech_to_text()




# Import the Library: import speech_recognition as sr imports the speech recognition library.
# Function Definition: speech_to_text() defines a function to convert speech to text.
# Initialize Recognizer: r = sr.Recognizer() initializes the speech recognizer.
# Try Block: The try block contains the main code and handles any errors that might occur.
# Use Microphone: with sr.Microphone() as source: uses the microphone as the input source.
# Adjust for Noise: r.adjust_for_ambient_noise(source, duration=0.5) adjusts the recognizer to ignore 
# ambient noise.
# Listen to Speech: audio = r.listen(source) listens to the speech input and stores it in audio.
# Recognize Speech: text = r.recognize_google(audio) uses Google's speech recognition to convert the 
# audio to text.
# Print Text: print("You said: " + text) prints the recognized text.
# Exception Handling: The except blocks handle specific errors related to speech recognition 
# requests and unrecognized speech.