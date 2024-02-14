import pandas as pd


def iterate_using_apply(df):
    def process_row(row):
        return row['Column1'] + row['Column2']  

    result_series = df.apply(process_row, axis=1)
    print(result_series) 

df = pd.read_csv('big-mac-full-index.csv')



