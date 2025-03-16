import pandas as pd
df= pd.read_csv("movies.csv")
print(df.shape)

# to get max,min,avg imbd rating 

print(df.imdb_rating.min())
print(df.imdb_rating.max())
print(df.imdb_rating.mean())

# to get max,min,avg imbd rating in hollywood

df_h=df[df.industry=="Hollywood"]
print(df_h.imdb_rating.min())
print(df_h.imdb_rating.max())
print(df_h.imdb_rating.mean())

# to get max,min,avg imbd rating in bollywood

df_b=df[df.industry=="Bollywood"]
print(df_b.imdb_rating.min())
print(df_b.imdb_rating.max())
print(df_b.imdb_rating.mean())