"""
Goal: Show how to use scipy.optimize.curve_fit to optimize new parameters
with Benford's Law.

1. Import a data set.


2. Iterate through values of S:
2.1 Iterate through values of Q:
2.11 For each category, fit to BL
2.12 Get some overall fit score, like MSE
2.13 SAVE: S, Q, MSE

2.2 Return the ideal S, Q, and the MSE.

Should it consider some kind of chart?


Current problem: Iterating through those floats. What to do?


"""

# Imports
import pandas as pd
import numpy as np
import benfords
import math
from sklearn.metrics import mean_squared_error

# Settings
filename = 'AB_NYC_2019.csv'

s_min = -0.01
s_max = 1
s_inc = 0.1

q_min = 0
q_max = 3.0
q_inc = 0.1

# Functions

# Program
### Import data
data = pd.read_csv(filename, header=0, index_col=0)
prices = data[data['price']>0]['price']

results = []

s_lin = np.linspace(s_min, s_max, int((s_max-s_min)/s_inc))
for s in s_lin:

    q_lin = np.linspace(q_min, q_max, int((q_max-q_min)/q_inc))
    for q in q_lin:
        print('S:', s, ' Q:', q)
        # Count actual digit frequencies
        actual_freq = benfords.benfords(prices)[['Digit', 'Actual Value']]
        
        # Calculate expected frequencies
        expected_freq = pd.DataFrame(columns=['Digit', 'Expected Value'])

        for digit in range(1, 10):
            expected_freq = expected_freq.append({'Digit': str(digit), 'Expected Value': math.log(1+(1/(s+(digit**q))), 10)}, ignore_index=True)

        # Don't forget to normalize the expected frequencies
        total_exp = expected_freq['Expected Value'].sum()
        expected_freq['Expected Value'] = expected_freq['Expected Value']/total_exp

        # Merge together and compare
        freq = pd.merge(actual_freq, expected_freq, on='Digit', how='left')

        # Calculate fit and save data"""
        mse = mean_squared_error(freq['Actual Value'], freq['Expected Value'])
        results.append([s, q, mse])

results_df = pd.DataFrame(results, columns=('s', 'q', 'mse'))
x.iloc[x['mse'].argmax()]
