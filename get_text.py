import requests
from json import loads
import os

def get_text(cardsfile, textfile, url):
    if os.path.isfile(textfile):
        print("{} exists".format(textfile))
        return 

    if not os.path.isfile(cardsfile):
        print("Downloading {}".format(cardsfile))    
        with requests.get(url) as resp:
            with open(cardsfile, "wb") as f:
                f.write(resp.content)

    print("Loading {}".format(cardsfile))
    with open(cardsfile, "r") as f:
        data = f.read()

    cards = loads(data)
    texts = (card[pole] for card in cards if pole in card)
    text = " ".join(texts)

    print("Writing {}".format(textfile))
    with open(textfile, "w") as f:
        f.write(text)
