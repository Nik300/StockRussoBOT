from BotOS_API import *
import sys
if len(args)==0:
    PyBot.SendTextMessage("ATTENSIUN POPULASIUN, QUESTO COMANDO PRENDE DEGLI ARGOMENTI,IN QUESTA MANIERA NON FA NIENTE, ATTENSIUN!")
if len(args)>0:
    if args[0].lower()=="felice":
        if len(args)>1 and args[1].lower()=="risata":
            PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":rofl:"))
            sys.exit()
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":smile:"))
    elif args[0].lower()=="triste":
        if len(args)>1 and args[1].lower()=="pianto":
            PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":sob:"))
            sys.exit()
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":cry:"))
    elif args[0].lower()=="arrabbiato":
        if len(args)>1 and args[1].lower()=="infuriata":
            PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":imp:"))
            sys.exit()
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":rage:"))
    elif args[0].lower()=="ver":
        PyBot.SendTextMessage("0.1.1")
    elif args[0].lower()=="list":
        PyBot.SendTextMessage("/emozione con argomenti:\n  Felice, triste ed arrabbiato.\n Rispettivi sottoargomenti:\n  Risata, pianto ed infuriata.")
    elif args[0].lower()=="sottosopra":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":upside_down:"))
    elif args[0].lower()=="cuore":
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":heart:"))
    elif args[0].lower()=="bandiera":
        if len(args)>1 and args[1].lower()=="inghilterra":
            PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":england:"))
            sys.exit()
        PyBot.SendTextMessage(Utilities.ShortnameToEmoji(":flag_it:"))
if len(args)<1:
    sys.exit()
