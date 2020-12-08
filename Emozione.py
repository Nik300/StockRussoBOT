from BotOS_API import *
import sys
if len(args)==0:
    PyBot.SendTextMessage("ATTENSIUN POPULASIUN, QUESTO COMANDO PRENDE DEGLI ARGOMENTI,IN QUESTA MANIERA NON FA NIENTE, ATTENSIUN!")
if len(args)>0:
    if args[0]=="felice":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":smile:"))
    elif args[0]=="triste":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":cry:"))
    elif args[0]=="arrabbiato":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":rage:"))
    elif args[0]=="ver":
        PyBot.SendTextMessage("0.0.2")
    if args[1]=="risate"and args[0]=="felice":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":rofl:"))
if len(args)<1:
    sys.exit()
