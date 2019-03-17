import pandas as pd

excel_file = 'resources/sample.xlsx'
excel_sheet = 'Sheet1'

sample_xl = pd.read_excel('resources/sample.xlsx', sheet_name=excel_sheet)
print (sample_xl)

