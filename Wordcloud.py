from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
import matplotlib.pyplot as plt
import tweet_dumper as td
import csv
import re


def load_data():
    d = []
    with open('tweet.csv') as f:
        file = csv.reader(f)
        for row in file:
            d = row

    # df = td.fit('fahmisalmann')
    return d


def remove_escape(d):
    d = d.split('\\')
    d = ' '.join(d)
    return d


def remove_url(d):
    d = d.split()
    i = 0
    while i < len(d):
        if 'https://' in d[i]:
            d.remove(d[i])
            i -= 1
        elif 'http://' in d[i]:
            d.remove(d[i])
            i -= 1
        i += 1

    d = ' '.join(d)
    return d


def remove_punctuation(d):
    d = d.split()
    i = 0
    while i < len(d):
        if len(d) > 0:
            if d[i][0] == 'x' and len(d[i]) == 3:
                d.remove(d[i])
                i -= 1
        if len(d) > 0:
            if len(d[i]) == 1:
                d.remove(d[i])
                i -= 1
        if len(d) > 0:
            if 'rt' in d[i]:
                d.remove(d[i])
                i -= 1
        i += 1
    d = ' '.join(d)
    return d


def preprocessing(d):
    d = d[2:-1]
    d = d.lower()
    d = remove_escape(d)
    d = remove_url(d)
    d = remove_punctuation(d)
    return d


df = load_data()
for i in range(len(df)):
    df[i] = preprocessing(df[i])
print(df)
words = ' '.join(df)

twitter_mask = imread('Assets/Mask/twitter_mask.png', flatten=True)
wordcloud = WordCloud(
    stopwords=STOPWORDS,
    font_path='Assets/Font/CabinSketch-Bold.ttf',
    background_color='white',
    width=twitter_mask.shape[1],
    height=twitter_mask.shape[0],
    mask=twitter_mask
    ).generate(words)

plt.imshow(wordcloud)
plt.axis('off')
# plt.savefig('Output/my_twitter_wordcloud_1.png', dpi=300)
plt.show()
