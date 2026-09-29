def statistics(df):
    x=df.Annual_Income; print('\n========== STATISTICS =========='); print('Mean:',round(x.mean(),2)); print('Median:',round(x.median(),2)); print('Mode:',x.mode().iloc[0]); print('Min:',x.min()); print('Max:',x.max()); print('Variance:',round(x.var(),2)); print('Std Dev:',round(x.std(),2)); print('Q1:',x.quantile(.25)); print('Q2:',x.quantile(.5)); print('Q3:',x.quantile(.75))

def loan_statistics(df):
    x=df.Loan_Amount_Requested; print('\n========== LOAN STATISTICS =========='); print('Mean:',round(x.mean(),2)); print('Median:',round(x.median(),2)); print('Min:',x.min()); print('Max:',x.max()); print('Std Dev:',round(x.std(),2))
