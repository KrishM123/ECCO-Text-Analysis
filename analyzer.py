import contractions
import nltk
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
nltk.download('stopwords')

N = 10

with open('elder.txt', 'r') as text:
    text = contractions.fix(''.join([ele[7:] for ele in text.read().split('\\xe2\\')]))
    all_words = []
    for line in text.split('\n\n'):
        words = nltk.word_tokenize(line)
        words = [word.lower() for word in words if word.isalpha()]
        all_stopwords = stopwords.words('english')
        words_without_sw = [word for word in words if not word in all_stopwords]
        all_words += words_without_sw

    counts = dict(Counter(all_words).most_common(N))
    labels, values = zip(*counts.items())
    indSort = np.argsort(values)[::-1]
    labels = np.array(labels)[indSort]
    values = np.array(values)[indSort]
    indexes = np.arange(len(labels))
    bar_width = 0.35
    plt.bar(indexes, values)
    plt.xticks(indexes + bar_width, labels)
    plt.show()