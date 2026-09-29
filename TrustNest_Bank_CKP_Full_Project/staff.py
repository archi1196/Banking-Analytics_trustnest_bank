import pandas as pd

def staff_login(file):
    try: df = pd.read_excel(file, sheet_name='Staff')
    except Exception as e: print('Staff data error:', e); return None
    print('\n========== STAFF LOGIN ==========')
    u = input('Username: '); p = input('Password: ')
    r = df[(df.Username.astype(str) == u) & (df.Password.astype(str) == p)]
    if r.empty: print('Invalid username or password.'); return None
    print('Login successful. Welcome,', r.iloc[0].Staff_Name, '| Role:', r.iloc[0].Role)
    return r.iloc[0]
