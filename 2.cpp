#include <iostream>

using namespace std;

//створюю функцію для порівняння елементів. Повертає менший з них
int min(int min_el,int i);

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
    
    // знаходження мінімуму
    int min_el = 0;
    for(int i = 1; i < n; i++)
    {
        min_el = min(min_el, a[i]);
    }
    
    // виведення максимального елемента
    cout << min_el << endl;
}

//реалізую функцію min
int min(int min_el,int i){
    if (min_el>i){
        return i;
    }
}
