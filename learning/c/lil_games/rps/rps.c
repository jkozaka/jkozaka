#include "rps.h"

void help() {
    puts("Welcome to \e[1mrock paper scissors\e[0m.");
    puts("The game is quite simple.");
    puts("when it says: \e[1mrock,paper scissors,\e[0mpress enter until it says \"\e[31;1mSHOOT!\e[0m\"");
    puts("then type \e[1mR,P or S\e[0m, meaning rock, paper or scissors, in that order.");
    puts("Hope that the AI wont randomly pick the winning option\n");
}

int main() {

    getchar(); //wait until enter to be pressed. to help errors be viewed

    char choice = '0';
        
    clear();
    while (choice!='s') {

        puts("\e[35mwelcome. type \e[1;34mh\e[0m\e[35m for help and \e[1;34ms\e[0m\e[35m to play\e[0m");
        choice = lower(getchar()); //gets character to see if was certain operation

        clear();

        switch (choice) {

            case 'h':
                clear();
                help();//displays help
                break;

            default:
                puts("invalid answer");
                break;
        }
        getchar(); //sweeps away remaining chars
    }
    clear();
    
#include "game.c"
    return 0;
}
