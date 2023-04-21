import whisper


model = whisper.load_model("tiny")
result = model.transcribe("part2.mp3")

print(result)

# pickle the result
import pickle

with open("result.pkl", "wb") as f:
    pickle.dump(result, f)