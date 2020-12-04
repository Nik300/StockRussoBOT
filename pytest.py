from BotOS_API import *
def command():
	try:
        PyBot.SendTextMessage("Comando di prova installato!")
	except Exception as ex:
		PyBot.SendTextMessage("<b>Errore durante l'esecuzione di pyinstall</b>\n<i>" + str(ex) + "</i>")

command()
