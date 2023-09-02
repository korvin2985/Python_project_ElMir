from selenium.webdriver.common.by import By
import imaplib
import email
import base64



def open_email():



    imap_server = "imap.ukr.net"
    imap = imaplib.IMAP4_SSL(imap_server)

    password = "loXRbbAtCxmgSRzv"
    imap.login("oleg.test.pyt@ukr.net", password)

    imap.select("INBOX")
    UIDs = imap.search(None, "UNSEEN")
    #print(UIDs)

    res, msg = imap.fetch(b'14', '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])
    letter_from = msg["Return-path"]
    #print(letter_from)

    #Вытащить тему письма
    #text_subject = imap.fetch(b'13', "(BODY[HEADER.FIELDS (Subject)])")
    #print(text_subject)

    text_email = msg.get_payload()

    #print(text_email)
    ref = ''
    for part in msg.walk():
        if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
           # print(part.get_payload())
            message = (base64.b64decode(part.get_payload()).decode())
           # message = part.get_payload.decode()
            #charset = part.get_charset()
            #message = str(part.get_payload(decode=True), str(charset), 'ignore').encode('utf8', 'replace')
           # print(message)

            #for i in range (0,len(part.get_payload())-2):
             #   ref = ref + part.get_payload()[i]
            #print(ref)
            #return(str(ref))
    message_code = message.split(":")[1].rsplit()
    #print(message.split(":")[1])
    #print(message_code[0])

    return (message_code[0])                                                                #print(base64.b64decode(part.get_payload()).decode())


open_email()