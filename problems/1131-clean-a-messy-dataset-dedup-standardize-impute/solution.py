import pandas as pd

def solution(df):
    df = df.copy()
    df['name'] = df['name'].astype(str).str.strip().str.title()
    df['date'] = pd.to_datetime(df['date'].astype(str).str.strip()).dt.strftime('%Y-%m-%d')
    df = df.drop_duplicates(keep='first').reset_index(drop=True)
    mean_val = df['value'].mean()
    df['value'] = df['value'].fillna(mean_val)
    return df
    pass