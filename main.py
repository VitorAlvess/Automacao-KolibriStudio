from __future__ import print_function
from playwright.sync_api import sync_playwright
import time
import os
import json

#Imports do upload google sheeets
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import datetime
data = datetime.datetime.now()





#Parte de baixar os dados (O certo é isso estar dentro de um Def)
with open("config.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo config com usernames e passwords
    dados = json.load(meu_json)

UsernameKolibri = dados["kolibri"]["username"]
PasswordKolibri = dados["kolibri"]["password"]


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, downloads_path= os.getcwd()) #Colocar true depois
    pagina = navegador.new_page()
    pagina.set_default_timeout(200000) #set o tempo que vai esperar por uma ação 1200000 = 20 min
    pagina.goto("http://185.211.4.249/pt-br/facility/#/data")
    pagina.locator('xpath=/html/body/div[1]/div[3]/div/div/p[2]/a').click()
    pagina.fill('xpath=//*[@id="username"]/div/div/label/input', UsernameKolibri)
    pagina.locator('xpath=//*[@id="main"]/div/div/div[1]/div/div/div[1]/form/div/div[3]/button').click()
    pagina.fill('xpath=//*[@id="password"]/div/div/label/input',PasswordKolibri)
    pagina.locator('xpath=//*[@id="main"]/div/div/div[1]/div/div/div[1]/form/div[2]/div[2]/button/span').click()
    pagina.locator('xpath=//*[@id="main"]/div/div[1]/div/div/div[3]/div/p[3]/a/span').click() #gerar novo relatorio
    time.sleep(5)
    
   
    with pagina.expect_download() as download_info:
        # Perform the action that initiates download
        pagina.locator('xpath=//*[@id="main"]/div/div[1]/div/div/div[3]/div/p[2]/button').click()
        download = download_info.value
        # Wait for the download process to complete
        print(download.path())
        # Save downloaded file somewhere
        working_dir_path= os.getcwd()
        final_path = os.path.join(working_dir_path, 'dados.csv')
        download.save_as(final_path)
        
   

    time.sleep(5)
   
#Parte de mandar para planilha



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Poy26SomDLI_JbJ7Cj8gwPcw5Kr-T_XvwiJ9Kk6D3sk'
SAMPLE_RANGE_NAME = 'dados!A:L'


def main():
   
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        #Passar valores
        sheet = service.spreadsheets()
        valores_adicionar = [
            
        ]
        with open('dados.csv', mode='r', encoding="utf8") as ficheiro:
            reader = csv.reader(ficheiro, delimiter=',')
            for linha in reader:
                valores_adicionar.append(linha)
        horario_atual = [
        [f"Gerado no dia {data.day}/{data.month}/{data.year} as {data.hour} h {data.minute} min {data.second} s."]
        ]
    
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME, valueInputOption="RAW", body={'values': valores_adicionar}).execute()
        result2 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range='dados!M1', valueInputOption="RAW", body={'values': horario_atual}).execute()
        
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()






    