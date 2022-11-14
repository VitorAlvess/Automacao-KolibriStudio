from playwright.sync_api import sync_playwright
import time
import os
import json


with open("config.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo config com usernames e passwords
    dados = json.load(meu_json)

UsernameKolibri = dados["kolibri"]["username"]
PasswordKolibri = dados["kolibri"]["password"]
UsernameGoogle = dados["google"]["username"]
PasswordGoogle = dados["google"]["password"]

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, downloads_path= os.getcwd()) #Colocar true depois
    pagina = navegador.new_page()
    pagina.set_default_timeout(6000) #set o tempo que vai esperar por uma ação
    pagina.goto("http://185.211.4.249/pt-br/facility/#/data")
    pagina.locator('xpath=/html/body/div[1]/div[3]/div/div/p[2]/a').click()
    pagina.fill('xpath=//*[@id="username"]/div/div/label/input', UsernameKolibri)
    pagina.locator('xpath=//*[@id="main"]/div/div/div[1]/div/div/div[1]/form/div/div[3]/button').click()
    pagina.fill('xpath=//*[@id="password"]/div/div/label/input',PasswordKolibri)
    pagina.locator('xpath=//*[@id="main"]/div/div/div[1]/div/div/div[1]/form/div[2]/div[2]/button/span').click()

    with pagina.expect_download() as download_info:
        # Perform the action that initiates download
        pagina.locator('xpath=//*[@id="main"]/div/div[1]/div/div/div[3]/div/p[2]/button').click()
        download = download_info.value
        # Wait for the download process to complete
        print(download.path())
        # Save downloaded file somewhere
        working_dir_path= os.getcwd()
        final_path = os.path.join(working_dir_path, 'data/myfile.csv')
        download.save_as(final_path)
        
    # pagina.locator('xpath=//*[@id="main"]/div/div[1]/div/div/div[3]/div/p[3]/a/span').click() #gerar novo relatorio
   

    time.sleep(5)
    pagina.goto("https://docs.google.com/spreadsheets/d/1Poy26SomDLI_JbJ7Cj8gwPcw5Kr-T_XvwiJ9Kk6D3sk")
    pagina.fill('xpath=//*[@id="identifierId"]', UsernameGoogle) #Login Google
    pagina.locator('xpath=//*[@id="identifierNext"]/div/button/span').click() #Avançar
    pagina.fill('xpath=//*[@id="password"]/div[1]/div/div[1]/input', PasswordGoogle) #Senha Google
    pagina.locator('//*[@id="passwordNext"]/div/button/span').click() #Avançar
    time.sleep(10)
    pagina.locator('xpath=//*[@id="docs-file-menu"]').click() #Arquivo
    pagina.locator('xpath=//*[@id=":5a"]').click() #Importar
    time.sleep(5)
    pagina.locator('xpath=//*[@id=":3"]/div').click() #upload
    pagina.locator('xpath=//*[@id=":8"]/div').click() #upload
    pagina.locator('xpath= //*[@id=":11"]/div').click() #upload




    time.sleep(6)








    