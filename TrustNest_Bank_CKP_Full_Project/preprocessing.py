import pandas as pd

def clean_data(df):
    df=df.drop_duplicates().copy()
    for c in df.select_dtypes(include='number').columns: df[c]=df[c].fillna(df[c].median())
    for c in df.select_dtypes(include='object').columns:
        if not df[c].mode().empty: df[c]=df[c].fillna(df[c].mode()[0])
    return df

def data_info(df):
    print('\n========== DATA INFORMATION =========='); print('Rows:',len(df),'Columns:',len(df.columns)); print(df.dtypes); print('\nMissing values:'); print(df.isnull().sum())

def outliers(df):
    print('\n========== OUTLIER ANALYSIS ==========')
    for c in df.select_dtypes(include='number').columns:
        q1,q3=df[c].quantile(.25),df[c].quantile(.75); iqr=q3-q1
        n=((df[c]<q1-1.5*iqr)|(df[c]>q3+1.5*iqr)).sum(); print(c,':',n)

def normalize(df):
    cols=['Age','Annual_Income','Credit_Score','Account_Balance','Loan_Amount_Requested']; x=df[cols].copy()
    for c in cols:
        lo,hi=x[c].min(),x[c].max()
        if hi!=lo: x[c]=(x[c]-lo)/(hi-lo)
    print('\nNormalized data:'); print(x.head()); return x
