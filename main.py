import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
nltk.download('punkt_tab')

url ='https://edition.cnn.com/2024/11/20/politics/doge-remote-work-federal-employees/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title:{article.title}')
print(f'Authors:{article.authors}')
print(f'Publication Date:{article.publish_date}')
print(f'Summary:{article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')



