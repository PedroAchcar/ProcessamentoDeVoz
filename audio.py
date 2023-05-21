import speech_recognition as sr


def text_from_audio() -> str:
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        print("-> Diga uma palavra:")
        audio = microphone.record(source, duration=2)

    try:
        word = microphone.recognize_google(audio, language='pt-BR')
        print('1 - Palavra: ', word)

        return word

    except sr.UnknownValueError:
        return "-> Não foi possível reconhecer o áudio"

    except sr.RequestError as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    text_from_audio()
