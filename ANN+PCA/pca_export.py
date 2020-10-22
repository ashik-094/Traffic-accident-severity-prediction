# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:52:52 2019

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
# Backprop on the Seeds Dataset
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp

# Imporing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing dataset
dataset = pd.read_csv('Leeds01.csv')
#x=dataset
#print(x)
x = dataset.iloc[:,:-1].values
#print(x)
y = dataset.iloc[:,-1].values

# Feature scaling
from sklearn.preprocessing import StandardScaler
standardscaler_x = StandardScaler()
standardscaler_x = standardscaler_x.fit(x)
x = standardscaler_x.transform(x)


# Applying PCA on x
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
x_pca =pca.fit_transform(x)
pro_x_pca=pd.DataFrame(data=x_pca)
enough_components = np.sum(pca.explained_variance_ratio_) > 0.4
#print(pro_x_pca)
#print(x)

#dataset.describe()
dataset=pd.concat([pro_x_pca,dataset['1']],axis=1)
print(dataset)
export_csv = dataset.to_csv(r'C:\Users\User\Desktop\Completed tasks\PCA+ANN\data\pca01.csv', index = None, header= True)

# if True, 2 components is enough.
# The condition is problem dependent but more than 40% if very good.


