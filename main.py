from modules import *
from utils import *
from loader import *
from indexer import *
from vectorizer import *
from preprocess import *
import sys

#UPDATE THIS OR UNCOMMENT BELOW QUERY TO RUN IN TERMINAL
#query = input("enter your query\n") 

query = sys.argv[1]

# Main file
#print(" 1. Loading data...")
data = load_data()  # Loading the data
data  = drop_nan(data)

# Getting the pos_index
#print("2. Constructing the Positional Indexing..")
# columns = ['figcaption', 'url', 'image_src']
columns = ['figcaption','url']

pos_index = get_pos_index(data, columns)

# Vectorizing the training data
#print(" 3. Vectorizing the data.")


#tfidf, tfidf_transformed_vector = tfidf_vectorize_data(data)
tfidf, tfidf_transformed_vector = tfidf_vectorize_data(data, columns)
# Ranking for the given query
#print(" 4. Ranking and displaying outputs for the query...")

#print("5. Printing the query <<<<<<<<")
print( "Showing Results For",query)
print('--------------------------------------------------')

cosine_sim = cosine_sim(query, tfidf, tfidf_transformed_vector)

#top_results = get_top_results(data, cosine_sim)
top_results= get_top_results(data, cosine_sim, columns)
print(top_results)


