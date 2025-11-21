//KATRAYOSHKA
//
//#include<iostream>
//#include<algorithm>
//using namespace std;
//
//int main()
//{
//	long long n,m,k;
//	cin>>n>>m>>k;
//	long long ans = 0;
//	long long a,b,c;
//	if(n==0 || k==0) cout<<0;
//	else if(n>0 && k>0) 
//	{ 
////		ans = max(min(n/2,k),(min(n/2,(m,k)),min({n,m,k});
//		a = min({n/2,k});
//		b = min({n/2,m,k});
//		c = min({n,m,k});
//		cout<<a+b+c;
////		cout<<ans;
//	}
//	
//}

#include<iostream>
using namespace std;

int main()
{
	long long n,m,k;
	cin>>n>>m>>k;
	
//	if(n or k == 0)  cout<<0;
		
	long long mn1 = min(n,min(m,k));
	n-=mn1;
	m-=mn1;
	k-=mn1;
	
	long long use_no_mouth = min(n/2,k);
	long long ans = mn1 + use_no_mouth ;
	cout<<ans;

	
	return 0;
}










