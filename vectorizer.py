

from modules import *

def tfidf_vectorize_data(data, columns):
    tfidf = TfidfVectorizer()
    combined_text = data[columns].apply(lambda x: ' '.join(x), axis=1)
    tfidf_transformed = tfidf.fit_transform(combined_text)
    return tfidf, tfidf_transformed


