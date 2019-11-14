from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
from Preprocessing import *
import matplotlib.pyplot as plt
import Tweet_dumper as td
import glob


class PyWordCloud(object):

    def __init__(self, username, mask=None, font=None, background='white'):
        self.username = username
        self.wordcloud = None
        self.mask = mask
        self.font = font
        self.background = background

    def load_data(self):
        # d = []
        # with open('tweet.csv') as f:
        #     file = csv.reader(f)
        #     for row in file:
        #         d = row
        d = td.fit(self.username)
        # d = []
        # for name in glob.glob('Dataset/*'):
        #     temp = open(name)
        #     d.append(temp.read())
        return d

    def preprocessing(self, d):
        d = d[2:-1].lower()
        d = remove_escape(d)
        d = remove_url(d)
        d = remove_punctuation(d)
        d = stopword_removal(d)
        return d

    def fit(self):

        if self.mask is None:
            self.mask = 'Assets/Mask/twitter_mask.png'

        if self.font is None:
            self.font = 'Assets/Font/CabinSketch-Bold.ttf'

        df = self.load_data()

        for i in range(len(df)):
            df[i] = self.preprocessing(df[i])
        words = ' '.join(df)

        twitter_mask = imread(self.mask, flatten=True)
        self.wordcloud = WordCloud(
            stopwords=STOPWORDS,
            font_path=self.font,
            background_color=self.background,
            width=twitter_mask.shape[1],
            height=twitter_mask.shape[0],
            mask=twitter_mask
        ).generate(words)

    def view_wordcloud(self, show=True, save=False):
        plt.imshow(self.wordcloud)
        plt.axis('off')
        if save:
            plt.savefig('Output/{}_tweet.png'.format(self.username), dpi=300)
        if show:
            plt.show()


if __name__ == '__main__':

    wc = PyWordCloud('fsn')
    wc.fit()
    wc.view_wordcloud()