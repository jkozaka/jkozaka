#include <iostream>
using namespace std;

int main() {

    int ToProcess;
    cin >> ToProcess;

    if (ToProcess%2==0) {
        cout << "Even";
    }

    else {
        cout << "Odd";
    }
    cout << endl;
    return 0;
}
