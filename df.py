
def find_split_column_index(df):
    res = []
    col_names = df.columns
    column_cnt = len(col_names)
    i = 0
    while i < column_cnt:
        col_name = df.columns[i]
        if ":" in col_name:
            col1 = col_name.split(":")[0].strip()
            col2 = col_name.split(":")[1].strip()
            df.insert(i, col1, '')
            df.rename(columns={col_name: col2}, inplace=True)
            res.append(i+1)
            column_cnt += 1
            i += 2
        else:
            i += 1
    return res

