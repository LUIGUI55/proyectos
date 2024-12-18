#include <iostream>
using namespace std;

int cuadrado(int num) {
    return num * num;
}

int main() {
    int num;
    cout << "Introduce un número: ";
    cin >> num;
    cout << "El cuadrado es: " << cuadrado(num) << endl;
    return 0;
}
