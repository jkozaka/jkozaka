#include <stdio.h>
#ifdef _WIN32
#define CALCULATOR "calculator"
#else
#define CALCULATOR "kcalc"
#endif

int main() {
    while(1){
        puts("YOU GOT HACKED!");
        system(CALCULATOR);
    }
}
