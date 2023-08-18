import speech_recognition as sr

def transcribe_audio(audio_path):
    """
    Transcribes audio from an audio file using the Google Web Speech API.

    Args:
        audio_path (str): Path to the audio file (supported formats: WAV, AIFF, FLAC).

    Returns:
        str: Transcribed text from the audio.

    Raises:
        FileNotFoundError: If the specified audio file is not found.
        Exception: If there is an issue with the speech recognition process.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)  # Record the entire audio file

        transcribed_text = recognizer.recognize_google(audio)
        return transcribed_text

    except FileNotFoundError:
        raise FileNotFoundError(f"Audio file not found at '{audio_path}'")

    except Exception as e:
        raise Exception(f"Error during speech recognition: {e}")

if __name__ == "__main__":
    try:
        audio_path = "path_to_your_audio_clip.wav"  # Replace with the path to your audio clip
        transcribed_text = transcribe_audio(audio_path)
        print("Transcribed Text:")
        print(transcribed_text)

    except Exception as e:
        print("Error:", e)
