#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Introduce un número: ";
    cin >> num;

    if (num % 2 == 0) {
        cout << num << " es par." << endl;
    } else {
        cout << num << " es impar." << endl;
    }
    return 0;
}
