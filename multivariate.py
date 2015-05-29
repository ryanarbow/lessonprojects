import pandas as pd

loansData = pd.read_csv('Loadstats3d.csv', skiprows=1)

#Remove '%' from int_rate
loansData['int_rate'] = loansData['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

#Extract columns
#intrate = loansData['int_rate']
#annualinc = loansData['annual_inc']
#homeown = loansData['home_ownership']
