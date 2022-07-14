#include <stdio.h>
int main(){
    puts("\033[2J\033[0;0H\n\n");                   //clears screen, goes to start of write
    char towrite[64];
    int  location;
    while(1) {
        location = SEEK_CUR;                        //saves location, (to write at later)       not working

        printf("\033[0;0H");                        //goes to spot to get append prompt
        printf("\033[2K");                          //clears line ftr input

        fgets(towrite, 64, stdin);                  //gets text to append
             
        fseek(stdout, (long) location, SEEK_SET);   //goes to append spot                       also doesnt work
        printf("\033[A%s",towrite);                 //appends text
    }
    return 0;
}
