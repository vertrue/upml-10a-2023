#include <iostream>

using namespace std;

int main()
{
    // розмір масиву
    int n;
    cin >> n;
    
    // створення масиву
    int a[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    
    // сума елементів на парних місцях (нумерація з 0)
    int summa = 0;
    for(int i = 1; i < n; i++)
    {
        if(a[i] % 2 = 0)
        {
            summa += a[i];
        }
    }
    
    // виведення
    cout << summa << endl;
}

