#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;
void find(string word) {
    string line;
    int count = 0;
   
    ifstream myfile ("/Users/swe_mini/Desktop/a.txt");
    

    if (myfile.is_open())
        
    {
        while(getline(myfile, line)){
            
            if(line.find(word) != string::npos){
                //cout << word << endl;
                count ++;
                
                
            }
           
        }
        
        cout <<"its -- > "<<count << endl;
        
        
        
        
        myfile.close();
        
    }
    
    else cout << "Unable to open file";
}

int main () {
    
    string line;
    //string word = "elder	High	High School	Wife	relative	Female	gain	relax	United-States	>50K";
    int count = 0;

    
    typedef map<string, int> line_record;
    line_record lines;
    int line_number = 1;
    
    
    ifstream mergeFile ("/Users/swe_mini/Desktop/merge.txt");
    ifstream myfile ("/Users/swe_mini/Desktop/a.txt");
    
    if (mergeFile.is_open())
    {
        while ( getline (mergeFile,line) )
        {
            line_record::iterator existing = lines.find(line);
            if(existing != lines.end())
            {
                existing->second = (-1);
                
            } else
            {
                lines.insert(make_pair(line,line_number));
                ++line_number;
                
                find(line);
                count++;
            }
            
            
            
        }
        mergeFile.close();
    }
    
    else cout << "Unable to open file";
    
    
    return 0;
    
}
