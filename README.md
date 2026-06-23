## Objetivo

Desenvolver uma aplicação em Python capaz de:

* Buscar contatos armazenados no Supabase;
* Personalizar mensagens com o nome de cada contato;
* Enviar mensagens via WhatsApp utilizando a Z-API;
* Processar até 3 contatos por execução.

---

## Tabela utilizada no Supabase

<img width="461" height="156" alt="Image" src="https://github.com/user-attachments/assets/f55269eb-adce-4e8d-952f-bc898fd96d2b" />

### Contatos cadastrados

<img width="521" height="161" alt="Image" src="https://github.com/user-attachments/assets/bef8d635-1aa7-4c03-812d-cbda95d66245" />

---

## Execução da aplicação

### Execução do script Python

<img width="300" height="110" alt="Image" src="https://github.com/user-attachments/assets/36042519-8460-4662-abbb-a27756ec4c4d" />

### Mensagem recebida no WhatsApp

<img width="430" height="430" alt="Image" src="https://github.com/user-attachments/assets/307f0a55-3388-4ed3-87dc-e142ef6072d9" />

---

## Tecnologias Utilizadas

* Python
* Supabase
* Z-API
* Requests
* Python Dotenv

---

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=sua_url_no_supabase
SUPABASE_KEY=sua_chave_no_supabase

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
```

---

## Como executar o projeto

Clone o repositório:

```bash
git clone [<url-do-repositorio>](https://github.com/CodIguinhoDev/b2bflow-python-challenge)
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python main.py
```

---
Documentação:
https://developer.z-api.io/message/send-text
