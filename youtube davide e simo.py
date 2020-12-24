from BotOS_API import *
import sys
if len(args)==0:
    PyBot.SendTextMessage("che canale vuoi che ti linki?")
if len(args)>0:
    if args[0].lower()=="davide":
        PyBot.SendTextMessage("THE CANAL DI DAVIDE:https://www.youtube.com/user/stockdroid")
    elif args[0].lower()=="simone":
        PyBot.SendTextMessage("CANALE DI SIMONE:https://www.youtube.com/user/MondoMOBILE00")
    elif args[0].lower=="kunnash":
        PyBot.SendTextMessage("CANALE TWITCH KUNNASH:https://www.twitch.tv/kunnash")
if len(args)<1:
    sys.exit()
