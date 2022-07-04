#include <stdio.h>
void clear() {
    printf("\e[2J\e[0;0H");
}

char lower(char tolower) {
    if (tolower >= 'A' && tolower <= 'Z') {
        tolower += 32;
    }
    return tolower;
}
