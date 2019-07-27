// maxexpression.cpp
// Johan Book
//
// This is an attempt to solve https://open.kattis.com/problems/maxexpression

#include<algorithm> // min, reverse, sort
#include<iostream> // cin
#include<math.h> // pow, round
#include<vector> // vector
using namespace std;

int N, n0, n1, n2;
const bool DEBUG = false;

// Like min but returns zero instead of negative numbers
int minx(int a, int b)
{
	int x = min(a,b);
	if (x < 0) 
		return 0;
	else
		return x;
}

// Subfunction to summ
void tot(int& x, int& m, int& n)
{
	m = minx(n,x);
	x -= m;
	n -= m;
}

// Determines how 2,1 and 0 are spent
// If zerod is true then 2s are priotized first
double summ(int x, bool zerod)
{
	// Numbers used in iteration
	int m0 = 0;
	int m1 = 0;
	int m2 = 0; 
	
	// If not enough 1s and 2s to fill positive then use zeros
	if(n1 + n2 < x)
		zerod = false;

	// Prioritize 2s, then 1s then 0s
	if(zerod)
	{
		tot(x,m2,n2);
		tot(x,m1,n1);
		tot(x,m0,n0);
	} 
	
	// Prioritize 0s, then 1s then 2s
	if(!zerod)
	{
		tot(x,m0,n0);
		tot(x,m1,n1);
		tot(x,m2,n2);
	}
	
	if(m0 > 0)
		return 0;

	return pow(2,m2); // idiot proof
}

void outp(vector<int> X)
{
	for(int x : X)
		cout << x << " ";
	cout << "\n";
}

// Main function
int main()
{
	// Input
	string c;
	cin >> N;
	cin >> c;
	cin >> n0 >> n1 >> n2;

	// Vectors to store numbers
	vector<int> positive;
	vector<int> negative;

	// Parse string into groups
	bool sign = true; // the first term is always positive
	int n = 1;
	for(int i =1; i < 2*N; i+=2)
	{
		// Increase group or store it
		if(c[i] == '*')
			n++;
		else
		{
			if(sign) 
				positive.push_back(n);
			else
				negative.push_back(n);

			n = 1;
		}
		
		// Store sign
		if(c[i] == '+') 
			sign = true;
		if(c[i] == '-') 
			sign = false;
	}

	// Sort vectors in reverse order
	sort(positive.begin(), positive.end());
	sort(negative.begin(), negative.end());
	reverse(positive.begin(), positive.end());
	reverse(negative.begin(), negative.end());
	
	// Debug printing
	if(DEBUG)
	{
		cout << N << ": " << n0 << " 0s, " << n1 << " 1s, " << n2 << " 2s\n";  
		cout << "+ "; outp(positive);
		cout << "- ";  outp(negative);
	}

	// Calculate max value
	double sum = 0;
	bool zerod[negative.size()];
	for(int i = 0; i < negative.size(); i++)
		zerod[i] = false;

	// Distribute as many zeros as possible to negative numbers
	for(int i = 0; 0 < n0 && i < negative.size(); i++)
	{
		zerod[i] = true;
		negative[i]--;
		n0--;
	}
	
	// Spend 0,1 and 2s for positive numbers
	for(int x : positive)
		sum += summ(x, true);

	// Spend 0,1 and 2s for negative numbers
	for(int i = 0; i < negative.size(); i++)
	{
		int tmp = summ(negative[i], zerod[i]);
		if(!zerod[i])
			sum -= tmp;
	}

	cout << round(sum) << endl;

	return 0;
}
