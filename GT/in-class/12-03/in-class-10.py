import pandas as pd

source_csv = "resources/books.csv" 
df = pd.read_csv(source_csv, encoding="ISO-8859-1") 

df1 = df[['isbn', 'original_publication_year', 'original_title', 'authors', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5']]

rename_to = {
    "isbn": "ISBN", 
    "original_publication_year": "Publication Year",
    "original_title": "Original Title",
    "authors": "Authors",
    "ratings_1": "One Star Reviews",
    "ratings_2": "Two Star Reviews",
    "ratings_3": "Three Star Reviews",
    "ratings_4": "Four Star Reviews",
    "ratings_5": "Five Star Reviews"
}

df_output = df1.rename(columns=rename_to)
df_output.to_csv('output.csv', index=False, header=True)
