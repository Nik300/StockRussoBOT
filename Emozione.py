from BotOS_API import *
import sys
import sys
import sys
if len(args)==0:
    PyBot.SendTextMessage("ATTENSIUN POPULASIUN, QUESTO COMANDO PRENDE DEGLI ARGOMENTI,IN QUESTA MANIERA NON FA NIENTE, ATTENSIUN!")
if len(args)>0:
    if args[0]=="felice":
        if len(args)>1 and args[1]=="risate":
            PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":rofl:"))
            sys.exit()
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":smile:"))
    elif args[0]=="triste":
        if len(args)>1 and args[1]=="pianto":
            PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":sob:"))
            sys.exit()
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":cry:"))
    elif args[0]=="arrabbiato":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":rage:"))
    elif args[0]=="ver":
        PyBot.SendTextMessage("0.0.2")
if len(args)<1:
    sys.exit()
