import pydub
import speech_recognition as sr

# Load the podcast audio
audio_path = 'path_to_your_podcast_audio.mp3'
podcast = pydub.AudioSegment.from_mp3(audio_path)

# Parameters
silence_threshold = -40  # Adjust this threshold to distinguish silence from speech
min_speech_duration = 5  # Minimum duration of speech segment (in seconds)

# Convert AudioSegment to raw audio data (16-bit PCM)
audio_data = podcast.raw_data
sample_width = podcast.sample_width
channels = podcast.channels
frame_rate = podcast.frame_rate

# Split audio into segments based on silence
r = sr.Recognizer()
audio_segments = pydub.silence.split_on_silence(audio_data, silence_thresh=silence_threshold)

# Filter segments to keep those with sufficient speech duration
important_segments = []
for segment in audio_segments:
    if len(segment) >= min_speech_duration * 1000:  # Convert to milliseconds
        important_segments.append(segment)

# Convert important segments back to AudioSegment and save as a new audio file
output_path = 'important_segments.mp3'
output_audio = pydub.AudioSegment.silent(duration=0, frame_rate=frame_rate, sample_width=sample_width, channels=channels)

for segment in important_segments:
    output_audio += segment

output_audio.export(output_path, format='mp3')

print(f"Extracted {len(important_segments)} important audio segments and saved them as {output_path}")
