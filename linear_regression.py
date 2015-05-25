import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove '%' from Interest.Rate
loansData['Interest.Rate'] = loansData['Interest.Rate'] .map(lambda x: round(float(x.rstrip('%')) / 100, 4))

#Remove 'months' from Loan.Length
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

#Convert FICO scores into a numerical value, and save it in a new column 
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x.split("-")[0]))

#Plot a histogram of FICO Scores
import matplotlib.pyplot as plt

plt.figure()
p = loansData['FICO.Score'].hist()

#Create a scatter plot matrix
a = pd.scatter_matrix(loansData, alpha=.05, figsize=(10,10))

plt.show()

#Lesson: Linear Regression Analysis
import numpy as np
import statsmodels.api as sm

#Extract columns
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()

# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

#Combine two columns together to create an input matrix
x = np.column_stack([x1,x2])

#Create linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()

loansData.to_csv('loansData_clean.csv', header=True, index=False)