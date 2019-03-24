import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from python_wordcloud import tweet_dumper as td
from scipy.misc import imread


df = td.fit('fahmisalmann')

words = ' '.join(df)

no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

twitter_mask = imread('Assets/Mask/twitter_mask.png', flatten=True)
wordcloud = WordCloud(
    stopwords=STOPWORDS,
    font_path='Assets/Font/CabinSketch-Bold.ttf',
    background_color='white',
    width=1800,
    height=1400,
    mask=twitter_mask
    ).generate(no_urls_no_tags)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('Output/my_twitter_wordcloud_1.png', dpi=300)
plt.show()