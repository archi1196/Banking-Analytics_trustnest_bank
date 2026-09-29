import numpy as np
from scipy import stats

def probability_menu(df):
    while True:
        print('\n========== PROBABILITY & INFERENCE =========='); print('1. Basic Probability\n2. Conditional Probability\n3. Binomial\n4. Poisson\n5. Normal\n6. Exponential\n7. Sampling & 95% CI\n8. Hypothesis Test\n9. Back')
        ch=input('Enter choice: ')
        p=(df.Loan_Status=='Approved').mean()
        if ch=='1': print('P(Loan Approved):',round(p,4))
        elif ch=='2':
            x=df[df.Credit_Score>=700]; print('P(Approved | Credit >=700):',round((x.Loan_Status=='Approved').mean(),4))
        elif ch=='3': print('Binomial P(exactly 6 of 10):',round(stats.binom.pmf(6,10,p),4))
        elif ch=='4': print('Poisson P(exactly 4):',round(stats.poisson.pmf(4,p*10),4))
        elif ch=='5': print('Normal P(Credit Score <=700):',round(stats.norm.cdf(700,df.Credit_Score.mean(),df.Credit_Score.std()),4))
        elif ch=='6':
            m=df.Loan_Amount_Requested.mean(); print('Exponential CDF at mean loan:',round(stats.expon.cdf(m,scale=m),4))
        elif ch=='7':
            n=min(100,len(df)); x=df.Annual_Income.sample(n=n,random_state=42); se=x.std()/np.sqrt(n); margin=stats.t.ppf(.975,n-1)*se; print('Sample Mean:',round(x.mean(),2)); print('95% CI:',round(x.mean()-margin,2),'to',round(x.mean()+margin,2))
        elif ch=='8':
            t,pv=stats.ttest_1samp(df.Annual_Income,500000); print('H0: Mean income = 500000'); print('t:',round(t,4),'p:',round(pv,4)); print('Reject H0' if pv<.05 else 'Fail to reject H0')
        elif ch=='9': break
        else: print('Invalid choice.')
