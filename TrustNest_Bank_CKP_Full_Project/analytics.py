def summary(df):
    a=(df.Loan_Status=='Approved').sum(); r=(df.Loan_Status=='Rejected').sum()
    print('\n========== BANK SUMMARY =========='); print('Bank: TrustNest Bank by CKP'); print('Customers:',len(df)); print('Approved:',a); print('Rejected:',r); print('Approval Rate:',round(a/len(df)*100,2),'%'); print('Avg Income:',round(df.Annual_Income.mean(),2)); print('Avg Balance:',round(df.Account_Balance.mean(),2)); print('Avg Credit Score:',round(df.Credit_Score.mean(),2))

def loan_analysis(df):
    print('\n========== LOAN ANALYSIS =========='); print(df.Loan_Status.value_counts()); print('\nExisting Loan:'); print(df.Existing_Loan.value_counts()); print('Avg Loan:',round(df.Loan_Amount_Requested.mean(),2)); print('Avg Term:',round(df.Loan_Term_Years.mean(),2),'years')

def risk_analysis(df):
    def cat(x): return 'Poor' if x<600 else ('Average' if x<700 else 'Good')
    print('\n========== CREDIT / RISK ANALYSIS =========='); print(df.Credit_Score.apply(cat).value_counts())

def group_analysis(df):
    print('\n========== GROUP ANALYSIS =========='); print('\nEducation:'); print(df.Education.value_counts()); print('\nEmployment:'); print(df.Employment_Status.value_counts()); print('\nProperty Area:'); print(df.Property_Area.value_counts()); print('\nAccount Type:'); print(df.Account_Type.value_counts())

def correlation(df):
    cols=['Age','Annual_Income','Credit_Score','Account_Balance','Loan_Amount_Requested']; print('\n========== CORRELATION =========='); print(df[cols].corr())

def insights(df):
    overall=(df.Loan_Status=='Approved').mean()*100; high=df[df.Credit_Score>=700]; high_rate=(high.Loan_Status=='Approved').mean()*100
    print('\n========== BUSINESS INSIGHTS =========='); print('Overall approval rate:',round(overall,2),'%'); print('Approval rate for credit score >=700:',round(high_rate,2),'%'); print('\nApproval rate by property area:'); print(df.groupby('Property_Area').Loan_Status.apply(lambda x:(x=='Approved').mean()*100).round(2))
