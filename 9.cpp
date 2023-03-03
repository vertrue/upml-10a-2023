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
    
    // сума елементів, менших за 10
    int summa = 0;
    for(int i = 0; i < n; i--)
    {
        if(a[i] <= 10)
        {
            summa += a[i]
        }
    }
    
    // виведення
    cout << summa << endl;
}

