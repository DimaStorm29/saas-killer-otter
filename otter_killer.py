#!/usr/bin/env python3
"""
Otter Killer - Free Transcription Script
Replaces $120/year Otter.ai subscription with local, private transcription.
"""

import os
import sys
import whisper

def transcribe_audio(file_path, model_size="base"):
    """
    Transcribe an audio file using OpenAI's Whisper model.
    
    Args:
        file_path: Path to audio file
        model_size: "base" (fast), "medium" (accurate), or "large" (very accurate)
    """
    
    # Load the model
    try:
        print(f"📥 Loading Whisper {model_size} model...")
        model = whisper.load_model(model_size)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        print("💡 Make sure you've run: pip install openai-whisper")
        return
    
    # Transcribe the file
    try:
        print(f"⚡ Transcribing: {file_path}")
        result = model.transcribe(file_path, fp16=False)
    except Exception as e:
        print(f"❌ Error transcribing file: {e}")
        return
    
    # Save to text file
    output_file = os.path.splitext(file_path)[0] + ".txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        print(f"✅ Transcription saved to: {output_file}")
    except Exception as e:
        print(f"❌ Error saving transcription: {e}")

if __name__ == "__main__":
    # Support command-line argument
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = "meeting_notes.mp3"
    
    if not os.path.exists(target_file):
        print(f"❌ File not found: {target_file}")
        print(f"💡 Usage: python {os.path.basename(__file__)} [audio_file.mp3]")
        print(f"💡 Example: python {os.path.basename(__file__)} my_recording.mp3")
        sys.exit(1)
    
    # Optional: allow model size selection
    model_size = "base"  # Default
    if len(sys.argv) > 2:
        model_size = sys.argv[2]
        if model_size not in ["base", "medium", "large"]:
            print(f"⚠️  Invalid model size: {model_size}")
            print("💡 Valid options: base, medium, large")
            model_size = "base"  # Fall back to default
    
    transcribe_audio(target_file, model_size)
