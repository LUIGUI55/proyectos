#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Introduce tres números: ";
    cin >> a >> b >> c;

    if (a >= b && a >= c) {
        cout << "El mayor es: " << a << endl;
    } else if (b >= a && b >= c) {
        cout << "El mayor es: " << b << endl;
    } else {
        cout << "El mayor es: " << c << endl;
    }
    return 0;
}