import numpy as np

from os import path, getcwd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

curr_dir = getcwd()

mask = np.array((Image.open(curr_dir + "/data/cloud_mask2.png")))

with open(path.join(curr_dir + "/data/shrek.txt"), "r") as f:
    text = f.read()

wc = WordCloud(max_words=500, stopwords=STOPWORDS, scale=3,
               mask=mask, margin=5, background_color="white", colormap="BuPu").generate(text)

wc.to_file("cloud.png")