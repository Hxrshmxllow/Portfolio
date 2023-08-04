import pandas as pd

def getItems(excel_file, sheet_name, start_row = 1):
    excel_data = pd.read_excel(excel_file, sheet_name, header=None)
    size = excel_data.shape
    row_num = size[0]
    datax = []
    for i in range(start_row, 4):
        data = excel_data.iloc[i].values.tolist()
        datax.append(data)
    return datax

     
