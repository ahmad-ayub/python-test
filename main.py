import whisper

model = whisper.load_model("base.en", download_root="/Users/Ahmad_Ayub/code/python-test/model")
result = model.transcribe("/Users/Ahmad_Ayub/code/python-test/alloy.wav")
print(result["text"])