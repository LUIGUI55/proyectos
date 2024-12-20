#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int* ptr = &a;

    cout << "Valor de a: " << a << endl;
    cout << "Dirección de a: " << ptr << endl;
    cout << "Valor usando el puntero: " << *ptr << endl;

    return 0;
}

