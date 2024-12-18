#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Introduce la cantidad de números Fibonacci: ";
    cin >> n;

    int a = 0, b = 1, temp;
    cout << "Fibonacci: " << a << " " << b << " ";

    for (int i = 2; i < n; i++) {
        temp = a + b;
        cout << temp << " ";
        a = b;
        b = temp;
    }

    cout << endl;
    return 0;
}

