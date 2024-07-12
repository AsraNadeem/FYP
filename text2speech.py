import pyttsx3  # Import the text-to-speech library

# Function to convert text to speech
def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    # Say the text
    engine.say(text)
    # Wait until the speech is finished
    engine.runAndWait()

if __name__ == "__main__":
    # Ask the user to enter the text
    text = input("Enter the text you want to convert to speech: ")
    # Convert the entered text to speech
    text_to_speech(text)


# Import the Library: import pyttsx3 imports the text-to-speech library.
# Function Definition: text_to_speech(text) defines a function to convert text to speech.
# Initialize Engine: engine = pyttsx3.init() initializes the text-to-speech engine.
# Say Text: engine.say(text) prepares the engine to say the given text.
# Run Engine: engine.runAndWait() runs the engine to speak the text and waits until it's finished.
# Main Block: if __name__ == "__main__": ensures the script runs only when executed directly.
# It prompts the user to enter text and calls text_to_speech(text) to convert it to speech.