#include<bits/stdc++.h>
#include<fstream>
#define ll long long

using namespace std;

int main()
{
    ll n=0;
    string str;
    ifstream file;
    file.open("RandomMatrix.txt");
    getline(file,str);
    for(ll k=0;k<str.length();k++)
        if(str[k]=='0' || str[k]=='1') n++;

    cout<<" n ="<<n<<endl;
    file.close();

    file.open("file.txt");

    while(!file.eof() && str[0]!='N')
    {
        getline(file,str);
    }
    if(str[0]=='N')
    {
        for(ll i=0;i<6;i++)
            getline(file,str);
    }
    ll send[1002],rec[1002];
    memset(send,0,sizeof(send));
    memset(rec,0,sizeof(rec));
    cout<<str[0]<<" "<<str[1]<<" "<<str[6]<<endl;
    while(str[1]=='a')
    {
        //cout<<str[7];
        ll j=7,val=0,node=0;
        while(str[j]!=':')
        {
            node=node*10 + str[j]-'0';
            j++;
        }
        j+=2;
        while(j<str.length())
        {
            val=val*10 + str[j]-'0';
            j++;
        }
        send[node]=val;
        cout<<node<<" "<<val<<endl;
        getline(file,str);
    }
    getline(file,str);
    while(str[1]=='a')
    {
        //cout<<str[7];
        ll j=7,val=0,node=0;
        while(str[j]!=':')
        {
            node=node*10 + str[j]-'0';
            j++;
        }
        j+=2;
        while(j<str.length())
        {
            val=val*10 + str[j]-'0';
            j++;
        }
        rec[node]=val;
        cout<<node<<" "<<val<<endl;
        getline(file,str);
    }
    file.close();
    ofstream file1;
    file1.open("max_sum_wts.txt");
    for(ll i=1;i<=n;i++)
    {
        cout<<send[i]+rec[i]<<" ";
        file1<<send[i]+rec[i]<<" ";
    }
    file1<<endl;
    cout<<endl;

    /*for(ll i=1;i<=n;i++)
    {
        cout<<rec[i]<<" ";
        file1<<rec[i]<<" ";
    }
    file1<<endl;*/
    file1.close();
}
