#include <time.h>

int playerwins = 0;
int aiwins = 0;

for(int x = 0;x<3;x++) { //each round
    clear();
    printf("\e[31;1mROUND %d\n\e[0;1mplayer:\e[35m%d\e[0m\e[1m  ai:\e[35m%d\n\n\e[0m",x+1,playerwins,aiwins); //displays points for each player

    printf("\e[1mrock");
    gets();
    printf("\e[1mpaper");
    gets();
    printf("\e[1mscissors");
    gets();
    printf("\e[1;31mSHOOT!\e[0m\n"); //visual cue to "shoot"
                                 
    char valid = 0;
    
    char shoot;
    char aishoot; //option by user and ai
                  
    char rps[][9] = {"rock","paper","scissors"};
    
    while (!(valid)) { // swap char to int. to ease checking who won
        
        char cshoot = lower(getchar()); //gets user option (rock paper or scissors)
        getchar();

        valid = 1;

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

        aishoot = srand(time(NULL)) % 3; //ai option (needs fixing keeps returning 1)
                              
    }

    printf("\e[1;35mAI: \e[0m%s\n\n",rps[aishoot]); //outputs ai choice

    if (shoot == (aishoot+1)%3) { //checks wins
        playerwins++;
        puts("\e[36;1mYOU WIN THIS ROUND\e[0m");

    } else if (aishoot == (shoot+1)%3) {
        aiwins++;
        puts("\e[36;1mAI WINS THIS ROUND\e[0m");

    } else if (aishoot == shoot) {
        puts("\e[36;1mTIE\e[0m");
        x--;
    } else {
        printf("ai:%d you:%d\n",aishoot,shoot);
    }

    gets();

}
