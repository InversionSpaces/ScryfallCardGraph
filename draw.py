import pandas as pd
import matplotlib.pyplot as plt
import os

def draw(countfile, barfile, barcount):
    if os.path.isfile(barfile):
        print("{} exists".format(barfile))
        return 

    df = pd.read_csv(countfile)
    df = df.sort_values(by=['count'], ascending=False)

    plt.figure(figsize=(20, 3))

    df[:barcount].plot.bar(x="word", y="count")

    print("Writing {}".format(barfile))
    plt.savefig(barfile, bbox_inches='tight')
