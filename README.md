# Configurações para automação do Kolibri Studio

- Precisa do python instalado no computador/vm
- Instalar a biblioteca playwright

```jsx
pip install pytest-playwright
```

- Instalar os browser que ela pede

```jsx
playwright install
```

- Talvez seja necessário instalar algumas dependências do Visual Studio para que o playwright rode, se precisar ele vai pedir no console. No caso do PC domestico apareceu que necessita de instalar a ferramenta para programar em C++, deu um total de 6GB para instalar
- Precisa criar credenciais no Google console ou reutilizar as que já existem.
- Baixar as credenciais em JSON e passar para o código
- Instalar a biblioteca da API

```jsx
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```