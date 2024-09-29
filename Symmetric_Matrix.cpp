#include <bits/stdc++.h>
using namespace std;

int main()
{
    int q;
    cin >> q;
    for (int t = 0; t < q; t++)
    {
        string s;
        int n;
        cin >> s >> s >> n;
        long long arr[n][n];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> arr[i][j];
            }
        }
        bool flag = true;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (arr[i][j] < 0 || arr[i][j] != arr[n - 1 - i][n - 1 - j])
                {
                    flag = false;
                    break;
                }
            }
            if (!flag)
            {
                break;
            }
        }

        if (flag)
        {
            cout << "Test #" << t + 1 << ": Symmetric." << endl;
        }
        else
        {
            cout << "Test #" << t + 1 << ": Non-symmetric." << endl;
        }
    }
    return 0;
}
