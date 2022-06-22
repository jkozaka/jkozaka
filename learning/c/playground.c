#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int times0,times1,times2;
    for(int x = 0;x<100;x++) {
        //srand(time(NULL)+x);
        printf("%d\n",rand() % 3);
        x++;
    }
    return 0;
}
