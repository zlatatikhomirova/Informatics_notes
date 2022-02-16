#include <iostream>

using namespace std;
int imp(int, int);
int main()
{
    for (int x = 0; x < 2; x++)
        for (int y = 0; y < 2; y++)
            for (int z = 0; z < 2; z++)
                if (imp((x||y), z))
                    cout << x << " " << y << " " << z << endl;

    return 0;
}
int imp(int x, int y)
{
    return (x && (!y));
}
