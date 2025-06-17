import whisper
from pyannote.audio import Pipeline
import json
import subprocess
import torchaudio


#loading whisper model 

model = whisper.load_model("large")
print("Whisper model loaded successfully.")
demo_audio = r"test.wav"
result = model.transcribe(demo_audio, language = "en")

print(result["text"])



pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=hface_token)
diarization = pipeline(demo_audio)


for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start: .1f}s - {turn.end: .1f}s: {speaker}")


segments = []
output = []

for segment in segments: 
    seg_start = segment['start']
    seg_end = segment['end']
    seg_speaker = segment['speaker']
    seg_text = result['text'][seg_start:seg_end]

    #find speaker in diarization time 

    speaker = "unknown"
    for turn, _, spk in diarization.itertracks(yield_label=True):
        if turn.start <= seg_start <= turn.end or turn.start <= seg_end <= turn.end:
            speaker = spk
            break

    output.append({
        "speaker": speaker,
        "start_time": seg_start,
        "end_time": seg_end,
        "text": seg_text.strip()
    })

# Save the output to a JSON file
with open("transcription_with_diarization.json", "w") as f:
    json.dump(output, f, indent=3)

print(json.dumps(output, indent=3))

