#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool check(int ToChek[],int ToChekSiz) {
    int x;
    for (x=0;x<ToChekSiz-1;x++) {

        if (ToChek[x]>ToChek[x+1]) {
            return false;
        }    
    }
    return true;
}

void scramble(int ToScram[],int ToScramSiz) {
    static int *Scram = malloc(ToScramSiz);
    memcpy(Scram,ToScram,ToScramSiz);
    

    for (int y=0;y<100;y++) {

        int swapindex[] = {rand()%ToScramSiz,rand()%17};
        int swapbuffer[]={Scram[swapindex[0]],Scram[swapindex[1]]};

        Scram[swapindex[0]]=swapbuffer[1];
        Scram[swapindex[1]]=swapbuffer[0];
    }
    //return ToScram;
}
int main() {
    //start. (make and scramble list)
    int tosort[]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14 ,15 ,16 };
    scramble(tosort,16);
    tosort = Scram;

    //bogosort(check and scramble)
    while (!(check(tosort,16))) {
        scramble(tosort,16);
        tosort = Scram;
        printf("working");
    }
    printf("\ndone");
    return 0;
}
