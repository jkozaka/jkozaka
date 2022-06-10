#include <stdio.h>
#include <stdlib.h>

void help() {
    puts("Welcome to \e[1mrock paper scissors\e[0m.");
    puts("The game is quite simple.");
    puts("say \e[1mR,P or S\e[0m, meaning rock, paper or scissors, in that order.");
    puts("Hope that the AI wont randomly pick the winning option");

}
void game() {
    //
}

int main() {
start:
    puts("welcome. type \e[1mh\e[0m for help and \e[1ms\e[0m to play");
    char choice = getchar(); //gets character to see if was certain operation

    puts("\e[2J\e[0;0H"); //clears terminal

    if (choice=='h') {
        help();
        goto start; //help info

    } else if (choice=='s') {
        game(); //a

    } else {
        puts("invalid answer\n");
        goto start;
    }
    return 0;
}
