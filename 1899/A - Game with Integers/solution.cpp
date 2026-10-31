#include <bits/stdc++.h>
#include <vector>
using namespace std;
 
int main() {
    vector<string> result;
	int t;
	cin >> t;
	for(int i  = 0;i<t;i++){
	    int a;
	    cin >> a;
	    if(((a+1) % 3 == 0) || ((a-1) % 3 == 0)){
	        result.push_back("First");
	    }
	    else{
	        result.push_back("Second");
	    }
	}
	for(int i = 0;i<t;i++){
	    cout << result[i] << endl;
	}
 
}