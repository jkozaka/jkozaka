int playerwins,aiwins;
playerwins = 0;
aiwins = 0;

for (int x = 0;x<3;x++) {
    clear();
    printf("\e[1mplayer:\e[35m%d\e[0m\e[1m  ai:\e[35m%d\n\n\e[0m",playerwins,aiwins); //displays points for each player

    printf("\e[1mrock");
    gets();
    printf("\e[1mpaper");
    gets();
    printf("\e[1mscissors");
    gets();
    printf("\e[1;31mSHOOT!\e[0m\n"); //visual cue to "shoot"
                                 
    char valid = 1;
    
    char shoot;
    char aishoot; //option by user and ai
    
    do { // swap char to int. to ease checking who won
        
        char cshoot = lower(getchar()); //gets user option (rock paper or scissors)
        getchar();

        switch (cshoot) {
            case 'r':
                shoot = 0;
                break;
            case 'p':
                shoot = 1;
                break;
            case 's':
                shoot = 2;
                break;
            default:
                valid = 0;
                break;      //conversion. if neither, of predefined options, restarts
            
        }


        aishoot = rand() % 3; //ai option

    } while (!(valid));

    char winner;

    if (shoot == (aishoot+1)%3) {
        winner = 0;
    } else if (aishoot == (shoot+1)%3) {
        //
    } else {
        //
    }

}
