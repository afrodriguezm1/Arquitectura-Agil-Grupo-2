import pandas as pd
import requests
import json
import time

df = pd.read_excel (r'datos1.xlsx',sheet_name='MOCK_DATA', engine='openpyxl')
url = df['URL'].tolist()
verbo = df['VERBO'].tolist()
nombre = df['NOMBRE'].tolist()
f = open('evidencia.txt', 'a')
for x in range (len(url)):
    time.sleep(1)
    if(verbo[x]=='POST'):
        r = requests.post(url[x], json = {'nombre':nombre[x]})
        f.write(str(nombre[x]) + "," + str(verbo[x]) + "," + str(r.status_code)+"\n")
    elif(verbo[x]=='GET'):
        r = requests.get(url[x])
        f.write(str(nombre[x]) + "," + str(verbo[x]) + "," + str(r.status_code)+"\n")
f.close()
