#include <bits/stdc++.h>
using namespace std;
//fuction to calculate z array/vector.
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
