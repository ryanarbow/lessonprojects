#Create a new file called 'logistic_regression.py'. For this lesson, we're going to need pandas and statsmodels.
import pandas as pd
import statsmodels.api as sm
import math


#Load the data
loansData = pd.read_csv('loansData_clean.csv')

#Add a column to your dataframe indicating whether the interest rate is < 12%. 
#This would be a derived column that you create from the interest rate column. 
#You name it IR_TF. It would contain binary values, i.e.'0' when interest rate < 12% 
#or '1' when interest rate is >= 12%

loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: 1 if x > .12 else 0)

#Do some spot checks to make sure that it worked.
#df[df['Interest.Rate'] == 10].head() # should all be True
#df[df['Interest.Rate'] == 13].head() # should all be False

#Statsmodels needs an intercept column in your dataframe, so add a column with a constant intercept of 1.0.
intercept = [1] * len(loansData)
loansData['Intercept'] = intercept

#Create a list of the column names of our independent variables, including the intercept, and call it ind_vars.
ind_vars = ['Intercept','Amount.Requested','FICO.Score']

df = loansData

#Define the logistic regression model.
logit = sm.Logit(df['IR_TF'], df[ind_vars])

#Fit the model
result = logit.fit()

#Get the fitted coefficients from the results.
coeff = result.params
print coeff

#Write a function called logistic_function that will take a FICO Score and a Loan Amount 
#of this linear predictor, and return p. (Try not to hardcode any values if you can! 
#Hint: pass the coefficients object to the function as an argument.)
def logistic_function(FicoScore, LoanAmount):
	# p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))
	prob = 1/(1 + math.exp(coeff[0] + coeff[2]*FicoScore+coeff[1]*LoanAmount))
	if prob > 0.7:
		p = 1
	else:
		p = 0
	return prob, p