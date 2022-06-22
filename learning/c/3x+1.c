
//only for linux (can run on windows, but with ansi)

#include <stdio.h>
int main() {
    unsigned long currentn;
    for (unsigned long n = 1U; n<=18446744073709551615U; n++) { //goes through all numbers that can be represented with 64 bits
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
            printf("\r\033[31;1m%lu \033[0m%lu ",n,currentn);
            x++;
        }
        
        printf("\033[1;32m✓%d\033[0m\n",x);
    }

    return 0;
}
