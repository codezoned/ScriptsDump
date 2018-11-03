//Simple Boyer Moore string matching algorithm. Only bad character rule is used.


#include <iostream>
#include <string>
using namespace std;

// Main driver of the program. It gives the last occurence of the character in a pattern

int last(string p, char c){
    int last = p.length()-1;
    for (int i = p.length()-1; i>=0; i--){
        if (p[i] == c) {
            if (i<last){
                last = i;
            }
        }
    }
    if (last == p.length()-1){
        return -1;
    }
    return last;
}

//String matching algorithm

int BM (string text, string pat){
    int n = text.length(); int m = pat.length();
    int i = m - 1;
    int j = m - 1;
    int index;

    while (true){
        if (text[i] == pat[j]){
            if (j == 0){
                return i;
            }
            i--;
            j--;
        }
        else if (i<=0){
            cout<<"here"<<endl;
        }
        else {
            i = i + m - min(j, 1+last(pat, text[i]));
            j = m - 1;
        }
    }
    return n+1;
}
int main(){
  return 0;
}
