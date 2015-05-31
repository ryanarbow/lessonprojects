import pandas as pd
import numpy as np
import statsmodels.api as sm

#Load Lending Club Statistic
loanStats = pd.read_csv('LoanStats3d.csv')

#Remove '%' from int_rate
loanStats['int_rate'] = loanStats['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

#Change house_ownership data to 
loanStats['home_ownership_ord'] = pd.Categorical(loanStats.home_ownership).labels

#Extract columns
intrate = loanStats['int_rate']
annualinc = loanStats['annual_inc']
homeown = loanStats['home_ownership_ord']

#Use income (annual_inc) to model interest rates (int_rate)
# The dependent variable
y = np.matrix(intrate).transpose()

# The independent variables shaped as columns
x1 = np.matrix(annualinc).transpose()

X = sm.add_constant(x1)
model = sm.OLS(y, X)
f = model.fit()
f.summary()

#Add home ownership (home_ownership) to the model.
x2 = np.matrix(homeown).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(X)
model = sm.OLS(y, X2)
f = model.fit()
f.summary()
