//Method to calculate the prime factors of a given number
//Time complexity is almost square root of n or we can say O(sqrt(n)logn).
//space complexity is almost constant.
//Note:  Base of log function is 2.
#include<bits/stdc++.h>
using namespace std;
vector<int> primeFactors(int n){
    vector<int>res;
    for(int i=2;i<=sqrt(n);i++){
        if(n%i==0){
            int powercnt=0;
            //divide untill unless it is divisible.
            while(n%i==0){
                n/=i;
                powercnt++;
            }
            while(powercnt--){
                res.push_back(i);
            }
        }
    }
    // if still n is still remaining that means it is prime number and 
    //also we are traversing only to sqrt of n so we have to count it.
    if(n>1) res.push_back(n);
    return res;
}

int main(){
    int n;
    cin>>n;
    vector<int>factors=primeFactors(n);
    // the factors
    for(int j=0;j<factors.size();j++){
        cout<<factors[j]<<' ';
    }
    return 0;
}