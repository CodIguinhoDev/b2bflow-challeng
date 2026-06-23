from supabase import Client, create_client
from dotenv import load_dotenv
import os

load_dotenv()


def connect() -> Client:
    try:
        return create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    except Exception as error:
        raise Exception(f"Erro ao conectar com o Supabase: {error}")
