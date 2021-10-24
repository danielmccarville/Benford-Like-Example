"""
Goal: Show how to use scipy.optimize.curve_fit to optimize new parameters
with Benford's Law.
"""

# Imports
import pandas as pd

import numpy as np
import benfords
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

# Settings
filename = 'AB_NYC_2019.csv'

# Functions
def test(digit, s, q):
    denominator = s+(digit**q)
    return np.log10(1+(1/denominator))

# Program

### Import data
data = pd.read_csv(filename, header=0, index_col=0)
prices = data[data['price']>0]['price']

### Calculate actual digit frequencies
actual_freq = benfords.benfords(prices)[['Digit', 'Actual Value']]
actual_freq['Digit'] = pd.to_numeric(actual_freq['Digit'], errors='coerce', downcast='float').astype('float64')

### Fit the parameters
x = actual_freq['Digit']
y = actual_freq['Actual Value']
popt, pcov = curve_fit(test, x, y, p0=[0, 0])

popt

