from gtts import gTTS

def generate_audio(text, lang="en"):

    tts = gTTS(text=text, lang=lang)

    file_path = "response.mp3"

    tts.save(file_path)

    return file_path