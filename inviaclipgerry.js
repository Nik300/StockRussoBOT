function buonasuora(){
    if(args == null){
        JSBot.SendTextMessage("MA CHE CLIP VUOI?");
        return;
    }
    if(args[0] == "auguri"){
        JSBot.SendVideoMessage("https://raw.githubusercontent.com/Nik300/StockRussoBOT/master/AUGURI!.mp4");
    }
    else if(args[0] == "allora"){
        JSBot.SendVideoMessage("https://raw.githubusercontent.com/Nik300/StockRussoBOT/master/ALLORA.mp4");
    }
    else if(args[0] == "info"){
        JSBot.SendTextMessage("Comando che invia clip di gerry, come argomento metti cosa è detto nella clip abbiamo per ora: auguri e allora");
    }
    else if(args[0] == "ver"){
        JSBot.SendTextMessage("0.0.1")
    } 
} 
buonasuora();