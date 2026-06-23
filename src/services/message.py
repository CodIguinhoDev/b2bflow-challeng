from dotenv import load_dotenv
import requests
import os

load_dotenv()

url = f"https://api.z-api.io/instances/{os.getenv('ZAPI_INSTANCE_ID')}/token/{os.getenv('ZAPI_TOKEN')}/send-text"


def get_payload(contact) -> dict:
    return {
        "phone": contact["telephone"],
        "message": f"Olá, {contact["name"]} tudo bem com você?",
    }


def get_headers() -> dict:
    return {
        "Client-Token": os.getenv("ZAPI_CLIENT_TOKEN"),
        "Content-Type": "application/json",
    }


def send_message(contact) -> None:
    try:
        payload = get_payload(contact)
        headers = get_headers()

        requests.post(url, json=payload, headers=headers)
        print(f"Mensagem enviada: {payload["message"]}")

    except Exception as error:
        raise Exception(f"Erro ao enviar mensagem: {error}")
