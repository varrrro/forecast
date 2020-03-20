import pandas as pd

def merge_datasets(temp, hum, final):
    temp_df = pd.read_csv(temp)
    hum_df = pd.read_csv(hum)

    temp_df = temp_df.dropna(subset=['San Francisco'])
    hum_df = hum_df.dropna(subset=['San Francisco'])

    temp_df = temp_df[['datetime', 'San Francisco']]
    hum_df = hum_df[['datetime', 'San Francisco']]

    temp_df = temp_df.rename(columns={'datetime': 'DATE', 'San Francisco': 'TEMP'})
    hum_df = hum_df.rename(columns={'datetime': 'DATE', 'San Francisco': 'HUM'})

    merged_df = pd.merge(temp_df, hum_df, on='DATE')
    merged_df.to_csv(final, index=False)