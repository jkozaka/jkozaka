
//only for linux (some libraries not supported)

#include <sys/ioctl.h>
#include <stdio.h>
#include <unistd.h>
#include <math.h>
int main() {

    FILE *f;
    f = fopen("logs", "rb+"); 
    

    if (!f) {
        puts("error reading file.");
        return 0;
    } else {


    unsigned long currentn; //processing number
    unsigned long n; //number being processed

    for (fread(&n, 8, 1, f); n<18446744073709551615UL; n++) { //goes through all numbers that can be represented with 64 bits

        struct winsize w;
        ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);

        rewind(f);
        fwrite(&n , 8, 1, f);

        
        currentn = n;
        int x = 0;

            //until currentn is 1,
            //if currentn is odd, multiply currentn by 3 and add 1
            //if currentn is even, divide by 2

        while (currentn != 1) {
            switch (currentn%2) {
                case 0:
                    currentn /= 2;
                    break;

                case 1:
                    currentn = currentn * 3 + 1;
                    break;
            }
            printf("\r\033[31;1m%lx \033[0m%lx ",n,currentn); //SHOWING CURRENT STATUS
            x++;
        }

        
        
        printf("\033[1;32m✓%d\r\033[%dC\033[0;1;36m%lx\n",x,w.ws_col - 20,(unsigned long int) pow(2,64) - n); //FINAL OUTPUT (how many steps it takes to get to 1 , percentage complete)
    }
    }

    printf("\n\033[41;5mCOMPLETE SUCSESSFULLY!!!!!");

    return 0;
}
