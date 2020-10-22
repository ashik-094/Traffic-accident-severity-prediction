# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 23:04:45 2019

@author: ASHIK
"""
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp

import numpy as np
import pandas as pd
from numpy import array
from random import seed
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_row', 20)
pd.set_option('display.max_columns', 15)

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset


encode = LabelEncoder()

# load and prepare data
#filename = 'Leeds.csv'
filename = pd.read_csv('Leeds.csv')
#filename = filename.sample(frac=1)

# =============================================================================
# filename['GREasting'] = encode.fit_transform(filename['GREasting'])
# filename['1st_Road'] = encode.fit_transform(filename['1st_Road'])
# filename['LightingConditions'] = encode.fit_transform(filename['LightingConditions'])
# filename['Road_Surface'] = encode.fit_transform(filename['Road_Surface'])
# filename['LightingConditions'] = encode.fit_transform(filename['LightingConditions'])
# filename['WeatherConditions'] = encode.fit_transform(filename['WeatherConditions'])
# filename['TypeofVehicle'] = encode.fit_transform(filename['TypeofVehicle'])
# filename['CasualtyClass'] = encode.fit_transform(filename['CasualtyClass'])
# filename['Sex'] = encode.fit_transform(filename['Sex'])
# filename['ReferenceNumber'] = encode.fit_transform(filename['ReferenceNumber'])
# =============================================================================

filename['GREasting'] = encode.fit_transform(filename['GREasting'])
filename['GRNorthing'] = encode.fit_transform(filename['GRNorthing'])
filename['1st_Road'] = encode.fit_transform(filename['1st_Road'])
filename['LightingConditions'] = encode.fit_transform(filename['LightingConditions'])
filename['Road_Surface'] = encode.fit_transform(filename['Road_Surface'])
filename['LightingConditions'] = encode.fit_transform(filename['LightingConditions'])
filename['WeatherConditions'] = encode.fit_transform(filename['WeatherConditions'])
filename['TypeofVehicle'] = encode.fit_transform(filename['TypeofVehicle'])
filename['CasualtyClass'] = encode.fit_transform(filename['CasualtyClass'])
filename['Sex'] = encode.fit_transform(filename['Sex'])

filename['Severity'] = encode.fit_transform(filename['Severity']) 
 
print(filename)

# =============================================================================
# data_dummy = pd.get_dummies(filename)
# export_csv = data_dummy.to_csv (r'G:\New folder (2)\thesis\final data\PSO+CNN\Leeds02dummies.csv', index = None, header=True)
# =============================================================================

export_csv = filename.to_csv (r'G:\New folder (2)\thesis\final data\PSO+CNN\Leeds01.csv', index = None, header=True)
filename= 'Leeds01.csv'
#print(filename)
#datase = load_csv(filename)
#print(baba)
#for i in range(len(dataset[0])-1):
#	str_column_to_float(dataset, i)