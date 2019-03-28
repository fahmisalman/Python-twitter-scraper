from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
import matplotlib.pyplot as plt
import tweet_dumper as td
import csv
import re

df = []
with open('tweet.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        df = row

# df = td.fit('fahmisalmann')

words = ' '.join(df)

no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

twitter_mask = imread('Assets/Mask/twitter_mask.png', flatten=True)
print(twitter_mask.shape)
wordcloud = WordCloud(
    stopwords=STOPWORDS,
    font_path='Assets/Font/CabinSketch-Bold.ttf',
    background_color='white',
    width=twitter_mask.shape[1],
    height=twitter_mask.shape[0],
    mask=twitter_mask
    ).generate(no_urls_no_tags)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('Output/my_twitter_wordcloud_1.png', dpi=300)
plt.show()