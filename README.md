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

<img width="341" height="84" alt="Image" src="https://github.com/user-attachments/assets/869272d9-5841-4dbf-b1e0-be974bd28dd5" />

### Mensagem recebida no WhatsApp

<img width="430" height="500" alt="Image" src="https://github.com/user-attachments/assets/30e7642b-93df-4b9d-b9cf-c67a14b3ee74" />

---

## Tecnologias Utilizadas

* Python
* Supabase
* Z-API

---
Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

Python 3.12 ou superior
Pip 24.0 ou superior
Conta no Supabase
Conta na Z-API

Verificar versões instaladas:

python --version
pip --version
--
## Configurações

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
git clone <url-do-repositorio> (https://github.com/CodIguinhoDev/b2bflow-python-challenge)
```

Crie e ative um ambiente virtual:

```bash
Para criar: python -m venv venv
Para ativar venv/Scripts/activate
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
https://www.conventionalcommits.org/en/v1.0.0/
