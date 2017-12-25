# Modul mdmail, enthaelt Funktionen zum Kontakt mit Mailserver und Extraktion
# der Inhalte.

# CONFIG
Mail_User = "captain.proboat@gmail.com"
Mail_Paswd = "ub6-NdW-dv2-z3e"
Mail_Imap = "imap.gmail.com"
Mail_ImapPort = 993
Mail_Smtp = "smtp.gmail.com"

import imaplib

# Funktion GetURLFromMail, ruft neuste E-Mail ab, extrahiert Shortlink
# und gibt diesen zurueck
def GetURLFromMail():
 im = imaplib.IMAP4_SSL(Mail_Imap, Mail_ImapPort) # Verbindung aufbauen
 im.login(Mail_User, Mail_Paswd) ### LOGIN
 
 print(im.list())
 
 im.logout() ### LOGOUT
 
print(GetURLFromMail()) # test
