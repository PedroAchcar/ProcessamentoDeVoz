import speech_recognition as sr
from playsound import playsound


def text_from_audio() -> str:
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        playsound('audios/word.mp3')
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


def close_program() -> bool:
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        print("-> Diga 'fechar programa' para encerrar ou qualquer coisa para continuar.")
        audio = microphone.record(source, duration=3)

    try:
        word = microphone.recognize_google(audio, language='pt-BR')

        if word.lower() == 'fechar programa':
            return True
        return False

    except:
        return False


if __name__ == "__main__":
    text_from_audio()
