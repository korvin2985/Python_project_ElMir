from selenium.webdriver.common.by import By
import imaplib
import email
import base64


def open_email():
    imap_server = "imap.ukr.net"
    imap = imaplib.IMAP4_SSL(imap_server)

    password = "yd9c3J1eoEsVwzWK"
    imap.login("oleg.test.pyt@ukr.net", password)

    imap.select("INBOX")
    UIDs = imap.search(None, "UNSEEN")
    last_uid_index = str(UIDs[1][0]).rsplit()[-1].split("'")[0]
    last_uid = bytes(str(last_uid_index), 'utf-8')

    res, msg = imap.fetch(last_uid, '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])
    letter_from = msg["Return-path"]
    print(letter_from)

    for part in msg.walk():
        if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
           message = (base64.b64decode(part.get_payload()).decode())

    message_code = message.split(":")[1].rsplit()

    return (message_code[0])


#open_email()
