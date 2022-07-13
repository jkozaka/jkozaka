#include <stdio.h>

int main() {
    FILE *logs = fopen("logs","wb");
    unsigned long int initval = 2U;
    fwrite(&initval,8,1,logs);
    return 0;
}
