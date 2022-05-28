#include <stdio.h>

int main() {

    int num;

    for (num=1;num<101;num++) { //runs 101 times from 1 to 100
                                
        // if num divisible by x say y

        if (num%15==0) {        //x:15 y:fizzbuzz 
            printf("\033[41mFizzBuzz\033[0m");
        }

        else if (num%5==0) {    //x:5 y:buzz
            printf("\033[41mBuzz\033[0m");
        }

        else if (num%3==0) {    //x:3 y:fizz
            printf("\033[41mFizz\033[0m");
        }

        else {                  //x:neither y:num
            printf("%d",num);
        }

        printf("\n");

    }
    while (1){}
    return 0;
}
