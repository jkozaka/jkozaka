#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
    int ran = srand(time(NULL));
    printf("%d",ran);
}
