
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def record_audio(duration, sample_rate=44100):
    print("Recording...")

    # Record audio for the given duration
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")

    return audio

def save_audio(file_name, audio_data, sample_rate=44100):
    # Save the recorded audio as a WAV file
    wav.write(file_name, sample_rate, audio_data)
    print(f"Audio saved as '{file_name}'.")

def main():
    duration = int(input("Enter duration in seconds: "))  # Duration of the recording
    audio_data = record_audio(duration)
    
    file_name = input("Enter filename to save audio (e.g., recording.wav): ")
    save_audio(file_name, audio_data)

if __name__ == "__main__":
    main()
