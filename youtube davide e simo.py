from BotOS_API import *
import sys
if len(args)==0:
    PyBot.SendTextMessage("che canale vuoi che ti linki?")
if len(args)>0:
    if args[0]=="davide":
        PyBot.SendTextMessage("https://www.youtube.com/results?search_query=stockdroid")
    elif args[0]=="simone":
        PyBot.SendTextMessage("https://www.youtube.com/results?search_query=simone+russo")
if len(args)<1:
    sys.exit()
