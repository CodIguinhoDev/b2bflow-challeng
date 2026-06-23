from services.message import send_message


def process_contacts(contacts: list[dict]) -> None:

    if len(contacts) == 0:
        print("Nenhum contato encontrado!")
        return

    print(f"{len(contacts)} contatos encontrados.")

    for contact in contacts[:3]:

        try:
            send_message(contact)

        except Exception as error:
            print(f"Erro ao enviar mensagem para {contact['name']}: {error}")
