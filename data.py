import requests
import pandas as pd

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    countries = []
    flags = []
    for index, item in enumerate(data):
        countries.append(data[index]['name']['common'])
        flags.append(data[index]['flags']['png'])

    # Converting list to dataframe
    excel_data = {'Countries': countries, 'Flags': flags}
    df = pd.DataFrame(excel_data)

    # writting to excel
    excel_file_path = 'F:\AzubiAfrica\Projects\Python\\rest_countries\countries.xlsx'
    df.to_excel(excel_file_path, index=False)
else:
    print(f"request failed with status_code: {response.status_code}")
