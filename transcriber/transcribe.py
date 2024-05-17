import whisper
import warnings
import torch
import os
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

# Suppress specific warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

def extract_audio(file_path):
    """Extract audio from a video file and return the path to the audio file."""
    if file_path.lower().endswith(('.mp4', '.mkv', '.mov')):
        video = VideoFileClip(file_path)
        audio_path = "extracted_audio.wav"
        video.audio.write_audiofile(audio_path, codec='pcm_s16le')
        return audio_path
    else:
        return file_path

def transcribe_file(file_path, start_time, end_time):
    # Load the Whisper model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("base", device=device)

    # Extract audio if input is a video file
    audio_file_path = extract_audio(file_path)
    
    # Load the audio file with pydub to trim it
    audio = AudioSegment.from_file(audio_file_path)
    
    # Convert times from minutes to milliseconds
    start_time_ms = start_time * 60 * 1000
    end_time_ms = end_time * 60 * 1000 if end_time else len(audio)
    
    # Trim the audio
    trimmed_audio = audio[start_time_ms:end_time_ms]
    
    # Export the trimmed audio to a temporary file
    trimmed_audio_path = "trimmed_audio.wav"
    trimmed_audio.export(trimmed_audio_path, format="wav")
    
    # Transcribe the trimmed audio file
    result = model.transcribe(trimmed_audio_path, language="en", task="transcribe", condition_on_previous_text=False)
    
    # Remove the temporary trimmed audio file
    os.remove(trimmed_audio_path)
    if audio_file_path != file_path:
        os.remove(audio_file_path)
    
    # Format the transcription with newlines for each speaker change
    segments = result['segments']
    transcription_with_speakers = ""
    last_speaker = None
    
    for segment in segments:
        speaker = segment.get('speaker', None)
        text = segment['text'].strip()
        
        if speaker != last_speaker:
            if last_speaker is not None:
                transcription_with_speakers += "\n"
            last_speaker = speaker
        
        transcription_with_speakers += f"{text} "

    return transcription_with_speakers.strip()
