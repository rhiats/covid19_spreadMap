#Read excel file and separate categories in the file.

import xlrd
import numpy as np
import matplotlib

fileName = "COVID-19-geographic-disbtribution-worldwide-2020-03-19.xlsx"

wb = xlrd.open_workbook(fileName) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0)