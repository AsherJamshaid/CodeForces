#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
 
using namespace std;
 
int main(void){
	int t;
	cin >> t;
	vector <int> arr;
	for(int i = 0;i<t;i++){
		int a,b;
		cin >> a >> b;
		int min = 1110;
		int result = 0;
		if(a==b){
			arr.push_back(0);
		}
		else{
			for(int j = a;j<b;j++){
				result = (j-a) + (b-j);
				if(result < min){
					min = result;
			}
			
		}
		arr.push_back(min);
		}
		
	}
	
	for(int i = 0;i<t;i++){
		cout << arr[i] << endl;
	}
}