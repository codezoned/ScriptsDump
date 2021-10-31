/*Let, f be some reversible function and A be an array of integers of length N.
Fenwick tree is a data structure which:
        1.calculates the value of function f in the given range [l,r] (i.e. f(Al,Al+1,…,Ar)) in O(logn) time;
        2.updates the value of an element of A in O(logn) time;
        3.requires O(N) memory, or in other words, exactly the same memory required for A;
        4.is easy to use and code, especially, in the case of multidimensional arrays.
Note:- 
        Fenwick tree is also called Binary Indexed Tree, or just BIT .
Application:-
        calculating the sum of a range (i.e. f(A1,A2,…,Ak)=A1+A2+⋯+Ak).  */
#include <bits/stdc++.h>
using namespace std;


int FNT[1000000] = {0}; //fenwick tree array
int query(int i)
{
        int ans = 0;
        while (i > 0)
        {
                ans += FNT[i];
                i = i - (i & (-i));
        }
        return ans;
}
void Build_update(int i, int inc, int N)
{
        while (i <= N)
        {
                FNT[i] += inc;
                i += (i & (-i));
        }
}
int main()
{
        
        int n;
        cin >> n;
        int a[n];
        for (int i = 1; i <= n; i++)
        {
                cin >> a[i];
                Build_update(i, a[i], n);
        }
        int q, l, r;
        cin >> q;
        while (q--)
        {
                cin >> l >> r;
                cout << (query(r) - query(l - 1)) << endl;
        }
        return 0;
}