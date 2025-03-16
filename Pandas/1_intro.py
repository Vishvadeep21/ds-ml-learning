import pandas as pd
df= pd.read_csv("movies.csv")
print(df.head(3))       #used to prinnt from top
print(df.tail(3))       #used to ptint from bottom
print(df.sample(3))     #used to print randomly

# we can also print using slicing concept

print(df.shape)     #used to see number of rows and columns of a file
