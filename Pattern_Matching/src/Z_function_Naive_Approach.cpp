#include<bits/stdc++.h>
using namespace std;
//naive approach for finding Z  function array(i.e. z[i] is the length of the longest string that is, at the same time, a prefix of s and a prefix of the suffix of s starting at i.)
// i-th element is equal to the greatest number of characters starting from the position i that coincide with the first characters of s.
//O(n^2)
vector<int>Z_function(string s){
    int n = s.size();
    //vector z store the  z  values 
    //i.e.(i-th element is equal to the greatest number of characters starting from the position i that coincide with the first characters of s)
    vector<int> z(n,0); 
    //Traversing the whole string 
    for (int i = 1; i < n; ++i)
    //comparing the characters and incresing the range i.e. length of substring which previously exists 
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];
    return z;
}

int main(){
    string text;
    string pat;
    cin>>text>>pat;
    //making a temporary string total
    string total=pat+"$"+text;
    vector<int>OutputIndices=Z_function(total);
    //Z_function will return the array/vector of indices ie
    //i-th element is equal to the greatest number of characters starting from the position i that coincide with the first characters of temporary string total.
    //if size of pattern matches with any value of vector returned by z_function it means our pattern found in temporary string 
    // but to  get real index of pattern in given text we have to substract  pattern length and 1 (for special character) from the index of vector returned by Z_function.
    for(auto i=0;i<OutputIndices.size();i++){
        if(OutputIndices[i]==pat.size()){
            
            cout<<(i-pat.size()-1)<<" ";
        }
    }
    
    
    return 0;
}
