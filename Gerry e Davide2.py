from BotOS_API import *
if args is None:
    PyBot.SendTextMessage("MUSO MARSO NON TI DIMENTICARE CHE QUESTO COMANDO PRENDE DEGLI ARGOMENTI!!!!!!!")
if args is not None:
    if args[0]=="Davide":
        PyBot.SendTextMessage("MA SIAMO AL MILITARE QUI!!!!!!")
    if args[1]=="Gerry":
        PyBot.SendTextMessage("<b>MA NOOO MA NON È VERO!!!</b>")
if len(args)<2:
    sys.exit()
