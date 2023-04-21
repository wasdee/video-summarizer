import whisper

for name in whisper.available_models():
    print("Downloading whisper model: ", name)
    # skip old models
    if name in ["large-v1"]:
        continue
    whisper._download(whisper._MODELS[name], "/home/din/.cache/whisper", False)