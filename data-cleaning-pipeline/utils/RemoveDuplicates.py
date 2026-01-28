import pandas as pd

def removeDuplicate(df:pd.DataFrame)->pd.DataFrame:
    df.drop_duplicates(inplace=True)
    return df