/*For the sake of brevity, let's call segment matches those substrings that coincide with a prefix of s. For example, the value of the desired Z-function z[i] is the length of the segment match starting at position i (and that ends at position i+z[i]−1).
To do this, we will keep the [l,r] indices of the rightmost segment match. That is, among all detected segments we will keep the one that ends rightmost. In a way, the index r can be seen as the "boundary" to which our string s has been scanned by the algorithm; everything beyond that point is not yet known.
Then, if the current index (for which we have to compute the next value of the Z-function) is i, we have one of two options:
i>r -- the current position is outside of what we have already processed.
We will then compute z[i] with the trivial algorithm (that is, just comparing values one by one). Note that in the end, if z[i]>0, we'll have to update the indices of the rightmost segment, because it's guaranteed that the new r=i+z[i]−1 is better than the previous r.
i≤r -- the current position is inside the current segment match [l,r].
Then we can use the already calculated Z-values to "initialize" the value of z[i] to something (it sure is better than "starting from zero"), maybe even some big number.
For this, we observe that the substrings s[l…r] and s[0…r−l] match. This means that as an initial approximation for z[i] we can take the value already computed for the corresponding segment s[0…r−l], and that is z[i−l].
However, the value z[i−l] could be too large: when applied to position i it could exceed the index r. This is not allowed because we know nothing about the characters to the right of r: they may differ from those required.
*/


#include <bits/stdc++.h>
using namespace std;
//fuction to calculate z array/vector.
//O(N+m) N,m are length of text and patterns respectively.
vector<int> Z_array(string s)
{

    int n = s.size();
    vector<int> z_array(n);
    int ss = 0, es = 0;
    // ss== start segment es== end segment 
    //(ss and es is range of current segment which is prevoiusly occured/found.)
    for (int i = 1; i < n; ++i)
    {
        if (i <= es)
            z_array[i] = min(es - i + 1, z_array[i - ss]);
        while (i + z_array[i] < n && s[z_array[i]] == s[i + z_array[i]])
        //for maching characters we have to increase our range of segment and update the z_array
            z_array[i]++;
        if (i + z_array[i] - 1 > es)   
            //if we have already processed then we have to use prevoius value
            //for maintaining the condition l<=i<=r<=n ;
            ss = i, es = i + z_array[i] - 1;
    }
    return z_array;
}

int main()
{
    string text, pat;
    cin >> text >> pat;
    string total = pat + "@" + text;
    vector<int> output = Z_array(total); 
    for (int i = 0; i < output.size(); i++)
    {
        if (output[i] == pat.size())
        //To obtain the actual position of pattern in a given string.
        //we have to subtract the pattern length +1(1 for special character)
            cout << (i - pat.length() - 1) << " "; 
            
    }

    return 0;
}
