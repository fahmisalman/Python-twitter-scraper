import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

df = pd.read_csv('naufal_yai__tweets.csv')

# join tweets to a single string
words = ' '.join(df['text'])

# remove URLs, RTs, and twitter handles
no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

twitter_mask = imread('./twitter_mask.png', flatten=True)
wordcloud = WordCloud(
    stopwords=STOPWORDS,
    font_path='CabinSketch-Bold.ttf',
    background_color='white',
    width=1800,
    height=1400,
    mask=twitter_mask
    ).generate(no_urls_no_tags)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./my_twitter_wordcloud_1.png', dpi=300)
plt.show()