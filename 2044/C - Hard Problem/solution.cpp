#include <iostream>
#include <vector>
using namespace std;
 
int main(void){
	int t,m,a,b,c;
	cin >> t;
	vector <int> arr;
	for(int i = 0;i<t;i++){
		int total = 0;
		cin >> m >> a >> b >> c;
		int row1 = m;
		int row2 = m;
		
		if(row1 >= a){
			total+=a;
			row1-=a;
		}
		else{
			total+=row1;
			row1 = 0;
		}
		if(row2 >=b){
			total+=b;
			row2-=b;
		}
		else{
			total+=row2;
			row2=0;
		}
		
		if((row1 + row2) >= c){
			total+=c;
		}
		else{
			total+=(row1+row2);
		}
		arr.push_back(total);
	}
	for(int i = 0;i<t;i++){
		cout << arr[i] << endl;
	}
}