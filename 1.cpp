#include <iostream>
#include <math>

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
    
    // знаходження максимуму
    int max_el = 0;
    for(int i = 1; i < n; i++)
    {
        max_el = max(max_el, a[i]);
    }
    
    // виведення максимального елемента
    cout << max_el << endl;
}
