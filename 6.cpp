#include <iostream>

using namespace std;

int main()
{
    // розмір масиву
    int n;
    cout<< "Введіть розмір масиву: ";
    cin >> n;
    cout << "Введіть елементи масиву: " << endl;
    
    // створення масиву
    int a[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    
    // сума елементів на непарних місцях (нумерація з 0)
    int summa = 0;
    for(int i = 1; i < n; i = i + 2)
    {   
        summa += a[i];
    }
    
    // виведення
    cout << "сума елементів на непарних місцях (нумерація з 0): ";
    cout << summa << endl;
}
