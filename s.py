# -*- coding:utf 8 -*-
import imaplib
import email
import unicodedata

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('foldesi.zsombor@gmail.com', 'Lak3c0m0easya42')
mail.list("inbox")

mail.select("inbox") # connect to inbox.
print mail.select("inbox")
result, data = mail.uid('search', None, 'ALL')
uids = data[0].split()




for i in range(1,4):
    typ, msg_data = (mail.fetch(str(i), '(RFC822)'))
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in ['subject','to','from']:
                print unicode('%-8s: %s' % (header.upper(), msg[header]))

