import pandas as pd
def youtube_clean():
    df=pd.read_csv("Youtubedata.csv")
    df.describe()
    D=df["published_at"]
    Dates=[]
    for i in D:
        Dates.append(i[0:10])
    df.drop(["published_at"],axis=1,inplace=True)
    df["Dates"]=Dates
    df.drop(["Unnamed: 0"],axis=1,inplace=True)
    print(df)
    df.to_csv("cleaned_youtube_data.csv")