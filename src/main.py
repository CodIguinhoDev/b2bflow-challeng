from controllers.contact_controller import process_contacts
from services.contacts import get_contacts
from database.connection import connect
from datetime import datetime


def main() -> None:

    db_connect = connect()
    contacts = get_contacts(db_connect)
    process_contacts(contacts)

    print(f"Data e Horário: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")


if __name__ == "__main__":
    main()
