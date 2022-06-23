#include <stdio.h>

int main(){
    static int score;
    static char click;
    while (1){
        printf("\e[2J\e[0;0H%d\n",score);
        click = getchar();
        score++;
    }
    return 0;
}
