import pandas
import matplotlib.pyplot as plt


# This particular program works file only with bank of baroda bank statements

def get_date_wise_graphical_transactions(dataframe, transaction_type):
    df_grouped = dataframe.groupby(dataframe['DATE'].dt.date)[transaction_type].sum()
    df_grouped.plot()
    plt.show()


def data_cleaner(data_frame, columns):
    data_frame.drop(data_frame.columns[data_frame.columns.str.contains('^Unnamed')], axis=1, inplace=True)
    for column in columns:
        data_frame[column].fillna(0, inplace=True)
        data_frame[column] = data_frame[column].str.replace('Cr', '').str.replace(',', '').astype(float)
    return data_frame


def read_transaction_records_and_clean():
    columns_to_clean = ["DEPOSIT(CR)", "WITHDRAWAL(DR)", "BALANCE(INR)"]
    file_path = "/Users/nikhil/Downloads/transaction2.xls"
    data_frame = pandas.read_excel(file_path, skiprows=range(1, 11), header=1, nrows=446)
    data_frame = data_frame.rename(columns={'DATE': 'Unnamed', 'Unnamed: 1': "DATE"})
    cleaned_data_frame = data_cleaner(data_frame, columns_to_clean)
    cleaned_data_frame['DATE'] = pandas.to_datetime(cleaned_data_frame['DATE'], format='%d/%m/%Y')

    return cleaned_data_frame


def graphical_representation_of_transactional_data():
    dataframe = read_transaction_records_and_clean()
    get_date_wise_graphical_transactions(dataframe, ["WITHDRAWAL(DR)", "DEPOSIT(CR)"])


def basic_analysis_on_recorded_data():
    dataframe = read_transaction_records_and_clean()
    total_deposited_amount = dataframe["DEPOSIT(CR)"].sum()
    total_withdrawal_amount = dataframe["WITHDRAWAL(DR)"].sum()
    average_balance = dataframe["BALANCE(INR)"].mean()
    print("Total Amount Deposited", total_deposited_amount)
    print("Total Amount WITHDRAWAL", total_withdrawal_amount)
    print("Average Monthly Balance", average_balance)


def upi_id_and_payment_occurrence_analysis():
    dataframe = read_transaction_records_and_clean()
    mask = dataframe['NARRATION'].str.contains('/UPI/')
    filtered_df = dataframe[mask]
    upi_ids = filtered_df['NARRATION'].str.extract('/UPI/(\w+)')
    upi_counts = upi_ids.value_counts()
    print(upi_counts)


upi_id_and_payment_occurrence_analysis()
