# Automação de geração de relatórios do Kolibri Studio subindo para o Google Sheets

# Ideia do projeto

- Criar um script que consiga:
    - Gerar e salvar relatórios do Kolibri ✅
    - Tratar os dados que são baixados ✅
    - Subir para o Google Sheets todos os dados ✅
    - Realizar todos os passos anterior de forma automática a partir de determinado critério

# Configurações:

- Instalação do [python](https://www.python.org/)
- Instalar a biblioteca [playwright](https://playwright.dev)

```jsx
pip install pytest-playwright
```

- Instalar os browser que ela pede

```jsx
playwright install
```

- é necessário instalar algumas dependências do Visual Studio para que o playwright rode, se precisar ele vai pedir no console.  necessita de instalar a ferramenta desenvolvimento para desktop com C++, deu um total de 1~GB para instalar



- Criar um arquivo <b>config.json</b> e inserir dados referente a username e password do Kolibri

```jsx
{
    "kolibri":{
        "username": "username",
        "password": "password"
    }
}
```

- Instalar a biblioteca da API do [Google Sheets](console.cloud.google.com/apis/api/sheets.googleapis.com/)

```jsx
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

- Precisa criar credenciais no Google console ou reutilizar as que já existem.

```jsx
Console -> APIs e serviços -> Credenciais
```

- Baixar as credenciais em JSON e inserir na pasta do projeto
