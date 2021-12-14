import pandas as pd

def read_file(file_path, dtype):
    pd_csv = pd.read_csv(file_path,dtype=dtype)
    return pd_csv


def get_cell(records, index, column_name):
    return records[[index],[column_name]]


def write_csv(file_path, source_df):
    source_df.to_csv(file_path)


def read_mul_files(file_list):
    l = []
    for csv_file in file_list:
        l.append(read_file(csv_file))
    df = pd.concat(l)
    return df


