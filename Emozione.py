from BotOS_API import *
import sys
if len(args)==0:
    PyBot.SendTextMessage("ATTENSIUN POPULASIUN, QUESTO COMANDO PRENDE DEGLI ARGOMENTI,IN QUESTA MANIERA NON FA NIENTE, ATTENSIUN!")
if len(args)>0:
    if args[0]=="felice":
        Utilities.ShortnameToEmoji(":(::")
    elif args[0]=="triste":
        Utilities.ShortnameToEmoji("::):")
if len(args)<1:
    sys.exit()
