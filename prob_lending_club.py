#Write a script called "prob_lending_club.py" that reads in the loan data, cleans it, and 
#loads it into a pandas DataFrame. Use the script to generate and save a boxplot, 
#histogram, and QQ-plot for the values in the "Amount.Requested" column. Be able to 
#describe the result and how it compares with the values from the 
#"Amount.Funded.By.Investors". Push your code to Github and enter the link below.

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

#boxplot
loansData.boxplot(column='Amount.Requested')
plt.show()
plt.savefig("loans_box.png")

#histogram
loansData.hist(column='Amount.Requested')
plt.show()
plt.savefig("loans_hist.png")

#qq
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
plt.savefig("loans_qq.png")


