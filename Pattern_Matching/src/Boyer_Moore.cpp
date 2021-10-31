// Boyer Moore String Matching Algorithm
// Best Case time complexity O(n/m)
// Average Case time complexity O(n)
// Worst Case time complexity O(nm)

#include <bits/stdc++.h>
using namespace std;
# define NO_OF_CHARS 256

// The preprocessing function for Boyer Moore's
// bad character Function
void badCharacter( string str, int size, int badChar[NO_OF_CHARS])
{
	// Fill the last occurrence of a character
	for (int i = 0; i < size; i++)
		badChar[(int) str[i]] = i;
}

/* A pattern searching function that uses Bad
Character Heuristic of Boyer Moore Algorithm */
void search( string txt, string pat)
{
	int m = pat.size();
	int n = txt.size();

	int badChar[NO_OF_CHARS]={-1};

	/* Fill the bad character array by function badCharHeuristic() for given pattern */
	badCharacter(pat, m, badChar);

	int s = 0; // s is shift of the pattern with respect to text

	while(s <= (n - m))
	{
		int j = m - 1;

		/* Keep reducing index j of pattern while
		characters of pattern and text are
		matching at this shift s */
		while(j >= 0 && pat[j] == txt[s + j])
			j--;

		/* If the pattern is present at current
		shift, then index j will become -1 after
		the above loop otherwise not less than 0*/
		if (j < 0)
		{
			cout << "pattern occurs at shift = " << s << endl;

			/* Shift the pattern so that the next
			character in text aligns with the last
			occurrence of it in pattern.
			The condition s+m < n is necessary for
			the case when pattern occurs at the end
			of text */
			s += (s + m < n)? m-badChar[txt[s + m]] : 1;

		}

		else
			/* Shift the pattern so that the bad character
			in text aligns with the last occurrence of
			it in pattern. The max function is used to
			make sure that we get a positive shift.
			We may get a negative shift if the last
			occurrence of bad character in pattern
			is on the right side of the current
			character. */
			s += max(1, j - badChar[txt[s + j]]);
	}
}


int main()
{
	string txt= "CCACACCABCABCD";
	string pat = "ABCD";
	search(txt, pat);
	return 0;
}

// Description
// Boyer Moore algorithm starts matching from the last character of the pattern
// It preprocesses the pattern and creates different arrays for last occurrence of each of the characters in string .
// At every step, it slides the pattern by the max of the slides suggested .
