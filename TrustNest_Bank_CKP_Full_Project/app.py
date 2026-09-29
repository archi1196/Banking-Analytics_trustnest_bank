from flask import Flask, render_template, request, jsonify
import pandas as pd
from pathlib import Path
from ml_model import train, prepare_input

BASE_DIR=Path(__file__).resolve().parent
EXCEL_FILE=BASE_DIR/'CKP_BANK_20k_Customers_25_Staff.xlsx'
app=Flask(__name__)

def customers(): return pd.read_excel(EXCEL_FILE,sheet_name='Customers')
def staff(): return pd.read_excel(EXCEL_FILE,sheet_name='Staff')

@app.get('/')
def home(): return render_template('index.html')

@app.post('/api/staff-login')
def staff_login():
    d=request.get_json(silent=True) or {}; u=str(d.get('username','')).strip(); p=str(d.get('password','')).strip()
    df=staff(); r=df[(df['Username'].astype(str).str.strip()==u)&(df['Password'].astype(str).str.strip()==p)]
    if r.empty: return jsonify(success=False,message='Invalid username or password.'),401
    x=r.iloc[0]
    return jsonify(success=True,staff={'id':str(x['Staff_ID']),'name':str(x['Staff_Name']),'role':str(x['Role'])})

@app.post('/api/customer-login')
def customer_login():
    d=request.get_json(silent=True) or {}; bid=str(d.get('banking_id','')).strip().upper(); p=str(d.get('password','')).strip()
    df=customers(); r=df[(df['Banking_ID'].astype(str).str.strip().str.upper()==bid)&(df['Customer_Password'].astype(str).str.strip()==p)]
    if r.empty: return jsonify(success=False,message='Invalid Banking ID or password.'),401
    x=r.iloc[0]
    def val(k): return str(x[k])
    return jsonify(success=True,customer={
        'banking_id':val('Banking_ID'),'name':val('Full_Name'),'age':val('Age'),'gender':val('Gender'),
        'married':val('Married'),'dependents':val('Dependents'),'education':val('Education'),
        'employment_status':val('Employment_Status'),'account_type':val('Account_Type'),
        'account_balance':float(x['Account_Balance']),'credit_score':float(x['Credit_Score']),
        'existing_loan':val('Existing_Loan'),'previous_loan_amount':float(x['Previous_Loan_Amount']),
        'previous_loan_status':val('Previous_Loan_Status'),'loan_status':val('Loan_Status')})

@app.get('/api/analytics')
def analytics():
    df=customers(); s=df['Loan_Status'].astype(str).str.strip(); total=len(df); approved=int((s=='Approved').sum()); rejected=int((s=='Rejected').sum())
    return jsonify(total_customers=total,approved=approved,rejected=rejected,approval_rate=round(approved/total*100,2),average_income=round(pd.to_numeric(df['Annual_Income'],errors='coerce').mean(),2),average_balance=round(pd.to_numeric(df['Account_Balance'],errors='coerce').mean(),2),average_credit=round(pd.to_numeric(df['Credit_Score'],errors='coerce').mean(),2))

@app.post('/api/predict')
def predict():
    d=request.get_json(silent=True) or {}; df=customers()
    row={
        'Age':d.get('Age'),'Gender':d.get('Gender'),'Married':d.get('Married'),'Dependents':d.get('Dependents'),
        'Education':d.get('Education'),'Employment_Status':d.get('Employment_Status'),'Self_Employed':d.get('Self_Employed'),
        'Annual_Income':d.get('Annual_Income'),'Credit_Score':d.get('Credit_Score'),'Account_Type':d.get('Account_Type'),
        'Account_Balance':d.get('Account_Balance'),'Existing_Loan':d.get('Existing_Loan'),'Property_Area':d.get('Property_Area'),
        'Loan_Amount_Requested':d.get('Loan_Amount_Requested'),'Loan_Term_Years':d.get('Loan_Term_Years')}
    model=train(df); inp=prepare_input(pd.DataFrame([row])); pred=model.predict(inp)[0]; probs=model.predict_proba(inp)[0]; classes=list(model.classes_); prob=float(probs[classes.index(pred)]*100)
    return jsonify(success=True,prediction=str(pred),probability=round(prob,2))

if __name__=='__main__':
    print('TRUSTNEST BANK BY CKP')
    print('Open http://127.0.0.1:5000')
    app.run(host='0.0.0.0',port=5000,debug=True)
