import pyttsx3

def save_and_speak(engine, text, output_file_path):
    # Set the volume level to 0.5 (you can adjust the value)
    engine.setProperty('volume', 2.3)

    # Use the save_to_file method to save the speech to the specified file
    engine.save_to_file(text, output_file_path)

    # Speak the text
    engine.say(text)

    # Wait for the speech to finish and save the file
    engine.runAndWait()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Set the voice to the second voice in the list (you can adjust the index)
engine.setProperty('voice', voices[1].id)

# Set the speech rate to 150 words per minute
engine.setProperty('rate', 150)

# Text to be spoken
text = "Hello I am Dhanushkumar."

# Set the file path where you want to save the audio file
output_file_path = r"C:\Users\ggrov\Desktop\New folder\output.wav"

# Call the function to speak and save the text with volume control
save_and_speak(engine, text, output_file_path)

print(f"Speech saved to: {output_file_path}")
