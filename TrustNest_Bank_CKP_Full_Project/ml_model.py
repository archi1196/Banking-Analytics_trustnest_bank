import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

FEATURES=['Age','Gender','Married','Dependents','Education','Employment_Status','Self_Employed','Annual_Income','Credit_Score','Account_Type','Account_Balance','Existing_Loan','Property_Area','Loan_Amount_Requested','Loan_Term_Years']
NUM=['Age','Dependents','Annual_Income','Credit_Score','Account_Balance','Loan_Amount_Requested','Loan_Term_Years']
CAT=['Gender','Married','Education','Employment_Status','Self_Employed','Account_Type','Existing_Loan','Property_Area']

def clean_for_ml(df):
    df=df.copy()
    df['Loan_Status']=df['Loan_Status'].astype(str).str.strip()
    df=df[df['Loan_Status'].isin(['Approved','Rejected'])].copy()
    for c in NUM:
        df[c]=pd.to_numeric(df[c],errors='coerce')
    df['Dependents']=df['Dependents'].astype(str).str.replace('+','',regex=False)
    df['Dependents']=pd.to_numeric(df['Dependents'],errors='coerce')
    for c in CAT:
        df[c]=df[c].astype(str).replace('nan',np.nan).str.strip()
    return df

def prepare_input(d):
    d=d.copy()
    for c in FEATURES:
        if c not in d.columns: d[c]=np.nan
    d=d[FEATURES]
    for c in NUM: d[c]=pd.to_numeric(d[c],errors='coerce')
    d['Dependents']=d['Dependents'].astype(str).str.replace('+','',regex=False)
    d['Dependents']=pd.to_numeric(d['Dependents'],errors='coerce')
    for c in CAT: d[c]=d[c].astype(str).replace('nan',np.nan).str.strip()
    return d

def train(df):
    df=clean_for_ml(df)
    if df.empty: raise ValueError('No Approved/Rejected records found for ML training.')
    x=df[FEATURES]; y=df['Loan_Status']
    if y.nunique()<2: raise ValueError('Loan_Status must contain both Approved and Rejected.')
    num_pipe=Pipeline([('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())])
    cat_pipe=Pipeline([('imputer',SimpleImputer(strategy='most_frequent')),('encoder',OneHotEncoder(handle_unknown='ignore'))])
    pre=ColumnTransformer([('numeric',num_pipe,NUM),('categorical',cat_pipe,CAT)])
    model=Pipeline([('preprocessor',pre),('classifier',LogisticRegression(max_iter=1000))])
    xt,xv,yt,yv=train_test_split(x,y,test_size=.20,random_state=42,stratify=y)
    model.fit(xt,yt)
    pred=model.predict(xv)
    print('\n========== LOGISTIC REGRESSION RESULTS ==========')
    print('Accuracy :',round(accuracy_score(yv,pred),4))
    print('Precision:',round(precision_score(yv,pred,pos_label='Approved',zero_division=0),4))
    print('Recall   :',round(recall_score(yv,pred,pos_label='Approved',zero_division=0),4))
    print('F1 Score :',round(f1_score(yv,pred,pos_label='Approved',zero_division=0),4))
    print('Confusion Matrix:')
    print(confusion_matrix(yv,pred,labels=['Approved','Rejected']))
    return model
