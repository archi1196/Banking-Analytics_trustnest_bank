import matplotlib.pyplot as plt
import seaborn as sns

def visualization_menu(df):
    while True:
        print('\n========== DATA VISUALIZATION =========='); print('1. Loan Status\n2. Credit Score\n3. Income vs Loan\n4. Employment\n5. Correlation Heatmap\n6. Back'); ch=input('Enter choice: ')
        if ch=='1': sns.countplot(x='Loan_Status',data=df); plt.title('TrustNest Bank - Loan Status'); plt.show()
        elif ch=='2': plt.hist(df.Credit_Score,bins=20); plt.title('Credit Score Distribution'); plt.xlabel('Credit Score'); plt.ylabel('Customers'); plt.show()
        elif ch=='3': plt.scatter(df.Annual_Income,df.Loan_Amount_Requested,alpha=.4); plt.title('Income vs Loan Amount'); plt.xlabel('Annual Income'); plt.ylabel('Loan Amount'); plt.show()
        elif ch=='4': sns.countplot(x='Employment_Status',data=df); plt.title('Employment Distribution'); plt.xticks(rotation=20); plt.show()
        elif ch=='5':
            cols=['Age','Annual_Income','Credit_Score','Account_Balance','Loan_Amount_Requested']; sns.heatmap(df[cols].corr(),annot=True,fmt='.2f'); plt.title('Banking Correlation Heatmap'); plt.show()
        elif ch=='6': break
        else: print('Invalid choice.')
