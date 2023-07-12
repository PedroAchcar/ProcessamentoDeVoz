import requests
from playsound import playsound

from audio import text_from_audio, close_program
from display import display_meaning
from text_to_speech import automaticReader


def get_meaning(word: str) -> list:
    url = f'https://dicio-api-ten.vercel.app/v2/{word}/'

    response = requests.get(url).json()
    response = response[0]['meanings'][0]
    print('2 - Significado: ', response)
    response = response.split(',')

    return response


def main() -> None:
    while True:
        word = text_from_audio()

        try:
            meaning = get_meaning(word)
            automaticReader(meaning)
            display_meaning(meaning)
        except:
            print(word)
            playsound('audios/error.mp3')

        if close_program():
            break

    playsound('audios/end.mp3')
    print("Finalizando programa")


if __name__ == "__main__":
    main()
