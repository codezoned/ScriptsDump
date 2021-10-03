//Description
//Knuth Morris Pratt Pattern Searching Algorithm
//The idea behind KMP’s algorithm is: whenever we detect a mismatch after some matches, we already know some of the characters in the text of the next window. 
//We take advantage of this information to avoid matching the characters that we know will anyway match.
//This algorithm is an optimization to naive string matching technique performed in O(text.length*pattern.length)
//
//KMP algorithm uses the concept of LPS(Longest Proper Prefix which is also a Proper Suffix)
//Prefix of abcd - a, ab, abc, abcd
//Proper Prefix of abcd - All prefixes except full string - a, ab, abc 
//First thing is to do preprocessing of text string and make a lps array that stores length of proper prefix that is also proper suffix till index i
//Also, there can be overlapping between the prefixes and suffixes while calculating the longest length.
//lps[0] = 0 as String made till index 0 will be a single character and that wont have any proper prefix or suffix thus longest length - 0
//For example:
//text -  aabaacaabaad
//lps[] - 010120123450


import java.util.Scanner;

public class KMP_Pattern_Matching {
	public static int[] LPS(String s){
	    int[]lps = new int[s.length()];
	    int i=1,len=0;
	    while(i<s.length()){
	        if(s.charAt(i)==s.charAt(len)){ //characters matched then value for this lps idx will be len's previous value + 1
	            len++;
	            lps[i] = len;
	            i++;
	        }
	        else{//characters unmatched then we need to find longest prefix and suffix length for this index
	            if(len>0){
	                len = lps[len-1];//check backwards 
	            }
	            else{
	                i++;//no matching len index found so lps[i] = 0 which is already filled from start so simply i++
	            }
	        }
	    }
	    return lps;
	}

	public static void KMP(String text, String pattern){
	    //Create a string by concatenating pattern and text and separated by a special character that can't be present in our text
	    String s = pattern+"#"+text;
	    
	    //Then we need to find the lps of this created string s. The maximum length of longest lps would be length of pattern only because that special character won't be present in our string
	    int[]lps = LPS(s);

	    //Now count all the indexes in this lps array starting from i=pattern.length where value of lps[i] == pattern.length
	    int cnt=0;
	    for(int i=pattern.length();i<s.length();i++){
	        if(lps[i]==pattern.length()){
	            cnt++;
	        }
	    }
	    System.out.println("Pattern is found in text "+cnt+" times");
	}
	
	public static void main(String[]args) {
		Scanner scn = new Scanner(System.in);
		String text = scn.nextLine();
		String pattern = scn.nextLine();
		KMP(text,pattern);
	}
}

//Overall Time Complexity of KMP is O(text.length+pattern.length)
