#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        long long n;
        cin >> n;
        long long cc = (n * (n - 1)) / 2;
        cout << "Case " << i << ": ";
        if (cc % 2 == 0)
            cout << cc / 2 << endl;
        else
            cout << cc << "/" << 2 << endl;
    }
    return 0;
}