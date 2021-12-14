import csv_rw
import pandas as pd
import df

csv_list = ['download_file_1.csv',
            'download_file_2.csv',
            'download_file_3.csv'
            ]

old_csv_file = 'ABS_BLDG_APPROVALS_LGA2021_19112021134429578_old.csv'

cleanup_replace = [["Measure", "Number of dwelling units","Total number of dwelling units"],
                   ]

sort_col_order_new = ['SECTOR','WORK_TYPE','BUILDING_TYPE','REGION']
sort_col_order_old = ['SECTOR','TYPE_WORK','TYPE_BLDG','LGA_2020']


def get_old_data():
    data = csv_rw.read_file(old_csv_file,dtype={'Value':pd.Int64Dtype()})
    data.sort_values(by=sort_col_order_old, inplace=True)
    return data


def get_new_data():
    data = csv_rw.read_file(csv_list[0],dtype={'OBS_VALUE':pd.Int64Dtype()})
    for i in range(1, len(csv_list)):
        tmp_data = csv_rw.read_file(csv_list[i],dtype={'OBS_VALUE':pd.Int64Dtype()})
        data = data.append(tmp_data, ignore_index=True)

    split_columns = df.find_split_column_index(data)
    split_cnt = 0
    for index, row in data.iterrows():
        for col_idx in split_columns:
            value = data.iloc[index, col_idx]
            if ":" in str(value):
                try:
                    data.iloc[index, col_idx - 1] = int(value.split(":")[0].strip())
                except:
                    data.iloc[index, col_idx - 1] = value.split(":")[0].strip()
                data.iloc[index, col_idx] = value.split(":")[1].strip()
                split_cnt += 1
            else:
                pass

        data.loc[index,'TIME_PERIOD'] = 'Sep-2021'
        for r in cleanup_replace:
            if data.loc[index,r[0]].strip() == r[1]:
                data.loc[index, r[0]] = r[2]

    data.sort_values(by=sort_col_order_new, inplace=True)
    print(split_cnt)
    return data

old_data = get_old_data()
csv_rw.write_csv('old.csv', old_data)

new_data = get_new_data()
csv_rw.write_csv('new.csv', new_data)