from collections import Counter as counter
import os

def parse(textfile, countfile):
    if os.path.isfile(countfile):
        print("{} exists".format(countfile))
        return

    print("Loading {}".format(textfile))
    with open(textfile, "r") as f:
        data = f.read()

    data = map(lambda c: (" ", c.lower())[int(c.isalpha())], data)
    data = "".join(list(data)).split()
    data = counter(data)

    print("Writing {}".format(countfile))
    with open(countfile, "w") as f:
        print("word,count", file=f)
        for word, count in data.items():
            print("{},{}".format(word,count), file=f)
