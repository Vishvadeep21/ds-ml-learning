import pandas as pd
df=pd.read_csv("movies.csv")
print(f"{df}\n")

df['profit']=df['revenue']-df['budget']
print(f"{df}\n")

df['age']=df['release_year'].apply(lambda x: 2025-x)
print(f"{df}\n")

df.set_index('title',inplace=True)      

#When inplace=False (default): The function returns a new DataFrame with the updated index but does not modify the original DataFrame.
# When inplace=True: The function modifies the original DataFrame directly and returns None.

print(f"{df} \n")

df.reset_index(inplace=True)
print(f"{df}\n")

print(f"Oldest movie is:-\n{df[df['age']==df.age.max()]}")
print(f"newset movie is:-\n{df[df['age']==df.age.min()]}")