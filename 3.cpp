/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
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
    int zeros = 0;
    for(int i = 0; i < n; i++)
    {
        if(a[i] == 0) {
            zeros += 1;
        }
    }
    
    // виведення кількості нулів
    cout << zeros << endl;
}