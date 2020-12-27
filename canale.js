function canali(){
    if(args == null){
        JSBot.SendTextMessage("che canale vuoi che ti linki?");
        return;
    }
    else if(args[0] == "davide"){
        JSBot.SendTextMessage("THE CANAL YOUTUBBICO DI DAVIDE:https://www.youtube.com/user/stockdroid");
    }
    else if(args[0] == "simone"){
        JSBot.SendTextMessage("CANALE YOUTUBE DI SIMONE:https://www.youtube.com/user/MondoMOBILE00");
    }
    else if(args[0] == "kunnash"){
        JSBot.SendTextMessage("CANALE TWITCH KUNNASH:https://www.twitch.tv/kunnash");
    }
    else if(args[0] == "federico"){
        JSBot.SendTextMessage("CANALE YOUTUBE FEDERICO CELLA:https://www.youtube.com/channel/UCIW2dZm5e1_c21MQXrtqHSg");
    }
}
canali();