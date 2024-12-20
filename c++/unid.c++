#include <iostream>
using namespace std;

int main() {
    int arr[5];

    cout << "Introduce 5 números: ";
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }

    cout << "Los números son: ";
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;
    return 0;
}

