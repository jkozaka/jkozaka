#include <stdio.h>
#include <stdlib.h>

void help() {
    puts("Welcome to \e[1mrock paper scissors\e[0m.");
    puts("The game is quite simple.");
    puts("say \e[1mR,P or S\e[0m, meaning rock, paper or scissors, in that order.");
    puts("Hope that the AI wont randomly pick the winning option\n");
}

void clear() {
    puts("\e[2J\e[0;0H");
}

int main() {

    getchar();getchar();

    char choice = '0';
        
    clear();
    while (choice!='s') {

        puts("\e[35mwelcome. type \e[1;34mh\e[0m\e[35m for help and \e[1;34ms\e[0m\e[35m to play\e[0m");
        choice = getchar(); //gets character to see if was certain operation

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
