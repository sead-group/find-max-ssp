import shutil
import pandas as pd
import os


def clear_and_create_dir(dirpath):
    try:
        shutil.rmtree(dirpath)
    except FileNotFoundError:
        pass
    os.mkdir(dirpath)


def write_excel_file(df, filepath):
    """
    Writes a pandas dataframe to an Excel file.

    Parameters:
    df (pandas.DataFrame): The dataframe to write to the Excel file.
    filepath (str): The name of the Excel file to write.

    Returns:
    None
    """
    try:
        df.to_excel(filepath, index=False)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")


def load_excel_file(filename):
    """
    Reads an Excel file and returns its contents as a pandas dataframe.

    Parameters:
    filename (str): The name of the Excel file to read.

    Returns:
    pandas.DataFrame: The contents of the Excel file as a dataframe.
    """
    df = pd.read_excel(filename)
    return df

