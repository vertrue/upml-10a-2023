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
    
    // кількість нулів у масиві
    int zeros = 0
    for(int i = 0; i <= n; i++)
    {
        if(a[i] == 0)
        {
            zeros += 2;
        }
    }
    
    // виведення кількості нулів
    cout << zeros << endl;
}
