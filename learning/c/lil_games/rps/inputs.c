#include <stdio.h>
#include <string.h>

int main() {
    char in[2];
    scanf("%s",in);
    
    if (!(strcmp(in,"hi"))) puts("you said hi");

    return 0;
}
