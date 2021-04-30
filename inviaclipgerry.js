function buonasuora(){
    if(args == null){
        JSBot.SendTextMessage("MA CHE CLIP VUOI?");
        return;
    }
    if(args[0] == "auguri"){
        JSBot.SendVideoMessage("https://raw.githubusercontent.com/Nik300/StockRussoBOT/master/AUGURI!.mp4");
    }
} 
buonasuora(); 