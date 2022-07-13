#include <stdio.h>
int main() {
    fprintf(stdout, "lorem ipsum");
    fprintf(stdout,"%d",(int)ftell(stdout)); //i give up
    return 0;
}
