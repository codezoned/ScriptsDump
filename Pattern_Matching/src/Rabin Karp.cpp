//#Rapin karp pattern searching algorithm
//#Best and average time complexity - O(n+m)
//#Worst case time complexity [O(nm)] when all characters of pattern and text are same
// as the hash values of all the substrings of txt[] match with hash value of pat[]

#include<bits/stdc++.h>
using namespace std;
int main()
{
        string s,pat;
        cin>>s>>pat;
        int n=s.size();
        int m=pat.size();
        int cnt=0;
        long long mod=1e9+7;
        // If length of string of string is >= than that of pattern
        if(n>=m)
        {
            //Calculating hash value for 1st m characters as well as for pattern also
            //hashfunction: [ hash+=pow(26,m - char no.)*hashcode_of_that_char ] for m characters
            int hashstring=0,j=0,hashpat=0;
            while(j<m)
            {
                hashstring=(hashstring + ( (s[j]-'a'+1) * int(pow(26,m-j-1))%mod ))%mod;
                hashpat=(hashpat + ( (pat[j]-'a'+1)*int(pow(26,m-j-1))%mod ))%mod;
                j++;
            }

            if(hashpat==hashstring)
                {
                	int i;
                	//matching pattern and substring
                	for( i=0;i<m;i++)
                	{
                		if(s[i]==pat[i]) 
                		 continue;
                		else 
                		 break;
					}
					if(i==m)
					 cnt++;
				}
				
            for(int i=1;i<n-m+1;i++)
            {
                //Ex:- for dbac, if length of pat is 3 and we want to calculate for index 1
                //then remove contribution of 'd' (at index 0) and add that of 'c' with proper degree in power

                hashstring-=( (s[i-1]-'a'+1) * int(pow(26,m-1))%mod )%mod;     //subtracting 1st string of previous group
                hashstring=(hashstring*26)%mod;                                //Increasing power of each remaining char by 1
                hashstring=(hashstring + (s[i+m-1]-'a'+1))%mod;       //Adding hashcode for new char in that group that that of previous one

                if(hashpat==hashstring)
                 {
                	int k;
                	// Matching pattern and substring
                	for( k=0;k<m;k++)           
                	{
                		if(s[k+i]==pat[k])
                		 continue;
                		else 
                		 break;
					}
					if(k==m)
					 cnt++;
				}
            }
            cout<<"No. of pattern found is "<<cnt;
        }
        else
            cout<<"String length is smaller than that of pattern";
    return 0;
}

//#Description
//Rabin karp is one of the efficient algorithm for pattern searching.
//It uses the concept that calculate the hashvalue for pattern
//Also calculate for substring of m characters and equate it with that of pattern one
//If it matches means 1 pattern found
