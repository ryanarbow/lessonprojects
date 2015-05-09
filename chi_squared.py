#Write a script called "chi_squared.py" that loads the data, cleans it, 
#performs the chi-squared test, and prints the result. 


from scipy import stats

#Loads data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#cleans data
loansData.dropna(inplace=True)

#performs chi squared
chi, p = stats.chisquare(freq.values())

#prints
print chi