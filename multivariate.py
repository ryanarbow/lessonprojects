cd /Users/Ryan/Desktop/Thinkful

import pandas as pd
import numpy as np
import statsmodels.api as sm

#Load Lending Club Statistic
loanStats = pd.read_csv('LoanStats3d.csv')

#Remove '%' from int_rate
loanStats['int_rate'] = loanStats['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

#Change house_ownership
loanStats['home_ownership_ord'] = pd.Categorical(loanStats.home_ownership).labels

#Extract columns
X = loanStats['int_rate']
y = loanStats['annual_inc']

X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
est.summary()

X1 = loanStats[['int_rate', 'home_ownership_ord']]
X2 = sm.add_constant(X1)
est = sm.OLS(y, X2).fit()
est.summary()