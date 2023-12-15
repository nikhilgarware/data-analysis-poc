import pandas


def data_cleaner(data_frame, columns):
    data_frame.drop(data_frame.columns[data_frame.columns.str.contains('^Unnamed')], axis=1, inplace=True)
    for column in columns:
        data_frame[column].fillna(0, inplace=True)
        data_frame[column] = data_frame[column].str.replace('Cr', '').str.replace(',', '').astype(float)

    return data_frame


def read_transaction_records_and_clean():
    columns_to_clean = ["DEPOSIT(CR)", "WITHDRAWAL(DR)", "BALANCE(INR)"]
    file_path = "/Users/nikhil/Downloads/transaction.xls"
    data_frame = pandas.read_excel(file_path, skiprows=range(1, 11), header=1, nrows=35)
    data_frame = data_frame.rename(columns={'DATE': 'Unnamed', 'Unnamed: 1': "DATE"})
    cleaned_data_frame = data_cleaner(data_frame, columns_to_clean)
    cleaned_data_frame['DATE'] = pandas.to_datetime(cleaned_data_frame['DATE'], format='%d/%m/%Y')

    pandas.options.display.max_columns = None
    print(cleaned_data_frame["DEPOSIT(CR)"].sum() - cleaned_data_frame["WITHDRAWAL(DR)"].sum())


read_transaction_records_and_clean()
