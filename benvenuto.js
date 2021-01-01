if(args==null)
{
    JSBot.SendTextMessage("Muso marso non hai messo se l'utente è femmina o maschio");
}
else
{
    let utente=JSBot.From.Username;
    if(args[0]=="maschio")
    {
        JSBot.ReplyVideoMessage("https://raw.githubusercontent.com/Nik300/StockRussoBOT/master/video_2021-01-01_14-48-50.mp4", utente+" ti dà il benvenuto") 
    }
    else if(args[0]=="femmina")
    {
        JSBot.ReplyVideoMessage("https://raw.githubusercontent.com/Nik300/StockRussoBOT/master/video_2021-01-01_14-48-55.mp4", utente+" ti dà il benvenuto")
    }
    else
    {
        JSBot.SendTextMessage("Muso marso hai messo una parola senza senso, devi mettere maschio o femmina");
    }
}