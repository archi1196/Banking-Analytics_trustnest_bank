
def customer_login(file):
    import pandas as pd
    try: df = pd.read_excel(file, sheet_name='Customers')
    except Exception as e: print('Customer data error:', e); return None
    print('\n========== CUSTOMER LOGIN ==========')
    bid = input('Banking ID: '); pwd = input('Password: ')
    r = df[(df.Banking_ID.astype(str) == bid) & (df.Customer_Password.astype(str) == pwd)]
    if r.empty: print('Invalid Banking ID or password.'); return None
    print('Login successful. Welcome,', r.iloc[0].Full_Name); return r.iloc[0]

def show_profile(c):
    print('\n========== MY PROFILE ==========')
    for x in ['Banking_ID','Full_Name','Age','Gender','Married','Dependents','Education','Employment_Status']:
        print(x.replace('_',' '), ':', c[x])

def show_account(c):
    print('\n========== MY ACCOUNT ==========')
    for x in ['Account_Type','Account_Balance','Credit_Score']:
        print(x.replace('_',' '), ':', c[x])

def show_loan(c):
    print('\n========== MY LOAN ==========')
    for x in ['Existing_Loan','Previous_Loan_Amount','Previous_Loan_Status','Loan_Status']:
        print(x.replace('_',' '), ':', c[x])

def customer_management(df):
    while True:
        print('\n========== CUSTOMER MANAGEMENT ==========')
        print('1. Search\n2. Add\n3. Update\n4. Delete\n5. Back')
        ch=input('Enter choice: ')
        if ch=='1':
            bid=input('Banking ID: '); r=df[df.Banking_ID.astype(str)==bid]
            print('Customer not found.' if r.empty else r.to_string(index=False))
        elif ch=='2': df=add_customer(df)
        elif ch=='3': df=update_customer(df)
        elif ch=='4': df=delete_customer(df)
        elif ch=='5': return df
        else: print('Invalid choice.')

def add_customer(df):
    try:
        row={
        'Banking_ID':input('Banking ID: '),'Full_Name':input('Full Name: '),'Customer_Password':'Temp@123',
        'Age':int(input('Age: ')),'Gender':input('Gender: '),'Married':input('Married: '),'Dependents':input('Dependents: '),
        'Education':input('Education: '),'Employment_Status':input('Employment Status: '),'Self_Employed':input('Self Employed: '),
        'Annual_Income':float(input('Annual Income: ')),'Credit_Score':int(input('Credit Score: ')),'Account_Type':input('Account Type: '),
        'Account_Balance':float(input('Account Balance: ')),'Existing_Loan':input('Existing Loan: '),'Previous_Loan_Amount':0,
        'Previous_Loan_Status':'No Previous Loan','Property_Area':input('Property Area: '),'Loan_Amount_Requested':float(input('Loan Amount: ')),
        'Loan_Term_Years':int(input('Loan Term: ')),'Loan_Status':'Pending'}
        df.loc[len(df)]=row; print('Customer added.')
    except ValueError: print('Invalid numeric input.')
    return df

def update_customer(df):
    bid=input('Banking ID: '); idx=df.index[df.Banking_ID.astype(str)==bid].tolist()
    if not idx: print('Customer not found.'); return df
    print('1. Full Name  2. Annual Income  3. Credit Score  4. Account Balance')
    fields={'1':'Full_Name','2':'Annual_Income','3':'Credit_Score','4':'Account_Balance'}; ch=input('Field: ')
    if ch not in fields: print('Invalid choice.'); return df
    f=fields[ch]; v=input('New value: ')
    try: v=float(v) if f!='Full_Name' else v
    except ValueError: print('Invalid value.'); return df
    df.at[idx[0],f]=v; print('Customer updated.'); return df

def delete_customer(df):
    bid=input('Banking ID: '); old=len(df); df=df[df.Banking_ID.astype(str)!=bid]
    print('Customer deleted.' if len(df)<old else 'Customer not found.'); return df
