import win32com.client as win32

def send_email(to_address, subject, body):
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)  # 0 значить olMailItem - новий лист
    mail.To = to_address
    mail.Subject = subject
    mail.Body = body
    mail.Send()

# Приклад використання:
recipients = ["email1@example.com", "email2@example.com", "email3@example.com"]
greeting_message = "Доброго дня, {name}! Це вітальний лист від вас."

for recipient in recipients:
    # Ваше ім'я чи текст для вставки в лист
    name = "Ім'я Одержувача"
    personalized_message = greeting_message.format(name=name)

    # Відправити лист
    send_email(recipient, "Вітальний лист", personalized_message)