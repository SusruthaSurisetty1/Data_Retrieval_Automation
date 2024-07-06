import pandas as pd
import os
excels_folder_path = "C:/Users/dell/OneDrive/Desktop/GUI/datasets/"
output_folder_single_excel_path = "C:/Users/dell/OneDrive/Desktop/GUI/output/"
files = [file for file in os.listdir(excels_folder_path) if file.endswith('.xlsx')]
final_excel_file_data = []

for file in files:
    df = pd.read_excel(excels_folder_path + file, usecols="B")
    data = df.to_dict('list')
    data = data['flex href']
    final_excel_file_data.extend(data)
import xlwt 
from xlwt import Workbook 
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 
for i in range(0, len(final_excel_file_data)):
    sheet1.write(i, 0, final_excel_file_data[i])
wb.save(output_folder_single_excel_path + 'Final Output.xlsx')