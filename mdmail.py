# Modul mdmail, enthaelt Funktionen zum Kontakt mit Mailserver und Extraktion
# der Inhalte.

# CONFIG
Mail_User = "captain.proboat@gmail.com"
Mail_Paswd = "ub6-NdW-dv2-z3e"
Mail_Imap = "imap.gmail.com"
Mail_ImapPort = 993
Mail_Smtp = "smtp.gmail.com"

import imaplib

# Funktion GetTargetFromMail, ruft neuste E-Mail ab, extrahiert Shortlink
# und bestimmt die Position daraus (via Internet) und gibt Koordinaten
# als Liste zurueck, oder "none", wenn keine neue Mail eingetroffen ist
def GetTargetFromMail():
 im = imaplib.IMAP4_SSL(Mail_Imap, Mail_ImapPort) # Verbindung aufbauen
 # falls gmail verwendet wird, muss dort Zugriff von unsicheren Apps
 # erlaubt werden, sonst muesste xauth2 implementiert werden
 im.login(Mail_User, Mail_Paswd) ### LOGIN
 
 im.select("INBOX")
 mailids = im.search(None, '(SUBJECT "Gesetzte Markierung")') # IDs liegen an zweiter Listenstelle, wiederum als Liste
 
 for id in mailids[1][0].split(): # Maximale ID herausfinden
  mailid_max = id
  
 mail_content = im.fetch(mailid_max, "(BODY[TEXT])")
 print(mail_content)
 
 for id in mailids[1][0].split(): # Alle Mails mit den besagten IDs loeschen
   im.store(id, '+FLAGS', '\\Deleted')
 im.expunge()

 im.logout() ### LOGOUT
 
 # Was noch fehlt:
 # 1) "none"-Rueckgabe, falls keine neue Mail
 # 2) Link aus mail_content auslesen
 # 3) Linkuebergabe an GetGooglePosition(url), die Positionsdaten ermittelt, mit return
 
print(GetTargetFromMail()) # test
