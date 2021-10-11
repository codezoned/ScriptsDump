// Prime Seive aka Sieve of Eratosthenes
// Time complexity : O(n*log(log(n)))
// Space complexity: O(n)
// DESC : here we will discuss how to find prime numbers in a given range 
#include <bits/stdc++.h>

using namespace std;

void sieve(vector<bool>& isprime, int n){
    // since 0 and 1 are non-prime numbers we mark them as false;
    isprime[0] = isprime[1] = false;
    // 1st method
    for(int i = 2; i * i <= n; i++){
        if(isprime[i] == true){ //if we find i'th number to be a prime number, we will mark every multiple of that number as non-prime
            for(int j = i*i ; j <= n; j += i){
                isprime[j] = false;
            }
        }
    }
    // here we are iterating every element from 2 to sqrt(n), but since we know that 2 is the only even prime number
    // this can be further optimized to
    // first we will mark every multiple of 2, and then in the next loop we will iterating only for odd numbers 
    // 2. more optimized
    for(int i = 2; i < 3; i++){
        if(isprime[i] == true){ //if we find i'th number to be a prime number, we will mark every multiple of that number as non-prime
            for(int j = i*i ; j <= n; j += i){
                isprime[j] = false;
            }
        }
    }
    for(int i = 3; i * i <= n; i += 2){ // will only check for odd number
        if(isprime[i] == true){ //if we find i'th number to be a prime number, we will mark every multiple of that number as non-prime
            for(int j = i*i ; j <= n; j += i){
                isprime[j] = false;
            }
        }
    }
    // now in the isprime vector we have prime numbers from 0 to 1000000
    // note that we are using isprime vector of boolean data type and not integer as it will reduce space (integer takes 4bytes, whereas bool takes 1byte)
}

signed main(){
    int n=1e6;
    //initialize a vector isprime such that if value at an index is true then it is a prime number, else a composite
    //initially we consider every number as prime
    vector<bool> isprime(n+1,true);  
    sieve(v,n);

    return 0;
}