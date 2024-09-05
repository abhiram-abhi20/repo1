import openpyxl

def get_list_from_excel():
    credentials = openpyxl.load_workbook("creds.xlsx")
    login_creds=credentials["login_creds"]
    credentials_list=[]
    for row in range(1,5):
        nested_creds=[]
        for column in range(1,3):
            data=login_creds.cell(row,column)
            nested_creds.append(data.value)
        credentials_list.append(nested_creds)
    return credentials_list