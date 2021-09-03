#include<iostream>

using namespace std;

bool is_greater(int x, int y)
{
    if (x > y)
        return true; 
    else
        return false; 
}

int main()
{    
    if (is_greater(11, 2))
        cout << "x is greater than y" <<endl;
    else
        cout << "x is less than or equal to y" <<endl;

    return 0;
}