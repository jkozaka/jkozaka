#include <iostream>
using namespace std;

int main() {
    int cn;

    for (cn=0;cn<101;cn++) {

        if (cn%15==0) {
            cout << "FizzBuzz";
        }

        else if (cn%5==0) {
            cout << "Buzz";
        }

        else if (cn%15==0) {
            cout << "Fizz";
        }

        else {
            cout << cn;
        }
        cout << endl;
    }
    return 0;
}
