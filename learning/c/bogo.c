#include <stdio.h>
#include <stdbool.h>

bool check(int tocheck[],int arrsize) {
    int x;
    for (x=0;x<arrsize-1;x++) {

        if (tocheck[x]>tocheck[x+1]) {
            return false;
        }    
    }
    return true;
}
int swap() {
    //pass
}

int main() {
    //start. (make and scramble list)
        int tosort[]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14 ,15 ,16 };
    //bogosort(check and scramble)
        while (!(check(tosort,16))) {
            //scramble
        }
        printf("done");
        return 0;
}
