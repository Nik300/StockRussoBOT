function sistema(){
    if(args[0] == "felice"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":smile:"));
        if(args > 0 && args[1] == "risata"){
            JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":rofl:"));
    }
    
    }
    else if(args[0] == "triste"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":cry"));
        if(args > 0 && args[1] == "pianto"){
             JSBot.SendTextMessage(Utilities.ShortnameToEmoji(:sob:));
         }
    }

}
sistema();