#Read excel file and separate categories in the file.

import xlrd
import folium
import re
import numpy as np
import matplotlib

fileName = "COVID-19-geographic-disbtribution-worldwide-2020-03-19.xlsx"

wb = xlrd.open_workbook(fileName) 
sheet = wb.sheet_by_index(0) 

pattern = 'Afghanistan';
total_cases = 0;
for row in range(sheet.nrows):
	#sheet.cell_value(row, 6) stores the country name in the sheet
	if re.match(pattern,sheet.cell_value(row, 6)):
		#sheet.cell_value(row, 4) stores the number of cases in the sheet
		total_cases = total_cases + sheet.cell_value(row, 4);

#Create a map, centered (0,0)
mapWorld = folium.Map(location=[0, 0],zoom_start=3)

#Mark the total cases with a red dot on the map - show most recent date
folium.Marker(location = [33.9391, 67.7100], popup = total_cases).add_to(mapWorld)

#Determine the next country -- excel sheet of all possible countries and check if that country appears
#in the excel sheet. (pattern comes from all possible exel sheet)  - need the coordinate of the country.
mapWorld.save(outfile='coronaVirusCases.html')