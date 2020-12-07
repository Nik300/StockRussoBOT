from BotOS_API import *
import sys
if len(args)==0:
    PyBot.SendTextMessage("ATTENSIUN POPULASIUN, QUESTO COMANDO PRENDE DEGLI ARGOMENTI,IN QUESTA MANIERA NON FA NIENTE, ATTENSIUN!")
if len(args)>0:
    if args[0]=="felice":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":smile:"))
    elif args[0]=="triste":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":frowning2:"))
if len(args)<1:
    sys.exit()
