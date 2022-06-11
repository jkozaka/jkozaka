#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

int playerwins,aiwins;
playerwins = 0;
aiwins = 0;

for (int x = 0;x<3;x++) {
    clear();
    printf("\e[1mplayer:\e[35m%d\e[0m\e[1m  ai:\e[35m%d\n\n\e[0m",playerwins,aiwins); //displays points for each player

    puts("\e[1mrock");
    sleep(1);
    puts("\e[1mpaper");
    sleep(1);
    puts("\e[1mscissors");
    sleep(1);
    puts("\e[1;31mSHOOT!\e[0m");

    char shoot = getchar(); //gets user option (rock paper or scissors)
    getchar();

    int aishoot = rand() % 3;
}
