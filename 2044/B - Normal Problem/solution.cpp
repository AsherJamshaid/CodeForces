#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
 
using namespace std;
 
int main(void){
	int t;
	cin >> t;
	vector <string> arr;
	for(int i = 0;i<t;i++){
		string st1;
		cin >> st1;
		
		reverse(st1.begin(),st1.end());
		
		for(int j = 0;j<st1.length();j++){
			if(st1[j] == 'p'){
				st1[j] = 'q';
			}
			else if(st1[j] == 'q'){
				st1[j] = 'p';
			}
		}
		
		arr.push_back(st1);
	}
	
	
	for(int i = 0;i<t;i++){
		cout << arr[i] << endl;
	}
}