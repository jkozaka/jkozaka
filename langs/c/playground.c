#include <stdio.h>
#include <string.h>
#include "jlib.h"
int main() {
    char ok=1;
    while(ok){
    char animal[5];
    fgets(animal,3,stdin);

    char lowered[5];
    for(int x = 0;x<5;x++){
        lowered[x] = lower(animal[x]);
    }
    if (strcmp(lowered, "dog\n")) {
        puts("WOOF");
    } else if (strcmp(lowered, "cat\n")) {
        puts("MEOW");
    } else {
        ok=0;
    }
    }
    return 0;
}
