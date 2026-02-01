# Installation Guide

## Step 1: Install Python (if you don't have it)

Download from: https://www.python.org/downloads/

## Step 2: Install Whisper

Open your terminal/command prompt and run:

```bash
pip install openai-whisper
```

This will download the Whisper model on first run (about 1GB for base model).

## Step 3: Download Script

Download `otter_killer.py` from this repository.

## Step 4: Run It

Place your audio file in the same folder and name it `meeting_notes.mp3`, then:

```bash
python otter_killer.py
```

Your transcription will appear as `meeting_notes.txt`.

## Troubleshooting

**Error: "whisper" not found:**
- Make sure you ran `pip install openai-whisper`
- Try `pip3 install openai-whisper` if you have multiple Python versions

**Error: File not found:**
- Rename your audio file to `meeting_notes.mp3`
- Or edit the script and change the `target_file` variable

## Performance

- **Base model:** Fast, good accuracy
- **Medium model:** Slower, better accuracy
- **Large model:** Very slow, best accuracy

To use a different model, edit `otter_killer.py` and change:
```python
model = whisper.load_model("base")  # Change to "medium" or "large"
```
