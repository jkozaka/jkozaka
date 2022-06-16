#include <stdio.h>

int main() {
#ifdef _WIN32
    puts("use linux");
#else
    puts("nice");
#endif
    return 0;
}
