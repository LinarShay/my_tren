def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if not ("@" in recipient and recipient.endswith((".com", ".ru", ".net"))) or \
       not ("@" in sender and sender.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("Привет!", "student@example.com")  # Отправка с адреса по умолчанию
send_email("Привет!", "student@example.com", sender="admin@website.net")  # Нестандартный отправитель
send_email("Привет!", "admin@website")  # Некорректный адрес
send_email("Привет!", "university.help@gmail.com")  # Отправка самому себе
