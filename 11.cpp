#include <iostream>

using namespace std;

int main()
{
    // розмір масиву
    int n;
    cin >> n;
    
    // створення масиву
    int a[n]
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    
    // чи є хоча б 3 нулі
    int zeros = 0;
    for(int i = 1; i < n; i++)
    {
        if(a[i] = 0)
        {
            zeros += 1
        }
    }
    
    // виведення
    if(zeros > 3)
        cout << "є" << endl;
    else
        cout << "нема" << endl;
}

