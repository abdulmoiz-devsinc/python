import pandas as pd

def read_dataset(path: str) -> pd.DataFrame:
    try:
        if path.endswith('.csv'):
            return pd.read_csv(path)
        elif path.endswith('.json'):
            return pd.read_json(path)
        else:
            raise ValueError("Unsupported file format. Only .csv and .json are allowed.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file is empty: {path}")
    except Exception as e:
        raise RuntimeError(f"Failed to read dataset: {e}")


if __name__=="__main__":
    path='./dataset/data.csv'
    df=read_dataset(path)
    print(df.head())