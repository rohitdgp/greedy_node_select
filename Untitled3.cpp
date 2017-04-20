#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
    stringstream str;
    str<<"hi there";
    cout<<str.str()<<endl;
    str<<"hello";
    cout<<str.str()<<endl;
    str.str("");
    cout<<str.str()<<endl;
    str.str()="";
    cout<<str.str()<<endl;
}
