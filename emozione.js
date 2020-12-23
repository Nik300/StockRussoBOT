function sistema(){
    if(args > 0 && args[1] == "risata"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":rofl:"));
}
    if(args[0] == "felice"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":smile:"));
        
    
    }
    else if(args > 0 && args[1] == "pianto"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":sob:"));
    }
    if(args[0] == "triste"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":cry:"));
       
    }

}
sistema();