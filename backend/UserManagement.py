import pandas as pd

excel_file_path = 'backend/user_data.xlsx'
df = pd.read_excel(excel_file_path, engine='openpyxl')
# Strip whitespace from both 'Email' and 'Password' columns
df['Email'] = df['Email'].astype(str).str.strip()
df['Password'] = df['Password'].astype(str).str.strip()

def insertCredentials (first_name, last_name, age, gender, email, password, verify_pass, country, city, 
                        street_ap, primary_inst, second_inst, genre, level):
    new_user = pd.DataFrame({'First': [first_name], 'Last': [last_name], 'Age': [age], 'Gender': [gender],'Email': [email], 
                                'Password': [password], 'Verify': [verify_pass], 'Country': [country], 'City': [city],
                                'Street, appartment': [street_ap],'Primary Instrument': [primary_inst], 
                                'Secondary instrument': [second_inst], 'Genre': [genre], 'Level': [level]})
    global df
    global excel_file_path
    df = pd.concat([df, new_user], ignore_index=True)
    with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, index=False)
    print(df)

def checkCredentials (email, password) -> bool:
    for index, row in df.iterrows():
        if row['Email'] == email and row['Password'] == password:
            return True
    return False
    
