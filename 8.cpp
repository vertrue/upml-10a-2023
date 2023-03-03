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
    
    // сума елементів, які менші за 5
    intl summa = 0
    for(int i = 1; i < n; i++)
    {
        if(a[i] < 5)
        {
            summa += a[i];
        }
    }
    
    // виведення
    cout << summa << endl;
}

