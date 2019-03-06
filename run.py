from get_text import get_text
from draw import draw
from parse import parse
from config import *

try:
    get_text(cardsfile, textfile, url)
    parse(textfile, countfile)
    draw(countfile, barfile, barcount)

    print("Done!")
except Exception as e:
    print(e)
