def get_contacts(db_connect) -> list[dict]:

    try:
        response = db_connect.table("contacts").select("*").limit(20).execute()
        return response.data

    except Exception as error:
        raise Exception(f"Erro ao buscar contatos: {error}")
