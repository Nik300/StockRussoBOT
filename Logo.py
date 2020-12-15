from BotOS_API import *
import sys
if len(args)== 0:
    PyBot.SendTextMessage("MUSO MARSO CHE LOGO VUOI?")
if len(args)>0:
    if args[0].lower()=="botos":
        PyBot.SendImageMessage("https://raw.githubusercontent.com/Nik300/StockRussoBOT/master/BotOS.jpg")
if len(args)<1:
    sys.exit()
