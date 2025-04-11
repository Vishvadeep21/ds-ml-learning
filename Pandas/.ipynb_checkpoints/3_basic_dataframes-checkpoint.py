import pandas as pd

df=pd.read_csv("movies.csv")

print(df.columns)

print(df.studio.unique())                #gives unique values of selected column

print(df.industry.value_counts())       #gives no of repetation of value count

df_new=df[["title","industry"]]
print(df_new)                           #we can create sorted dataframe(acc to us) like this

print(df[(df.release_year>=2000) & (df.release_year<=2010)])    #here we sorted/filter row
print(df[df['industry']=="Hollywood"])

print(df.describe())                    #here we described whote dataframe using basic statistics

print(df.info())                        #we got information of the datatype and number of non null values

