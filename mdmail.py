# Modul mdmail, enthaelt Funktionen zum Kontakt mit Mailserver und Extraktion
# der Inhalte.

# CONFIG
Mail_User = "captain.proboat@gmail.com"
Mail_Paswd = "ub6-NdW-dv2-z3e"
Mail_Imap = "imap.gmail.com"
Mail_ImapPort = 993
Mail_Smtp = "smtp.gmail.com"

import imaplib
import re
import base64
import mdgps

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
 
 mailid_max = None
 for id in mailids[1][0].split(): # Maximale ID herausfinden
  mailid_max = id
  
 if mailid_max == None:
  return None
  
 mail_content = im.fetch(mailid_max, "(BODY[TEXT])")
 if re.search(r"base64", str(mail_content)) == "base64": # falls E-Mail base64-codiert ist
  mail_content = base64.decode(mail_content)
  print("base64")
 
 for id in mailids[1][0].split(): # Alle Mails mit den besagten IDs loeschen
   im.store(id, '+FLAGS', '\\Deleted')
 im.expunge()

 im.logout() ### LOGOUT
 
 shortlink_match = re.search('https://goo.gl.*"', str(mail_content)) # Shortlink auslesen
 shortlink = re.sub('"', '', shortlink_match.group(0)) # kuerzen des Stringteils des Matchobjekts

 coordinates = [0][0]
 coordinates = mdgps.GetGooglePosition(shortlink)
 return coordinates
