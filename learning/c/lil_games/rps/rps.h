#include <stdio.h>
#include <stdlib.h>
void clear() {
    puts("\e[2J\e[0;0H");
}

char lower(char tolower) {
    if (tolower >= 'A' && tolower <= 'Z') {
        tolower += 32;
    }
    return tolower;
}
