import pandas as pd

def removeNulls(df:pd.DataFrame)->pd.DataFrame:
    print("Total Nulls: ", df.isna().sum().sum())
    df.dropna(inplace=True)
    print("Total Nulls after removal: ", df.isna().sum().sum())
    return df