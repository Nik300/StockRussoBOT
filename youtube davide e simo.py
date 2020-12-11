from BotOS_API import *
import sys
if len(args)==0:
    PyBot.SendTextMessage("che canale vuoi che ti linki?")
if len(args)>0:
    if args[0].lower()=="davide":
        PyBot.SendTextMessage("THE CANAL DI DAVIDE:https://www.youtube.com/user/stockdroid")
    elif args[0].lower()=="simone":
        PyBot.SendTextMessage("CANALE DI SIMONEhttps://www.youtube.com/user/MondoMOBILE00")
if len(args)<1:
    sys.exit()
