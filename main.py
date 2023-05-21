import requests

from audio import text_from_audio
from display import display_meaning


def get_meaning(word: str) -> list:
    url = f'https://dicio-api-ten.vercel.app/v2/{word}/'

    response = requests.get(url).json()
    response = response[0]['meanings'][0]
    print('2 - Significado: ', response)
    response = response.split(',')

    return response


def main() -> None:
    word = text_from_audio()
    meaning = get_meaning(word)
    display_meaning(meaning)


if __name__ == "__main__":
    main()
