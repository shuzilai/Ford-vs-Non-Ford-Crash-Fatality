### Import packages in the virtual environment
import pandas as pd   ## search the package "pandans"
import statsmodels.api as sm    ## search the package "statsmodels"
import statsmodels.stats.api as sms   ## no need to install package
from statsmodels.compat import lzip   ## no need to install package
import matplotlib.pyplot as plt    ## search the package "matplotlib"
import seaborn as sns     ## search the package "seaborn"
import scipy.stats as scipy    ## search the package "scipy"
from scipy.stats import shapiro   ## no need to install package
import sys   ## no need to install package
import os   ## no need to install package

os.chdir(r"C:\Users\jenma\Desktop\spring 2025\CIS 9660\Group Project")
##Change the address to your working folder

pd.set_option('display.max_columns', 500)
## Display all columns when printing results

mydata = pd.read_csv(r"motor.csv")
## Remember to include “r” first inside the bracket.

file = open('motordata.txt','wt')
sys.stdout = file
## Open a text file and save all results into the text file

print(mydata.describe())
## Display summary statistics of the data
print(mydata.groupby('FORD?')['FATAL?'].mean())

df = pd.DataFrame(mydata)
##Transform the dataset into two-dimensional, size-mutable, potentially heterogeneous tabular data

######################## COMPARE FORD AND FATAL
x = df['FORD?']
y = df['FATAL?']
##Define t he dependent variable in the model

# with statsmodels
x = sm.add_constant(x)  # adding a constant
##Add a constant in the regression model

model1 = sm.Logit(y, x).fit()
##Fit the model
results_model1 = model1.summary()
print(results_model1)
##Output the results


######################## Linear regression with only multiple independent variables

x = df[['VEHICLE_OCCUPANTS', 'LICENSED?', 'NUMBER OF PERSONS INJURED', 'VEHICLE_AGE', 'FORD?', 'FEMALE?', 'DAYTIME?']]
##Define the independent variables in the model
y = df['FATAL?']
##Define the dependent variable in the model

# with statsmodels
x = sm.add_constant(x)  # adding a constant
##Add a constant in the regression model

model2 = sm.Logit(y, x).fit()
##Fit the model
results_model2 = model2.summary()
print(results_model2)
##Output the results

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
regression_results = {'Variable':['VEHICLE_OCCUPANTS','LICENSED?','NUMBER OF PERSONS INJURED','VEHICLE_AGE','FORD?','FEMALE?','DAYTIME?'],
'Coefficient': [0.0031, 0.8372, 0.1390, 0.0249, 0.5862, -0.2229, -0.9101],
'P-value': [0.944,0.411,0.484,0.434,0.235,0.629,0.016]}
data1 = pd.DataFrame(regression_results)
data1['Odds Ratio'] = np.exp(data1['Coefficient'])
data1['Significance'] = data1['P-value'] < 0.05
plt.figure(figsize=(10,6))
plt.bar(data1['Variable'],data1['Odds Ratio'], color=data1['Significance'].map({True:'green',False:'grey'}))
plt.axhline(1,color='black',label='No Effect (Odds Ratio=1')
plt.xlabel('Variables')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Odds Ratio')
plt.title('Odds Ratio for Logistic Regression Variables')
plt.legend()
plt.tight_layout()
plt.show()

#graph bar chart for fatality rate of ford vs non-ford
rate = {'FORD?': ['Non-Ford', 'Ford'],
        'Fatality Rate': [0.0002837,0.00051]}

ratedata = pd.DataFrame(rate)
plt.bar(rate['FORD?'],rate['Fatality Rate'], color=['grey','green'])
plt.title('Fatality Rate by Vehicle Type (Ford vs. Non-Ford')
plt.ylabel('Fatality Rate')
plt.xlabel('Vehicle Type')
plt.tight_layout()
plt.show()

file.close()
##Close the text file.


