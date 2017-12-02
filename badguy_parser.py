# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

files = ['BannedBrokers/Inbarred_individuals_20170930.csv', 'Active_Corporations___Beginning_1800.csv']

# Importing the dataset
dataset = pd.read_csv(files[0])
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

print(X)