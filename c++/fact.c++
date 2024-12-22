#include <iostream>
using namespace std;

int main() {
    int num;
    unsigned long long factorial = 1;

    cout << "Introduce un número positivo: ";
    cin >> num;

    for (int i = 1; i <= num; i++) {
        factorial *= i;
    }

    cout << "El factorial de " << num << " es: " << factorial << endl;
    return 0;
}