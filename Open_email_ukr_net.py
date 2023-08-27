from selenium.webdriver.common.by import By
import imapclient
import imaplib
import email
import pprint


def open_email():



imap_server = "imap.ukr.net"
imap = imaplib.IMAP4_SSL(imap_server)





##imapObj = imapclient.IMAPClient('imap.ukr.net',ssl=True)
password = "loXRbbAtCxmgSRzv"

imap.login("oleg.test.pyt@ukr.net", password)
imap.select("INBOX")
UIDs = imap.search(None, "UNSEEN")
print(UIDs)
res, msg = imap.fetch(b'9', '(RFC822)')
msg = email.message_from_bytes(msg[0][1])
letter_from = msg["Return-path"]
print(letter_from)
##imapObj.login("oleg.test.pyt@ukr.net", password)
# print(imapObj.list_folders())

##imapObj.select_folder('Inbox', readonly=True)
# UIDs=imapObj.search(['FROM edkhut@gmail.com'])

##UIDs = imapObj.search(['UNSEEN'])
##rawMess = imapObj.fetch(UIDs,['BODY[]'])

##pprint.pprint(rawMess)