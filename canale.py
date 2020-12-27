from BotOS_API import *
import sys
if len(args)==0:
    PyBot.ReplyTextMessage("che canale vuoi che ti linki?")
if len(args)>0:
    if args[0].lower()=="davide":
        PyBot.ReplyTextMessage("THE CANAL YOUTUBBICO DI DAVIDE:https://www.youtube.com/user/stockdroid")
    elif args[0].lower()=="simone":
        PyBot.ReplyTextMessage("CANALE YOUTUBE DI SIMONE:https://www.youtube.com/user/MondoMOBILE00")
    elif args[0].lower()=="kunnash":
        PyBot.ReplyTextMessage("CANALE TWITCH KUNNASH:https://www.twitch.tv/kunnash")
    elif args[0].lower()=="federico":
        PyBot.ReplyTextMessage("CANALE YOUTUBE DI FEDERICO CELLA: https://www.youtube.com/channel/UCIW2dZm5e1_c21MQXrtqHSg")
if len(args)<1:
    sys.exit()
