import whisper 

model = whisper.load_model("medium") 

def speech_to_text (audio_path: str ) -> str :

    result = model.transcribe( audio_path , language ="ar" ) 

    result ["text"].strip()