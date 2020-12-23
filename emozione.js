function sistema(){
    if(args.length > 0 && args[0] == "felice" && args[1] == "risata"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":rofl:"));
}
    else if(args[0] == "felice"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":smile:"));
        
    
    }
    else if(args.length > 0 && args[0] == "triste" && args[1] == "pianto"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":sob:"));
    }
    else if(args[0] == "triste"){
        JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":cry:"));
       
    }

}
sistema();