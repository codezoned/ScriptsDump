#include<bits/stdc++.h>
using namespace std;
//naive approach for finding Z  function array(i.e. z[i] is the length of the longest string that is, at the same time, a prefix of s and a prefix of the suffix of s starting at i.)
// i-th element is equal to the greatest number of characters starting from the position i that coincide with the first characters of s.
//O(n^2)
vector<int>Z_function(string s){
    int n = s.size();
    //store the values of z function
    vector<int> z(n,0); 
    //Traversing the whole string 
    for (int i = 1; i < n; ++i)
    //comparing the characters and incresing the range 
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];
    return z;
}
int main(){
    string text;
    string pat;
    cin>>text>>pat;
    string total=pat+"$"+text;
    vector<int>OutputIndices=Z_function(total);
    for(auto i=0;i<OutputIndices.size();i++){
        if(OutputIndices[i]==pat.size()){
            cout<<(i-pat.size()-1)<<" ";
        }
    }
    
    
    return 0;
}