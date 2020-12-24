function sistema(){
    if(args != null){
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
        else if(args.length > 0 && args[0] == "arrabbiato" && args[1] == "infuriata"){
            JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":imp:"));
        }
        else if(args[0] == "arrabbiato"){
            JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":rage:"));
        }
        else if(args[0] == "ver"){
            JSBot.SendTextMessage("js 0.0.1");
        }
        else if(args[0] == "list"){
            JSBot.SendTextMessage("/emozione con argomenti:\n  Felice, triste ed arrabbiato.\n Rispettivi sottoargomenti:\n  Risata, pianto ed infuriata.");
        }
        else if(args[0] == "sottosopra"){
            JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":upside_down:"));
        }
        else if(args[0] == "cuore"){
            JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":heart:"));
        }
        else if(args.length > 0 && args[0] == "bandiera" && args[1] == "inghilterra"){
            JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":england:"));
        }
        else if(args.length > 0 && args[0] == "bandiera" && args[1] == "italia"){
            JSBot.SendTextMessage(Utilities.ShortnameToEmoji(":flag_it:"));
        }
    }
    else
        JSBot.SendTextMessage("ATTENSIUN POPULASIUN, QUESTO COMANDO PRENDE DEGLI ARGOMENTI,IN QUESTA MANIERA NON FA NIENTE, ATTENSIUN!")
}
sistema();