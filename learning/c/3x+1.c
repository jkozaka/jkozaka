#include <stdio.h>
int main() {
    unsigned long currentn;
    for (unsigned long n = 1U; n<=18446744073709551615U; n++) { //goes through all numbers that can be represented with 64 bits
        currentn = n;
#ifdef _WIN32
    system("cls");
    printf("%lu\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\e[0m",n);
#else
        printf("\e[2J\e[0;0H\e[31;1m%lu\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\e[0m\n",n);
#endif
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
            printf("%lu ",currentn);
        }
        
        printf("\n");
    }

    return 0;
}
