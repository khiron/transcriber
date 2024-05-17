# Transcriber

A tool for transcribing audio and video files using Whisper.

## Installation

You can install this package using pip:

```pip install git+https://github.com/yourusername/transcriber.git```

### Installing with CUDA support

To utilize CUDA cores for transcription, follow these steps:

1. **Ensure you have a CUDA-capable GPU**.

2. **Install the NVIDIA CUDA Toolkit**:
   Download and install the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) for your operating system.

3. **Install cuDNN**:
   Download and install the [cuDNN library](https://developer.nvidia.com/cudnn) for your CUDA version.

4. **Install PyTorch with CUDA support**:
   Use the following command to install PyTorch with CUDA support:
   ```pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113```
   Replace `cu113` with the appropriate version for your setup if necessary.

5. **Install other dependencies**:
   ```pip install click whisper pydub moviepy```

## Usage

The `transcriber` command allows you to transcribe audio or video files with optional start and end times.

### Basic Usage

To transcribe an entire file:

```transcriber path_to_your_file```

### Specifying Output File

To save the transcription to an output file:

```transcriber path_to_your_file -o output_file.txt```

### Specifying Start and End Times

To transcribe from a specific start time to an end time (in minutes):

```transcriber path_to_your_file --start 1 --end 3```

### Options

- `file`: Path to the audio or video file (mp4, mkv, mov, m4a, etc.).
- `-o, --output`: Output file for the transcription. If not specified, the transcription is printed to stdout.
- `--start`: Start time in minutes (default: 0).
- `--end`: End time in minutes (default: till end of file).

### Examples

To transcribe the first 3 minutes of a file:

```transcriber path_to_your_file --start 0 --end 3```

To transcribe a file and save the output to a specific file:

```transcriber path_to_your_file -o my_transcription.txt```

## Description

This tool extracts audio from video files if necessary, trims the audio to the specified time range, and then transcribes the audio using the Whisper model. The transcription will include newlines when a new speaker starts talking.
