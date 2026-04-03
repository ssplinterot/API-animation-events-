"""
Отправка писем с GUI и логированием
Форма: адрес, тема, текст. Отправка через SMTP, лог ошибок и статуса.
Сохранение истории.
"""
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
import json
import datetime


def send_email():
  resipient = email_entry.get()
  tema = entry_tema.get()
  text_email = message.get("1.0", tk.END)

  sender = "margobolshakova49@gmail.com"
  password = "dytx priv vnxd bort"

  try:
    msg = MIMEText(text_email)
    msg["Subject"] = tema
    msg["From"] = sender
    msg["To"] = resipient
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() #шифрование
    server.login(sender, password)
    server.send_message(msg)
    print("Письмо отправлено")

    with open("log.txt", "a", encoding="UTF-8") as f: #"a" - append(добавить)
     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     f.write(f"[{now}] отправлено на адресок: {resipient}\n")

  except Exception as e:
    print(f"Ошибка при отправлке сообщения: {e}")

    with open("log.txt", "a", encoding="UTF-8") as f: 
     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     f.write(f"[{now}] не отправлено, ошибочка: {e}\n")

root = tk.Tk() 
root.title("Почтальён")
root.geometry("600x520")

#кому
tk.Label(root, text="Кому(gmail)", font=("JMH Typewriter", 20)).pack(pady=20)
email_entry = tk.Entry(root, width=40,bg= "grey" )
email_entry.pack(pady=5)  

#тема
tk.Label(root, text="Тема: ", font=("JMH Typewriter", 20)).pack(pady=20)
entry_tema = tk.Entry(root, width=40, bg= "grey")
entry_tema.pack(pady=5)  

#текст письма
tk.Label(root, text="Текст письма: ", font=("JMH Typewriter", 20)).pack(pady=20)
message = tk.Text(root, height=5, wrap="word", bg= "grey")
message.pack()

tk.Button(root, text="Отправить", command= send_email).pack()


root.mainloop()