import pandas as pd

def read_user_dataset(path: str) -> pd.DataFrame:
    try:
        if path.endswith('.csv'):
            return pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file is empty: {path}")
    except Exception as e:
        raise RuntimeError(f"Failed to read dataset: {e}")